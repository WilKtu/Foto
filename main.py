import json

def cargar_datos():
    with open("datos.json", "r") as archivo:
        datos = json.load(archivo)
    return datos

def guardar_datos(datos):
    with open("datos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)
        
def separador():
    print("-" * 30)

def menu():
    print("1. Agregar servicio fotográfico")
    print("2. Editar servicio fotográfico")
    print("3. Eliminar servicio fotográfico")
    print("4. Salir")