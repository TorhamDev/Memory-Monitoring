from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .controller import StatisticsController
from .db.database import GetDB
from .schema import Statistics

router = APIRouter()


@router.get("/", response_model=Statistics)
def get_mem_statistics(rows: int, db_session: Session = Depends(GetDB)):
    result = StatisticsController(db_session).get(rows)
    return result
