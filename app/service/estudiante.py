from sqlalchemy.orm import Session
from app.schemas.estudiante import EstudianteCreate

from app.models.estudiantes import Estudiante

def create_estudiante(db: Session, estudiante: EstudianteCreate):
    nuevo = Estudiante(**estudiante.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def get_estudiantes(db: Session) -> list[Estudiante]:
    return db.query(Estudiante).all()

