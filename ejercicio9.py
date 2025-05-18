def invertir_lineas_archivo(archivo_entrada, archivo_salida):
    print(f"\nEjercicio 9 - Invirtiendo líneas de '{archivo_entrada}' a '{archivo_salida}'")
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as infile, \
             open(archivo_salida, 'w', encoding='utf-8') as outfile:

            for linea in infile:
                linea_invertida = linea.rstrip('\n')[::-1] + '\n'
                outfile.write(linea_invertida)

        print("Proceso completado. Las líneas invertidas se guardaron en", archivo_salida)

    except FileNotFoundError:
        print(f"Error: El archivo de entrada '{archivo_entrada}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error durante el proceso: {e}")

