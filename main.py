import json

def cargar_datos():
    with open("datos.json", "r") as archivo:
        datos = json.load(archivo)
    return datos

def guardar_datos():
    with open("datos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)
        
def agregar_servicio():
    nombre = input("Ingrese el nombre del servicio fotográfico: ")
    precio = float(input("Ingrese el precio del servicio fotográfico: "))
    descripcion = input("Ingrese la descripción del servicio fotográfico: ")
    
    nuevo_servicio = {
        "nombre": nombre,
        "precio": precio,
        "descripcion": descripcion
    }
    
    guardar_datos.append(nuevo_servicio)
    print("Servicio fotográfico agregado exitosamente.")   
        
def separador():
    print("-" * 30)

def menu():
    print("1. Agregar servicio fotográfico")
    print("2. Editar servicio fotográfico")
    print("3. Eliminar servicio fotográfico")
    print("4. Salir")