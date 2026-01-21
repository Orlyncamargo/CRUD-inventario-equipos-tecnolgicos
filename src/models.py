from sqlalchemy import Column, Integer, String, Float, Date
from src.database import Base

class Dispositivo(Base):
    __tablename__ = "dispositivos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    tipo = Column(String(50))
    marca = Column(String(50))
    modelo = Column(String(50))
    numero_serie = Column(String(50))
    fecha_adquisicion = Column(Date)
    estado = Column(String(30))
    precio = Column(Float)
    ubicacion = Column(String(100))
