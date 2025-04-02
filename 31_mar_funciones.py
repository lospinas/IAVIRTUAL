"""
def suma():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    resultado = a + b
    print(f"La suma de {a} y {b} es: {resultado}")
   
suma()

def suma(a, b):
    resultado = a + b
    print(resultado)

suma(5, 10)

def suma(a, b):
    resultado = a + b
    return resultado

n = int(input("Ingrese el primer número: "))
m = int(input("Ingrese el segundo número: "))

print("el resultado es: ",suma(n, m))

"""
"""
ciclo_while true:

opc=0
print("1. SUMAR")
print("2. RESTAR)")
print("3. MULTIPLICAR")
print("4. DIVIDIR)")
print("5. SALIR" )

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

def suma():
    resultado = a + b
    print(f"La suma de {a} y {b} es: {resultado}")
suma()
def resta():
    resultado = a - b
    print(resultado)
multi()

def multi():
    resultado = a * b
    print(resultado)
multi()

def divi():
    resultado = a / b
    print(resultado)
divi()"
"""""
import os

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir por cero."
    return num1 / num2

def borrar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("--- MI CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def obtener_numeros():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("Entrada inválida. Por favor, ingrese números.")

def main():
    while True:
        borrar_pantalla()
        opcion = mostrar_menu()

        if opcion == '1':
            num1, num2 = obtener_numeros()
            resultado = sumar(num1, num2)
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == '2':
            num1, num2 = obtener_numeros()
            resultado = restar(num1, num2)
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == '3':
            num1, num2 = obtener_numeros()
            resultado = multiplicar(num1, num2)
            print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == '4':
            num1, num2 = obtener_numeros()
            resultado = dividir(num1, num2)
            print(f"El resultado de la división es: {resultado}")
        elif opcion == '5':
            print("¡Gracias por usar la calculadora!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida del menú.")

        input("Presione Enter para volver al menú principal...")

if __name__ == "__main__":
    main()
