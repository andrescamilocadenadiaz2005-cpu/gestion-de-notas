from archivo import cargar_datos, guardar_datos

def registrar_estudiante(nombre, identificacion):
    estudiantes = cargar_datos()

    for estudiante in estudiantes:
        if estudiante["identificacion"] == identificacion:
            print("Ese estudiante ya está registrado.")
            return

    nuevo_estudiante = {
        "identificacion": identificacion,
        "nombre": nombre,
        "notas": [],
        "promedio": 0,
        "estado": "Sin calcular"
    }

    estudiantes.append(nuevo_estudiante)
    guardar_datos(estudiantes)
    
    print("Estudiante registrado correctamente.")

def ingresar_notas(estudiante):
    pass

def calcular_promedio(notas):
    pass

def determinar_estado(promedio):
    pass
