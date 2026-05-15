from fastapi import FastAPI

from database import Base, engine
from routes.task_routes import router as task_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(task_router)