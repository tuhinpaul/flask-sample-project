from sqlalchemy import Column, Integer, String, Float

from .base import Base

class Event(Base):
    __tablename__ = 'Event'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    latitude = Column(Float)
    longitude = Column(Float)

    def __init__(self, name=None, latitude=None, longitude=None):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return '<Event %d: %r>' % (self.id, self.name)

    def as_dict(self):
        return {'name': self.name, 'latitude': self.latitude, 'longitude': self.longitude}

