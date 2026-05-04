from reporte import generar_reporte
from backend import (registrar_estudiante, ingresar_notas, mostrar_promedio_estudiante, mostrar_promedio_todos)


def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE NOTAS ---")
    print("1. Registrar estudiante")
    print("2. Ingresar notas")
    print("3. Calcular promedio y estado")
    print("4. Generar reporte")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre: ")
            identificacion = input("Ingrese identificación: ")
            registrar_estudiante(nombre, identificacion)

        elif opcion == "2":
            identificacion = input("Ingrese identificación: ")
            ingresar_notas(identificacion)

        elif opcion == "3":
            tipo = input("¿Ver uno específico (1) o todos (2)?: ")

            if tipo == "1":
                identificacion = input("Ingrese identificación: ")
                mostrar_promedio_estudiante(identificacion)

            elif tipo == "2":
                mostrar_promedio_todos()

            else:
                print("Opción inválida.")

        elif opcion == "4":
            generar_reporte()

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == '__main__':
    main()