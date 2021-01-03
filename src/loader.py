from pprint import pprint
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from models.age_group import AgeGroup
from models.income_group import IncomeGroup
from utils.census_utils import (
    get_age_group_stats,
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
        i += 1


if __name__ == "__main__":
    engine = create_engine("postgres://postgres@db/census_canada")
    session = Session(engine)
    try:
        session.execute(text(f"TRUNCATE TABLE {AgeGroup.__tablename__}"))
        session.commit()

        load_census_to_db(session, batch_size=5, max_areas=12)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
