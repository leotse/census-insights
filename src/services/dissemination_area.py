from geoalchemy2.shape import to_shape
from shapely.geometry import mapping
from sqlalchemy import func

from models import Session
from models.dissemination_area import DisseminationArea


def query_dissemination_area(lng: float, lat: float):
    session = Session()
    try:
        filter = func.ST_Contains(DisseminationArea.geometry, f"SRID=4326;POINT({lng} {lat})")
        da = session.query(DisseminationArea).filter(filter).first()
        if not da:
            return None
        return {
            "id": da.id,
            "province_name": da.province_name,
            "census_division_name": da.census_division_name,
            "census_consolidated_subdivision_name": da.census_consolidated_subdivision_name,
            "census_subdivision_name": da.census_subdivision_name,
            "economic_region_name": da.economic_region_name,
            "census_metro_area_name": da.census_metro_area_name,
            "census_tract_name": da.census_tract_name,
            "geometry": mapping(to_shape(da.geometry)),
        }
    except:
        session.rollback()
        raise
    finally:
        session.close()
