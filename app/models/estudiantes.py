from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Estudiante(Base):
    """Modelo para la tabla de estudiantes."""
    __tablename__ = "estudiantes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    codigo_estudiantil = Column(String(20), nullable=False, unique=True)
    dni = Column(String(15), unique=True)
    facultad = Column(String(100), nullable=False)
    carrera = Column(String(100), nullable=False)