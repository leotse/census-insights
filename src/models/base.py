from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ModelBase(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class CanadaCensusBase(ModelBase):
    __abstract__ = True

    year = Column(Integer, index=True)
    geo_code = Column(String, index=True)
    geo_name = Column(String)
    geo_level = Column(Integer)
