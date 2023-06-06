from sqlalchemy import Column, Integer, String, Boolean, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base

from api import db

# Base = declarative_base()


class SegmentModel(db.Model):
    __tablename__ = 'segment'

    id = Column(Integer, primary_key=True)
    professional_id = Column(Integer. foreingn_key=True)
    segment = Column(String)


query_class = db.session.query_property()