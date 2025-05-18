import re

mensaje_ejemplo = "Hola 123, ¿cómo estás? Esto es una prueba con ñáéíóú y símbolos: !@#$%"

patron = r'\S+'

coincidencias = re.findall(patron, mensaje_ejemplo)

print("Ejercicio 1 - Coincidencias encontradas (no espacios):")
print(coincidencias)

patron_palabras = r'\b\w+\b'
coincidencias_palabras = re.findall(patron_palabras, mensaje_ejemplo)
print("\nEjercicio 1 - Coincidencias encontradas (palabras):")
print(coincidencias_palabras)

patron_digitos = r'\d+'
coincidencias_digitos = re.findall(patron_digitos, mensaje_ejemplo)
print("\nEjercicio 1 - Coincidencias encontradas (dígitos):")
print(coincidencias_digitos)