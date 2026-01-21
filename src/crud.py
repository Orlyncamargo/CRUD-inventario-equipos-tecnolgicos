#Importando librerias a utilizar
from datetime import datetime
from src.database import SessionLocal
from src.models import Dispositivo
from src.database import SessionLocal
from src.models import Dispositivo
from sqlalchemy import func

#Funciones del menú
def listar_dispositivos():
    session = SessionLocal()
    try:
        dispositivos = session.query(Dispositivo).all()

        if not dispositivos:
            print("\nNo hay dispositivos registrados.\n")
            return

        print("\n--- LISTADO DE DISPOSITIVOS ---")
        for d in dispositivos:
            print(f"""
ID: {d.id}
Nombre: {d.nombre}
Tipo: {d.tipo}
Marca: {d.marca}
Modelo: {d.modelo}
Serie: {d.numero_serie}
Fecha adquisición: {d.fecha_adquisicion}
Estado: {d.estado}
Precio: {d.precio}
Ubicación: {d.ubicacion}
------------------------------
""")
    except Exception as e:
        print("Error al listar dispositivos:", e)
    finally:
        session.close()

def buscarDispositivo():
    print("\n--- Buscar dispositivos ---")
    print("1. Buscar por marca")
    print("2. Buscar por tipo")
    print("3. Buscar por estado")

    criterio = input("Selecciona un criterio de búsqueda: ")

    if criterio == "1":
        valor = input("Ingrese la marca a buscar: ")
        filtro = Dispositivo.marca
    elif criterio == "2":
        valor = input("Ingrese el tipo de dispositivo a buscar: ")
        filtro = Dispositivo.tipo
    elif criterio == "3":
        valor = input("Ingrese el estado a buscar: ")
        filtro = Dispositivo.estado
    else:
        print("Criterio no válido")
        return

    session = SessionLocal()

    try:
        resultados = session.query(Dispositivo)\
            .filter(filtro.ilike(valor))\
            .all()

        if not resultados:
            print("\nNo se encontraron dispositivos con ese criterio.\n")
            return

        print("\n--- Resultados de la búsqueda ---")
        for d in resultados:
            print(f"""
ID: {d.id}
Nombre: {d.nombre}
Marca: {d.marca}
Tipo: {d.tipo}
Estado: {d.estado}
Ubicación: {d.ubicacion}
------------------------------
""")
    finally:
        session.close()

