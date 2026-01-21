#Importamos las librerias a utilizar
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#conexión a la base de datos
DATABASE_URL = "mysql+mysqlconnector://root@localhost/inventario_tecnologico"

#Trabajamos con SQLAlchemy siendo el objeto que maneja la conexión a la base de datos
engine = create_engine(
    DATABASE_URL,
    echo=False,        
    future=True
)

#Nos permite interactuar con la base de datos
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

#Creamos la clase base para el proyecto
Base = declarative_base()

