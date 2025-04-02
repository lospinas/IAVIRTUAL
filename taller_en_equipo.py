"""
Carlos Fadul: Ejercicio: Sistema de Inventario de una Tienda
Objetivo: Crear un programa que permita gestionar el inventario de una tienda, donde los usuarios puedan:

Agregar productos
Buscar productos
Mostrar todos los productos
Salir del programa

Requisitos:
Diccionario para almacenar cada producto con su nombre, precio y cantidad.
Ejemplo: {"nombre": "Manzana", "precio": 0.5, "cantidad": 10}
Lista para guardar todos los productos del inventario.
Menú interactivo con while y condicionales (if-elif-else).
"""

activo = True
inventario = []

while activo:
    print("1. Agregar electrodoméstico")
    print("2. Buscar electrodoméstico")
    print("3. Mostrar todos los electrodomésticos")
    print("4. Salir")
    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
        nombre = input("Ingrese el nombre del electrodoméstico: ")
        precio = float(input("Ingrese el precio del electrodoméstico: "))
        cantidad = int(input("Ingrese la cantidad del electrodoméstico: "))
        
        electrodomestico = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        inventario.append(electrodomestico)
        print("Electrodoméstico AGREGADO")
    elif opcion == 2:
        nombre_buscar = input("Ingrese el nombre del electrodoméstico a buscar: ")
        encontrado = False
        
        for electrodomestico in inventario:
            if electrodomestico["nombre"].lower() == nombre_buscar.lower():
                print(f"Electrodoméstico encontrado: {electrodomestico}")
                encontrado = True
                break
                
        if not encontrado:
            print(f"Electrodoméstico '{nombre_buscar}' no encontrado.")
    elif opcion == 3:
        if inventario:
            print("Lista de electrodomésticos:")
            for electrodomestico in inventario:
                print(f"- {electrodomestico['nombre']}: ${electrodomestico['precio']}, Cantidad: {electrodomestico['cantidad']}")
        else:
            print("No hay electrodomésticos en el inventario.")
            
    elif opcion == 4:
        activo = False
        
    else:4
    
    print("Programa finalizado")
    