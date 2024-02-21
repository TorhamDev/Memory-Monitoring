import os

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from src.db.database import Base, GetDB
from src.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///" + os.getcwd() + "/test_db.sqlite3"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[GetDB] = override_get_db

client = TestClient(app)


def test_create_user():
    response = client.get("/mem/?rows=5")
    print(response.json())

    assert 1 == 2
