from pprint import pprint

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from models.age_group import AgeGroup
from utils.census_utils import get_age_group_stats, iterate_census_area


def _iterate_census_area_batch(batch_size: int = 100, max_rows: int = 2000):
    i = 0
    batch = []
    for area_stats in iterate_census_area():
        if i >= max_rows:
            break

        if len(batch) == batch_size:
            yield batch
            batch = []

        batch.append(area_stats)
        i += 1

    yield batch


def load_census_to_db(session: Session, batch_size: int = 100, max_areas: int = 500):
    i = 0
    for area_stats_batch in _iterate_census_area_batch(batch_size, max_areas):
        print(f"processing batch: {i} size: {batch_size}")
        session.bulk_insert_mappings(
            AgeGroup,
            [get_age_group_stats(area_stats) for area_stats in area_stats_batch],
        )
        i += 1


if __name__ == "__main__":
    engine = create_engine("postgres://postgres@db/census_canada")
    session = Session(engine)
    try:
        session.execute(text(f"TRUNCATE TABLE {AgeGroup.__tablename__}"))
        session.commit()
        
        load_census_to_db(session)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
