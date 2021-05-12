from sqlalchemy import Column, Integer, String, Float

from .base import Base

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    password = Column(String(256))

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return '<User %d: %r>' % (self.id, self.username)