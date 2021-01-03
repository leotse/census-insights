from sqlalchemy import Column, Integer, String

from .base import CanadaCensusBase


class IncomeGroup(CanadaCensusBase):
    __tablename__ = "income_groups"

    total = Column(Integer)
    income_10k_to_20k = Column(Integer)
    income_20k_to_30k = Column(Integer)
    income_30k_to_40k = Column(Integer)
    income_40k_to_50k = Column(Integer)
    income_50k_to_60k = Column(Integer)
    income_60k_to_70k = Column(Integer)
    income_70k_to_80k = Column(Integer)
    income_80k_to_90k = Column(Integer)
    income_90k_to_100k = Column(Integer)
    income_100k_to_150k = Column(Integer)
    income_150k_plus = Column(Integer)
