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
        
def separador():
    print("-" * 30)

def menu():
    print("1. Agregar servicio fotográfico")
    print("2. Editar servicio fotográfico")
    print("3. Eliminar servicio fotográfico")
    print("4. Salir")
    
while True:
    datos = cargar_datos()
    menu()
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_servicio(datos)
        guardar_datos(datos)
    elif opcion == "2":
        print("Funcionalidad de edición no implementada aún.")
    elif opcion == "3":
        print("Funcionalidad de eliminación no implementada aún.")
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, intente nuevamente.")
    
    separador()