import json

def cargar_datos():
    with open("datos.json", "r") as archivo:
        datos = json.load(archivo)
    return datos

def guardar_datos(datos):
    with open("datos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

def agregar_servicio(datos):
    nombre = input("Ingrese el nombre del servicio fotográfico: ")
    precio = float(input("Ingrese el precio del servicio fotográfico: "))
    descripcion = input("Ingrese la descripción del servicio fotográfico: ")
    
    nuevo_servicio = {
        "nombre": nombre,
        "precio": precio,
        "descripcion": descripcion
    }
    
    datos.append(nuevo_servicio)
    print("Servicio fotográfico agregado exitosamente.")
    
def editar_servicio(datos):
    nombre = input("Ingrese el nombre del servicio fotográfico a editar: ")
    for servicio in datos:
        if servicio["nombre"] == nombre:
            nuevo_nombre = input("Ingrese el nuevo nombre del servicio fotográfico: ")
            nuevo_precio = float(input("Ingrese el nuevo precio del servicio fotográfico: "))
            nueva_descripcion = input("Ingrese la nueva descripción del servicio fotográfico: ")
            
            servicio["nombre"] = nuevo_nombre
            servicio["precio"] = nuevo_precio
            servicio["descripcion"] = nueva_descripcion
            
            print("Servicio fotográfico editado exitosamente.")
            return
    print("Servicio fotográfico no encontrado.")    
        
def eliminar_servicio(datos):
    nombre = input("Ingrese el nombre del servicio fotográfico a eliminar: ")
    for servicio in datos:
        if servicio["nombre"] == nombre:
            datos.remove(servicio)
            print("Servicio fotográfico eliminado exitosamente.")
            return
    print("Servicio fotográfico no encontrado.")
    

def separador():
    print("-" * 30)

def menu():
    print("1. Agregar servicio fotográfico")
    print("2. Editar servicio fotográfico")
    print("3. Eliminar servicio fotográfico")
    print("4. Salir")