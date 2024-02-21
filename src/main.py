from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from src.exporter.collectors import collect_memory_metrics
from src.router import router as mem_router

from .database import get_db
from .models import Memory

app = FastAPI()


@app.on_event("startup")
@repeat_every(seconds=2)  # 1 min
async def remove_expired_tokens_task() -> None:
    mem_info = collect_memory_metrics()
    with get_db().begin() as db:
        memory = Memory(
            date=mem_info.date,
            used=mem_info.used,
            free=mem_info.free,
            total=mem_info.total,
        )

        db.add(memory)
        db.commit()


app.include_router(mem_router, prefix="/mem")
