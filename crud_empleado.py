import os
import json

def limpiar_pantalla():
    os.system("cls")

def cargar_json(url_archivo):
    with open(url_archivo, 'r') as archivo:
        return json.load(archivo)

limpiar_pantalla()

def menu_general():
    print("\t1- Crear empleado")
    print("\t2- Actualizar empleado")
    print("\t3- Eliminar empleado")
    print("\t4- Listar empleados")
    print("\t5- Salir")

def seleccionar_opcion(max_option):
    while True:
        opcion = 0
        try:
            opcion = int(input("Selecciona una opción: "))
            if opcion < 1 or opcion > max_option:
                print("La opción seleccionada no existe")
                input("Presiona Enter para continuar...")
            else:
                return opcion
        except:
            print("La opción ingresada debe ser un número")
            input("Presiona Enter para continuar...")
        limpiar_pantalla()


def iniciar_programa():
    while True:
        menu_general()
        opcion = seleccionar_opcion(5)

        if opcion == 1:
            print("Crear empleado")
        elif opcion == 2:
            print("Actualizar empleado")
        elif opcion == 3:
            print("Eliminar empleado")
        elif opcion == 4:
            print("Listar empleado")
        elif opcion == 5:
            return
        
        input("Presiona Enter para continuar...")

        
        empleados = cargar_json('empleados.json')
        print(empleados)

iniciar_programa()