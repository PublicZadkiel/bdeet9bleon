def leer_y_mostrar_lineas(nombre_archivo="texto.txt"):
    print(f"\nEjercicio 6 - Leyendo y mostrando líneas de: {nombre_archivo}")
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            print("--- Contenido del archivo ---")
            for linea in archivo:
                print(linea, end='')
            print("\n--- Fin del contenido ---")
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

