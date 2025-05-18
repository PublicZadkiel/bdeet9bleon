def analizar_archivo(nombre_archivo):
    print(f"\nEjercicio 8 - Analizando archivo: {nombre_archivo}")
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()

            num_caracteres = len(contenido)

            num_lineas = len(contenido.splitlines())

            palabras = contenido.split()
            num_palabras = len(palabras)

            print(f"Análisis de '{nombre_archivo}':")
            print(f"  Líneas: {num_lineas}")
            print(f"  Palabras: {num_palabras}")
            print(f"  Caracteres: {num_caracteres}")

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al analizar el archivo: {e}")

