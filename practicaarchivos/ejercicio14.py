def encontrar_mayor(lista_numeros):
    print(f"\nEjercicio 14 - Encontrando el mayor en: {lista_numeros}")
    if not lista_numeros:
        print("La lista está vacía.")
        return None

    mayor = lista_numeros[0]
    for numero in lista_numeros:
        if numero > mayor:
            mayor = numero
    return mayor

