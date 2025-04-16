from pydantic import BaseModel

class EstudianteCreate(BaseModel):
    nombre: str
    apellido: str
    codigo_estudiantil: str
    dni: str
    facultad: str
    carrera: str

class EstudianteOut(EstudianteCreate):
    id: int

    class Config:
        orm_mode = True  # Permite que FastAPI lea objetos SQLAlchemy como diccionarios