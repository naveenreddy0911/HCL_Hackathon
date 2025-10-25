from fastapi import FastAPI
from backend.db import Base, engine
from backend.routes import router
from backend.models.user import User

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)