import sqlalchemy as sa
from sqlalchemy.orm import Session, sessionmaker

from .db.models import Memory
from .schema import MemoryStatistics, Statistics


class StatisticsController:
    def __init__(self, db_session: sessionmaker[Session]) -> None:
        self.db_session = db_session

    def get(self, rows: int) -> Statistics:
        query = sa.select(Memory).order_by(Memory.id.desc()).limit(rows)

        with self.db_session.begin() as db:
            data = db.scalars(query).all()
            memory_metrics = [
                MemoryStatistics(
                    date=obj.date,
                    used=obj.used,
                    free=obj.free,
                    total=obj.total,
                )
                for obj in data
            ]

        statistics = Statistics(rows=rows, memory=memory_metrics)
        return statistics
