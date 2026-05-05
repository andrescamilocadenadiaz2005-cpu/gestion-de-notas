from archivo import cargar_datos
def generar_reporte():
    """Genera un reporte en consola."""
    estudiantes = cargar_datos()
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    print("\n" + "=" * 70)
    print("REPORTE GENERAL DE ESTUDIANTES")
    print("=" * 70)

    encabezado = (
        f"{'ID':<15}"
        f"{'NOMBRE':<20}"
        f"{'PROMEDIO':<15}"
        f"{'ESTADO':<15}"
    )

    print(encabezado)
    print("-" * 70)

    for estudiante in estudiantes:

        identificacion = estudiante.get("identificacion", "")
        nombre = estudiante.get("nombre", "")
        promedio = estudiante.get("promedio", 0)
        estado = estudiante.get("estado", "")

        fila = (
            f"{identificacion:<15}"
            f"{nombre:<20}"
            f"{promedio:<15.2f}"
            f"{estado:<15}"
        )

        print(fila)

    print("=" * 70)