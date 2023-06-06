from sqlalchemy import Column, Integer, String, Boolean, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base

from api import db


# Base = declarative_base()


class ProfessionalModel(db.Model):
    __tablename__ = 'professional'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    project = Column(String)
    responsible = Column(String)
    work_experience = Column(Integer)
    level = Column(Numeric)
    hour_value = Column(Numeric)
    salary = Column(Numeric)
    current_work = Column(String)
    to_be_rated = Column(Boolean)
    data_created = Column(DateTime)

    # segments = relationship('SegmentModel', backref='professional', lazy='dynamic')


query_class = db.session.query_property()
