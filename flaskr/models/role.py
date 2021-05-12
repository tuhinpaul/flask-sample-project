from sqlalchemy import Column, Integer, String, Float

from .base import Base

class Role(Base):
    __tablename__ = 'Role'
    id = Column(Integer, primary_key=True)
