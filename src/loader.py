from pprint import pprint
from typing import Optional

import geopandas as gpd
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from models.age_group import AgeGroup
from models.dissemination_area import DisseminationArea
from models.education_level import EducationLevel
from models.income_group import IncomeGroup
from utils.census_utils import (
    get_age_group_stats,
    get_education_levels,
    get_income_groups,
    iterate_census_area,
)


def _iterate_census_area_batch(batch_size: int = 100, max_areas: Optional[int] = None):
    i = 0
    batch = []
    for area_stats in iterate_census_area():
        if max_areas is not None and i >= max_areas:
            break

        if len(batch) == batch_size:
            yield batch
            batch = []

        batch.append(area_stats)
        i += 1

    yield batch


def load_census_to_db(
    session: Session,
    batch_size: int = 100,
    max_areas: Optional[int] = None,
):
    i = 0
    for area_stats_batch in _iterate_census_area_batch(batch_size, max_areas):
        print(f"processing batch: {i} size: {batch_size} max_areas: {max_areas}")
        session.bulk_insert_mappings(
            AgeGroup,
            [get_age_group_stats(area_stats) for area_stats in area_stats_batch],
        )
        session.bulk_insert_mappings(
            IncomeGroup,
            [get_income_groups(area_stats) for area_stats in area_stats_batch],
        )
        session.bulk_insert_mappings(
            EducationLevel,
            [get_education_levels(area_stats) for area_stats in area_stats_batch],
        )
        i += 1


def load_dissemination_area_to_db(session: Session):
    path_shp = "/data/lda_000b16a_e/lda_000b16a_e.shp"
    df = gpd.read_file(path_shp)

    # rename columns to match sql column names
    df = df.rename(
        {
            "DAUID": "dissemination_area_id",
            "PRUID": "province_id",
            "PRNAME": "province_name",
            "CDUID": "census_division_id",
            "CDNAME": "census_division_name",
            "CDTYPE": "census_division_type",
            "CCSUID": "census_consolidated_subdivision_id",
            "CCSNAME": "census_consolidated_subdivision_name",
            "CSDUID": "census_subdivision_id",
            "CSDNAME": "census_subdivision_name",
            "CSDTYPE": "census_subdivision_type",
            "ERUID": "economic_region_id",
            "ERNAME": "economic_region_name",
            "SACCODE": "statistical_area_classification_code",
            "SACTYPE": "statistical_area_classification_type",
            "CMAUID": "census_metro_area_id",
            "CMAPUID": "census_metro_area_province_id",
            "CMANAME": "census_metro_area_name",
            "CMATYPE": "census_metro_area_type",
            "CTUID": "census_tract_id",
            "CTNAME": "census_tract_name",
            "ADAUID": "aggregated_dissemination_area_id",
        },
        axis="columns",
    )

    # project to lat/lon coordinates
    print("projecting to epsg:4326")
    df = df[:50].to_crs("epsg:4326")  # TODO: remove debug limit
    df["geometry"] = df.geometry.apply(lambda s: f"SRID=4326;{s.wkt}")

    # finally write to db
    print("writing to db")
    session.bulk_insert_mappings(DisseminationArea, df.to_dict("records"))


if __name__ == "__main__":
    engine = create_engine("postgres://postgres@db/census_canada")
    session = Session(engine)
    try:
        # session.execute(text(f"TRUNCATE TABLE {AgeGroup.__tablename__}"))
        # session.execute(text(f"TRUNCATE TABLE {IncomeGroup.__tablename__}"))
        # session.execute(text(f"TRUNCATE TABLE {EducationLevel.__tablename__}"))
        # session.commit()
        # load_census_to_db(session, batch_size=200, max_areas=5038)
        # session.commit()

        session.execute(text(f"TRUNCATE TABLE {DisseminationArea.__tablename__}"))
        session.commit()
        load_dissemination_area_to_db(session)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
