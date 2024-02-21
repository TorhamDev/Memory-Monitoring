from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from .database import get_db

router = APIRouter()


@router.get("/")
def get_mem_statistics(rows: int, db_session: Session = Depends(get_db)):
    return {"H1": "h2"}
