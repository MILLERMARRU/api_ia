from fastapi import APIRouter, Form , Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.service.estudiante import create_estudiante
from app.schemas.estudiante import EstudianteCreate
from app.service.estudiante import get_estudiantes

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/registrar")
def register_estudiante(
    nombre: str = Form(...),
    apellido: str = Form(...),
    codigo_estudiantil: str = Form(...),
    dni: str = Form(...),
    facultad: str = Form(...),
    carrera: str = Form(...),
    db: Session = Depends(get_db)
):
    estudiante_data = EstudianteCreate(
        nombre=nombre,
        apellido=apellido,
        codigo_estudiantil=codigo_estudiantil,
        dni=dni,
        facultad=facultad,
        carrera=carrera
    )
    return create_estudiante(db=db, estudiante=estudiante_data)

@router.get("/listar")
def listar_estudiantes(db:Session = Depends(get_db)):
    return get_estudiantes(db)