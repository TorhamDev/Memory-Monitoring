from fastapi import FastAPI

from src.router import router as mem_router

app = FastAPI()

app.include_router(mem_router, prefix="/mem")
