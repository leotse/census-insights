from sqlalchemy import select

from models.age_group import AgeGroup


def query_stats(dissemination_area_id: str, *, session=None):
    age_groups = session.query(AgeGroup).filter(AgeGroup.geo_code == dissemination_area_id).first()
    return age_groups.to_dict()
