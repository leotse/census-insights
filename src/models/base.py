from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CanadaCensusBase(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    year = Column(Integer, index=True)
    geo_code = Column(String, index=True)
    geo_name = Column(String)
    geo_level = Column(Integer)
