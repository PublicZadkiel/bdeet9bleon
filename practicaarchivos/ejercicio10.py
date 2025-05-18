import string

def calcular_costo_telegrafo(mensaje):
    costo_letra_normal = 10
    costo_caracter_especial = 30
    costo_digito = 20

    letras_castellano_especiales = "ñáéíóúÑÁÉÍÓÚüÜ"
    letras_normales = string.ascii_letters

    costo_total = 0

    print(f"\nEjercicio 10 - Calculando costo del mensaje: \"{mensaje}\"")

    for caracter in mensaje:
        if caracter.isspace():
            pass
        elif caracter.isdigit():
            costo_total += costo_digito
        elif caracter in letras_castellano_especiales:
            costo_total += costo_caracter_especial
        elif caracter in letras_normales:
             costo_total += costo_letra_normal
        else:
            costo_total += costo_caracter_especial

    return costo_total

