import os

def contar_archivos_en_carpeta(carpeta):
    print(f"\nEjercicio 3 - Contando archivos en: {carpeta}")
    if not os.path.isdir(carpeta):
        print(f"Error: La carpeta '{carpeta}' no existe.")
        return 0

    contador = 0
    for nombre in os.listdir(carpeta):
        ruta_completa = os.path.join(carpeta, nombre)
        if os.path.isfile(ruta_completa):
            contador += 1
    return contador

