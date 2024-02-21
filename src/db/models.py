from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import DateTime, Float, Integer

from .database import Base


class Memory(Base):
    __tablename__ = "memory"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    used = Column(Float)
    free = Column(Float)
    total = Column(Float)
