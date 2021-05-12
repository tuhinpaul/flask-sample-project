from sqlalchemy import Column, Integer, String, Float

from .base import Base

class UserRole(Base):
    __tablename__ = 'UserRole'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer)
    roleId = Column(Integer)
