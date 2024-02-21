from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, sessionmaker

from .controller import StatisticsController
from .db.database import get_db
from .schema import Statistics

router = APIRouter()


@router.get("/", response_model=Statistics)
def get_mem_statistics(rows: int, db_session: sessionmaker[Session] = Depends(get_db)):
    result = StatisticsController(db_session).get(rows)
    return result
