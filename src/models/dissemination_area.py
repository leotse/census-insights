from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry

from .base import Base


class DisseminationArea(Base):
    __tablename__ = "dissemination_area"

    id = Column(Integer, primary_key=True)

    dissemination_area_id = Column(String(8))  # DAUID
    province_id = Column(String)  # PRUID
    province_name = Column(String)  # PRNAME
    census_division_id = Column(String(4))  # CDUID
    census_division_name = Column(String(100))  # CDNAME
    census_division_type = Column(String(3))  # CDTYPE
    census_consolidated_subdivision_id = Column(String(7))  # CCSUID
    census_consolidated_subdivision_name = Column(String(100))  # CCSNAME
    census_subdivision_id = Column(String(7))  # CSDUID
    census_subdivision_name = Column(String(100))  # CSDNAME
    census_subdivision_type = Column(String(3))  # CSDTYPE
    economic_region_id = Column(String(4))  # ERUID
    economic_region_name = Column(String(100))  # ERNAME
    statistical_area_classification_code = Column(String(4))  # SACCODE
    statistical_area_classification_type = Column(String(1))  # SACTYPE
    census_metro_area_id = Column(String(3))  # CMAUID
    census_metro_area_province_id = Column(String(5))  # CMAPUID
    census_metro_area_name = Column(String(100))  # CMANAME
    census_metro_area_type = Column(String(1))  # CMATYPE
    census_tract_id = Column(String(10))  # CTUID
    census_tract_name = Column(String(7))  # CTNAME
    aggregated_dissemination_area_id = Column(String(8))  # ADAUID
    geometry = Column(Geometry())
