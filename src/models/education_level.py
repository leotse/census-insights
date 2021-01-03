from sqlalchemy import Column, Integer, String

from .base import CanadaCensusBase


class EducationLevel(CanadaCensusBase):
    __tablename__ = "education_levels"

    total = Column(Integer)
    no_diploma = Column(Integer)
    secondary_school_diploma = Column(Integer)
    apprenticeship_trades_diploma = Column(Integer)
    college_diploma = Column(Integer)
    university_diploma_below_bachelor = Column(Integer)
    bachelor_degree = Column(Integer)
    university_diploma_above_bachelor = Column(Integer)
    medical_degree = Column(Integer)
    masters_degree = Column(Integer)
    earned_doctorate = Column(Integer)
