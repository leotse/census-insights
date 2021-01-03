from sqlalchemy import Column, Integer, String

from .base import CanadaCensusBase


class AgeGroup(CanadaCensusBase):
    __tablename__ = "age_groups"

    id = Column(Integer, primary_key=True)

    year = Column(Integer, index=True)
    geo_code = Column(String, index=True)
    geo_name = Column(String)
    geo_level = Column(Integer)

    total = Column(Integer)
    age_0_to_4 = Column(Integer)
    age_5_to_9 = Column(Integer)
    age_10_to_14 = Column(Integer)
    age_15_to_19 = Column(Integer)
    age_20_to_24 = Column(Integer)
    age_25_to_29 = Column(Integer)
    age_30_to_34 = Column(Integer)
    age_35_to_39 = Column(Integer)
    age_40_to_44 = Column(Integer)
    age_45_to_49 = Column(Integer)
    age_50_to_54 = Column(Integer)
    age_55_to_59 = Column(Integer)
    age_60_to_64 = Column(Integer)
    age_65_to_69 = Column(Integer)
    age_70_to_74 = Column(Integer)
    age_75_to_79 = Column(Integer)
    age_80_to_84 = Column(Integer)
    age_85_plus = Column(Integer)
