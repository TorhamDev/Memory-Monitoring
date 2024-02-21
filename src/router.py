from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .database import get_db

router = APIRouter()


@router.get("/")
def get_mem_statistics(rows: int, db_session: AsyncSession = Depends(get_db)):
    return {"H1": "h2"}
