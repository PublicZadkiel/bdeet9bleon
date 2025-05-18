def crear_lista_cuadrados(lista_numeros):
    print(f"\nEjercicio 13 - Creando lista de cuadrados para: {lista_numeros}")
    lista_cuadrados = []
    for numero in lista_numeros:
        lista_cuadrados.append(numero ** 2)
    return lista_cuadrados

