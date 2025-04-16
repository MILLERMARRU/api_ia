from fastapi import FastAPI
from app.routers import estudiante
from app.database.database import engine
from app.models.estudiantes import Base

app = FastAPI()

@app.get("/")
def read_root():
    return "PIPOL HAY Q PONERSE LAS PILAS DURACEL"

Base.metadata.create_all(bind=engine)

app.include_router(estudiante.router, prefix="/estudiantes", tags=["estudiantes"])
