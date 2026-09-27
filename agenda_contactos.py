"""
Programa: Agenda de Contactos
Nombre: Edinson Perez
Tema: Colecciones de datos - diccionarios
Descripcion: Este programa permite administrar una agenda de contactos
(nombre y numero de telefono) utilizando un diccionario de Python.
El usuario puede agregar, mostrar, buscar y eliminar contactos mediante
un menu interactivo por consola. Al iniciar, la agenda ya contiene
algunos contactos de ejemplo para que no arranque vacia.
"""

# Diccionario donde se guardan los contactos.
# La clave es el nombre del contacto y el valor es su numero de telefono.
contactos = {
    "Jorge Rivera": "0952456504",
    "Paula Rivera": "0906397666",
    "Paula Reyes": "0915135227",
    "Luis Torres": "0947967289",
    "Miguel Castro": "0996356737",
    "Daniela Vargas": "0937478280",
    "Ricardo Gomez": "0961510644",
    "Gabriela Sanchez": "0991463290",
    "Jorge Ortiz": "0960985704",
    "Luis Jimenez": "0958345577",
    "Luis Vega": "0950047584",
    "Diego Rivera": "0983477422",
    "Fernando Chavez": "0931158764",
    "Sofia Herrera": "0963101593",
    "Luis Castro": "0936056395"
}


def agregar_contacto():
    """Solicita un nombre y un numero, y los guarda en el diccionario."""
    nombre = input("Ingrese el nombre del contacto: ").strip()
    telefono = input("Ingrese el numero de telefono: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacio.\n")
        return

    if nombre in contactos:
        print(f"El contacto '{nombre}' ya existia. Se actualizo su numero.\n")
    else:
        print(f"Contacto '{nombre}' guardado correctamente.\n")

    contactos[nombre] = telefono


def mostrar_contactos():
    """Recorre el diccionario y muestra todos los contactos guardados."""
    if not contactos:
        print("No hay contactos registrados todavia.\n")
        return

    print("\n--- Lista de contactos ---")
    for nombre, telefono in contactos.items():
        print(f"Nombre: {nombre} | Telefono: {telefono}")
    print("---------------------------\n")


def buscar_contacto():
    """Busca un contacto por nombre y muestra su numero si existe."""
    nombre = input("Ingrese el nombre que desea buscar: ").strip()

    if nombre in contactos:
        print(f"{nombre} tiene el numero: {contactos[nombre]}\n")
    else:
        print(f"No se encontro ningun contacto con el nombre '{nombre}'.\n")


def eliminar_contacto():
    """Elimina un contacto del diccionario si existe."""
    nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()

    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto '{nombre}' eliminado correctamente.\n")
    else:
        print(f"No se encontro ningun contacto con el nombre '{nombre}'.\n")


def mostrar_menu():
    """Muestra las opciones disponibles del programa."""
    print("===== AGENDA DE CONTACTOS =====")
    print("1. Agregar contacto")
    print("2. Mostrar todos los contactos")
    print("3. Buscar un contacto")
    print("4. Eliminar un contacto")
    print("5. Salir")


def main():
    """Funcion principal que ejecuta el menu en un bucle."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion (1-5): ").strip()

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            print("Gracias por usar la agenda de contactos. Hasta pronto.")
            break
        else:
            print("Opcion no valida. Intente nuevamente.\n")


if __name__ == "__main__":
    main()