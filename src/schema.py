from datetime import datetime

from pydantic import BaseModel


class MemoryStatistics(BaseModel):
    date: datetime
    used: float
    free: float
    total: float


class Statistics(BaseModel):
    rows: int
    memory: list[MemoryStatistics]
