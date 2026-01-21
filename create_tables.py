from src.database import engine
from src.models import Base

print("Creando tablas...")
Base.metadata.create_all(bind=engine)
print("Tablas creadas correctamente")
