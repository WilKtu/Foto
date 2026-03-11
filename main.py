from json import load, dump

archivo = "datos.json"

def cargar_datos():

    with open(archivo, "r") as file:
        datos = load(file)


    return datos

def guardar_datos(datos):
    with open(archivo, "w") as file:
        dump(datos, file, indent=4)

def agregar_servicio():
    nombre = input("Nombre del paquete: ").strip()
    precio = float(input("Precio del paquete: "))
    tipo = input("Tipo de evento: ").strip()
        
    nuevo_servicio = {
        "nombre": nombre,
        "precio": precio,
        "descripcion": tipo
    }
        
    datos = cargar_datos()
    datos.append(nuevo_servicio)
    guardar_datos(datos)
    print("Servicio fotográfico agregado exitosamente.")

def mostrar_servicios():
    datos = cargar_datos()
    if not datos:
        print("No hay servicios fotográficos disponibles.")
        return
    print("Servicios fotográficos disponibles:")
    for servicio in datos:
        print(f"Nombre: {servicio['nombre']}, Precio: {servicio['precio']}, Descripción: {servicio['descripcion']}")

def editar_servicio():
    datos = cargar_datos()
    mostrar_servicios()
    nombre = input("Ingrese el nombre del servicio fotográfico a editar: ").strip()
    for servicio in datos:
        if servicio["nombre"].lower() == nombre.lower():
            nuevo_nombre = input("Ingrese el nuevo nombre del servicio fotográfico: ").strip()


            print("Error: El precio debe ser un número válido.")
            return
        nueva_descripcion = input("Ingrese la nueva descripción del servicio fotográfico: ").strip()
            
        servicio["nombre"] = nuevo_nombre
        servicio["precio"] = nuevo_precio
        servicio["descripcion"] = nueva_descripcion
            
        guardar_datos(datos)
        print("Servicio fotográfico editado exitosamente.")
        return
    print("Servicio fotográfico no encontrado.")

def eliminar_servicio():
    mostrar_servicios()
    datos = cargar_datos()
    nombre = input("Ingrese el nombre del servicio fotográfico a eliminar: ").strip()
    for servicio in datos:
        if servicio["nombre"].lower() == nombre.lower():
            datos.remove(servicio)
            guardar_datos(datos)
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

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            agregar_servicio()
        elif opcion == "2":
            editar_servicio()
        elif opcion == "3":
            eliminar_servicio()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
        separador()

if __name__ == "__main__":
    main()