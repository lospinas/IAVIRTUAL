#### CADENAS DE CARACTERES Y METODOS

#CONVERTIR A MAYUSCULAS
cadena = input("Ingrese un texto para que juguemos: ")
cadena_mayuscula = cadena.capitalize(cadena)
print(cadena_mayuscula)

#CONTAR CARACTERES
caracter = input("Ingresa el caracter que quieres contar: ")
print("La cantidad de veces que se repite el caracter ", caracter "es", cadena.count(caracter))

#CONTAR PALABRAS
palabra = input("ingrese la palabra a buscar: " )
cuenta_palabras=palabra.count(cadena)
print("La cantidad de veces que se repite el la palabra", palabra "es", cuenta_palabras

#EJERCICIO BUSCAR PALABRA Y REEMPLAZARLA
buscar_palabra = input("Ingresa la palabra que quieres buscar: ")
palabra_a_reemplazar = input("Por cual palabra quieres reemplazarla: ")
texto_nuevo = Texto.replace(buscar_palabra, palabra_a_reemplazar)
print(f"Texto modificado: {texto_nuevo}")

#PEDIR TEXTO, SI ES NUMERICO mostrar VERDADERO, sino, FALSO

