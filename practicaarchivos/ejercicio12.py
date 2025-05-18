def contar_mayores_que_diez(lista_numeros):
    print(f"\nEjercicio 12 - Contando mayores que 10 en: {lista_numeros}")
    contador = 0
    for numero in lista_numeros:
        if numero > 10:
            contador += 1
    return contador

