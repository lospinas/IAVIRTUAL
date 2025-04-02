def agregar_estudiante(estudiantes):
    """Agrega un nuevo estudiante a la lista."""
    nombre = input("Ingrese el nombre del estudiante: ")
    try:
        edad = int(input("Ingrese la edad del estudiante: "))
    except ValueError:
        print("La edad debe ser un número entero.")
        return
    calificaciones_str = input("Ingrese las calificaciones del estudiante separadas por comas (ej: 80,90,75): ")
    try:
        calificaciones = [float(calif.strip()) for calif in calificaciones_str.split(',')]
    except ValueError:
        print("Las calificaciones deben ser números válidos separados por comas.")
        return
    estudiantes.append({"nombre": nombre, "edad": edad, "calificaciones": calificaciones})
    print(f"Estudiante {nombre} agregado exitosamente.")

def calcular_promedio(estudiante):
    """Calcula el promedio de calificaciones de un estudiante."""
    if not estudiante["calificaciones"]:
        return 0
    return sum(estudiante["calificaciones"]) / len(estudiante["calificaciones"])

def mostrar_promedios_mayores(estudiantes, promedio_minimo):
    """Muestra los estudiantes con un promedio de calificaciones mayor al valor dado."""
    estudiantes_aprobados = []
    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante)
        if promedio > promedio_minimo:
            estudiantes_aprobados.append((estudiante["nombre"], promedio))

    if estudiantes_aprobados:
        print(f"\nEstudiantes con promedio mayor a {promedio_minimo}:")
        for nombre, promedio in estudiantes_aprobados:
            print(f"- {nombre}: {promedio:.2f}")
    else:
        print(f"\nNo hay estudiantes con promedio mayor a {promedio_minimo}.")

def buscar_estudiante(estudiantes, nombre_buscar):
    """Busca estudiantes por nombre."""
    resultados = [estudiante for estudiante in estudiantes if nombre_buscar.lower() in estudiante["nombre"].lower()]
    if resultados:
        print(f"\nResultados de la búsqueda para '{nombre_buscar}':")
        for estudiante in resultados:
            promedio = calcular_promedio(estudiante)
            print(f"- Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Promedio: {promedio:.2f}")
    else:
        print(f"\nNo se encontraron estudiantes con el nombre '{nombre_buscar}'.")

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n--- Menú ---")
    print("1. Agregar nuevo estudiante")
    print("2. Mostrar promedio de todos los estudiantes")
    print("3. Mostrar estudiantes con promedio mayor a un valor")
    print("4. Buscar estudiante por nombre")
    print("5. Salir")
    print("----------------")

def main():
    """Función principal del programa."""
    estudiantes = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_estudiante(estudiantes)
        elif opcion == '2':
            if estudiantes:
                print("\nPromedios de todos los estudiantes:")
                for estudiante in estudiantes:
                    promedio = calcular_promedio(estudiante)
                    print(f"- {estudiante['nombre']}: {promedio:.2f}")
            else:
                print("No hay estudiantes registrados.")
        elif opcion == '3':
            if estudiantes:
                try:
                    promedio_minimo = float(input("Ingrese el promedio mínimo: "))
                    mostrar_promedios_mayores(estudiantes, promedio_minimo)
                except ValueError:
                    print("El promedio mínimo debe ser un número.")
            else:
                print("No hay estudiantes registrados.")
        elif opcion == '4':
            if estudiantes:
                nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
                buscar_estudiante(estudiantes, nombre_buscar)
            else:
                print("No hay estudiantes registrados.")
        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()

