import json

ARCHIVO = "estudiantes.json"

def guardar_datos(estudiantes):

    archivo = open(ARCHIVO, "w")

    json.dump(estudiantes, archivo, indent=4)

    archivo.close()

    print("Datos guardados")


def cargar_datos():

    try:

        archivo = open(ARCHIVO, "r")

        estudiantes = json.load(archivo)

        archivo.close()

        return estudiantes

    except:

        return []
