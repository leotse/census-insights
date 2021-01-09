from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from config import get_db_url

from .age_group import AgeGroup
from .dissemination_area import DisseminationArea
from .education_level import EducationLevel
from .income_group import IncomeGroup

_db_url = get_db_url()
_engine = create_engine(_db_url)
Session = sessionmaker(bind=_engine)
