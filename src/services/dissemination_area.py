from typing import List

from geoalchemy2.shape import to_shape
from shapely.geometry import mapping
from sqlalchemy import func, or_

from api_models import LngLat
from models.dissemination_area import DisseminationArea
from decorators import use_db


@use_db
def query_dissemination_area_by_lnglats(lnglats: List[LngLat], *, session=None):
    if not lnglats:
        return []
    location_filters = [
        func.ST_Contains(DisseminationArea.geometry, f"SRID=4326;POINT({lnglat.lng} {lnglat.lat})")
        for lnglat in lnglats
    ]
    query = session.query(DisseminationArea).filter(or_(*location_filters))
    return [area.to_dict() for area in query.all()]
