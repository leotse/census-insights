from geoalchemy2.shape import to_shape
from shapely.geometry import mapping
from sqlalchemy import func

from models.dissemination_area import DisseminationArea


def query_dissemination_area(lng: float, lat: float, *, session=None):
    filter = func.ST_Contains(DisseminationArea.geometry, f"SRID=4326;POINT({lng} {lat})")
    da = session.query(DisseminationArea).filter(filter).first()
    if not da:
        return None
    return da.to_dict()
