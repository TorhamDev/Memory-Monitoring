from sqlalchemy import Column, Date, Float, Integer

from .database import Base


class Memory(Base):
    __tablename__ = "memory"

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    used = Column(Float)
    free = Column(Float)
    total = Column(Float)
