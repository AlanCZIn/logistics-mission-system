from fastapi import FastAPI
from app.core.database import engine, Base
from app.api.mission import router as mission_router

app = FastAPI()
app.include_router(mission_router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Mission System Running"}