def agregarDispositivo():
    print("\n--- Agregar nuevo dispositivo ---")

    nombre = input("Nombre del dispositivo: ")
    tipo = input("Tipo de dispositivo (Laptop, Smartphone, Tablet, etc.): ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    numero_serie = input("Número de serie: ")
    fecha_adquisicion_str = input("Fecha de adquisición (YYYY-MM-DD): ")
    estado = input("Estado (Nuevo, Usado, En reparación): ")

    try:
        precio = float(input("Precio: "))
    except ValueError:
        print("El precio debe ser un número")
        return

    ubicacion = input("Ubicación: ")

    # Convertir fecha
    try:
        fecha_adquisicion = datetime.strptime(
            fecha_adquisicion_str, "%Y-%m-%d"
        ).date()
    except ValueError:
        print("Formato de fecha inválido")
        return

    # Crear sesión
    db = SessionLocal()

    try:
        dispositivo = Dispositivo(
            nombre=nombre,
            tipo=tipo,
            marca=marca,
            modelo=modelo,
            numero_serie=numero_serie,
            fecha_adquisicion=fecha_adquisicion,
            estado=estado,
            precio=precio,
            ubicacion=ubicacion
        )

        db.add(dispositivo)
        db.commit()
        db.refresh(dispositivo)

        print(f"Dispositivo agregado con ID {dispositivo.id}")

    except Exception as e:
        db.rollback()
        print("Error al guardar el dispositivo")
        print(e)

    finally:
        db.close()

def actualizarDispositivo():
    print("\n--- Actualizar dispositivo ---")

    try:
        id_buscar = int(input("Ingrese el ID del dispositivo a actualizar: "))
    except ValueError:
        print("El ID debe ser un número")
        return

    session = SessionLocal()

    try:
        dispositivo = session.query(Dispositivo).filter(Dispositivo.id == id_buscar).first()

        if not dispositivo:
            print("No se encontró un dispositivo con ese ID")
            return

        print("\n--- Datos actuales del dispositivo ---")
        print(f"Nombre: {dispositivo.nombre}")
        print(f"Tipo: {dispositivo.tipo}")
        print(f"Marca: {dispositivo.marca}")
        print(f"Modelo: {dispositivo.modelo}")
        print(f"Número de serie: {dispositivo.numero_serie}")
        print(f"Fecha de adquisición: {dispositivo.fecha_adquisicion}")
        print(f"Estado: {dispositivo.estado}")
        print(f"Precio: {dispositivo.precio}")
        print(f"Ubicación: {dispositivo.ubicacion}")

        print("\nPresione ENTER para mantener el valor actual")

        nombre = input("Nuevo nombre: ")
        tipo = input("Nuevo tipo: ")
        marca = input("Nueva marca: ")
        modelo = input("Nuevo modelo: ")
        numero_serie = input("Nuevo número de serie: ")
        fecha_adquisicion = input("Nueva fecha (YYYY-MM-DD): ")
        estado = input("Nuevo estado: ")
        precio = input("Nuevo precio: ")
        ubicacion = input("Nueva ubicación: ")

        if nombre:
            dispositivo.nombre = nombre
        if tipo:
            dispositivo.tipo = tipo
        if marca:
            dispositivo.marca = marca
        if modelo:
            dispositivo.modelo = modelo
        if numero_serie:
            dispositivo.numero_serie = numero_serie
        if fecha_adquisicion:
            try:
                dispositivo.fecha_adquisicion = datetime.strptime(
                    fecha_adquisicion, "%Y-%m-%d"
                ).date()
            except ValueError:
                print("Formato de fecha inválido")
        if estado:
            dispositivo.estado = estado
        if precio:
            try:
                dispositivo.precio = float(precio)
            except ValueError:
                print("Precio inválido, se mantiene el valor anterior")
        if ubicacion:
            dispositivo.ubicacion = ubicacion

        session.commit()
        print("Dispositivo actualizado correctamente")

    except Exception as e:
        session.rollback()
        print("Error al actualizar el dispositivo")
        print(e)

    finally:
        session.close()

def eliminarDispositivo():
    print("\n--- Eliminar dispositivo ---")

    try:
        id_eliminar = int(input("Ingrese el ID del dispositivo a eliminar: "))
    except ValueError:
        print("El ID debe ser un número")
        return

    session = SessionLocal()

    try:
        dispositivo = session.query(Dispositivo).filter(Dispositivo.id == id_eliminar).first()

        if not dispositivo:
            print("No se encontró un dispositivo con ese ID")
            return

        print("\nDispositivo encontrado:")
        print(f"ID: {dispositivo.id}")
        print(f"Nombre: {dispositivo.nombre}")
        print(f"Marca: {dispositivo.marca}")
        print(f"Modelo: {dispositivo.modelo}")
        print(f"Ubicación: {dispositivo.ubicacion}")

        confirmacion = input("¿Está seguro que desea eliminarlo? (s/n): ").lower()

        if confirmacion == "s":
            session.delete(dispositivo)
            session.commit()
            print("Dispositivo eliminado correctamente")
        else:
            print("Eliminación cancelada")

    except Exception as e:
        session.rollback()
        print("Error al eliminar el dispositivo")
        print(e)

    finally:
        session.close()

def generarInforme():
    session = SessionLocal()
    try:
        dispositivos = session.query(Dispositivo).all()

        if not dispositivos:
            print("\nNo hay dispositivos registrados.\n")
            return

        total_dispositivos = len(dispositivos)
        valor_total = sum(d.precio for d in dispositivos if d.precio is not None)

        print("\n--- RESUMEN DE DISPOSITIVOS ---")
        print(f"Total de dispositivos: {total_dispositivos}")
        print(f"Valor total de los dispositivos: ${valor_total:,.2f}")  # Formato con comas y 2 decimales
        print("------------------------------\n")

    except Exception as e:
        print("Error al calcular el resumen de dispositivos:", e)
    finally:
        session.close()

