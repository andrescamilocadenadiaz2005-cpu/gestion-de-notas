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

def ingresar_notas(identificacion):
    estudiantes = cargar_datos()

    for estudiante in estudiantes:
        if estudiante["identificacion"] == identificacion:

            cantidad = int(input("¿Cuántas notas desea ingresar?: "))
            notas = []

            for i in range(cantidad):
                while True:
                    nota = float(input(f"Ingrese la nota {i+1}: "))

                    if 0 <= nota <= 5:
                        notas.append(nota)
                        break
                    else:
                        print("La nota debe estar entre 0 y 5.")

            estudiante["notas"] = notas
            guardar_datos(estudiantes)

            print("Notas guardadas correctamente.")
            return

    print("Estudiante no encontrado.")

def calcular_promedio(notas):
    if len(notas) == 0:
        return 0

    return sum(notas) / len(notas)


def determinar_estado(promedio):
    if promedio >= 3.0:
        return "Aprobado"
    else:
        return "Reprobado"
    
def obtener_estudiante(identificacion):
    estudiantes = cargar_datos()

    for estudiante in estudiantes:
        if estudiante["identificacion"] == identificacion:
            return estudiante

    return None


def mostrar_promedio_estudiante(identificacion):
    estudiante = obtener_estudiante(identificacion)

    if estudiante:
        promedio = calcular_promedio(estudiante["notas"])
        estado = determinar_estado(promedio)

        print(f"\nNombre: {estudiante['nombre']}")
        print(f"Promedio: {promedio}")
        print(f"Estado: {estado}")
    else:
        print("Estudiante no encontrado.")


def mostrar_promedio_todos():
    estudiantes = cargar_datos()

    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante["notas"])
        estado = determinar_estado(promedio)

        print(f"\nID: {estudiante['identificacion']}")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Promedio: {promedio}")
        print(f"Estado: {estado}")
