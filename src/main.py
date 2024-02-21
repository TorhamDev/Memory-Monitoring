from fastapi import FastAPI

from src.exporter.collectors import collect_memory_metrics
from src.router import router as mem_router
from src.utils.constants import TASK_REPEAT_TIME
from src.utils.repeater import repeat_every

from .db.database import GetDB
from .db.models import Memory

app = FastAPI()


@app.on_event("startup")
@repeat_every(seconds=TASK_REPEAT_TIME)
async def remove_expired_tokens_task() -> None:
    mem_info = collect_memory_metrics()
    with GetDB() as db:
        memory = Memory(
            date=mem_info.date,
            used=mem_info.used,
            free=mem_info.free,
            total=mem_info.total,
        )

        db.add(memory)
        db.commit()


app.include_router(mem_router, prefix="/mem")
