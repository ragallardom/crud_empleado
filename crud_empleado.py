import os
import json

def limpiar_pantalla():
    os.system("cls")

def cargar_json(url_archivo):
    with open(url_archivo, 'r') as archivo:
        return json.load(archivo)

limpiar_pantalla()
    
empleados = cargar_json('empleados.json')

print(empleados)