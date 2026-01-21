#Autor Orlin Camargo 
#Fecha modificación: 19/01/2025

from src.database import engine
from src.models import Base   # ← ESTO ES LO QUE FALTABA

# CREA LAS TABLAS
Base.metadata.create_all(bind=engine)

from src.crud import (
    listar_dispositivos,
    buscarDispositivo,
    agregarDispositivo,
    actualizarDispositivo,
    eliminarDispositivo,
    generarInforme
)

#creamos la función con el menú principal del CRUD
def menuPrincipal():
    print("\n-------Selecciona una opción-------")
    print("1. Listar los dispositivos")
    print("2. Buscar dispositivos")
    print("3. Agregar nuevo dispositivo")
    print("4. Actualizar información de dispositivo")
    print("5. Eliminar dispositivo")
    print("6. Generar informe")
    print("Salir")
    print("----------------------------")


#bucle  del menú principal del CRUD
while True:
    menuPrincipal()

    #manejo de excepciones en caso de que se ingrese un valor no esperado
    try:
        opcion = int(input("Selecciona una opción del menú: "))
    except ValueError:
        print("Debes ingresar un número válido")
        continue

    match opcion:
        case 1: 
            listar_dispositivos()
        case 2:
            buscarDispositivo()
        case 3: 
            agregarDispositivo()
        case 4:
            actualizarDispositivo()
        case 5:
            eliminarDispositivo()
        case 6:
            generarInforme()
        case 7:
            print("Saliendo del programa")
            break
        case _:
            print("Opción incorrecta")
