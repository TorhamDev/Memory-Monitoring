from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_mem_statistics():
    return {"H1": "h2"}
