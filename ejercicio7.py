def guardar_nombre_en_archivo(nombre_archivo="nombres.txt"):
    print(f"\nEjercicio 7 - Guardando nombre en: {nombre_archivo}")
    nombre = input("Por favor, introduce tu nombre: ")

    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(nombre)
            print(f"Nombre '{nombre}' guardado exitosamente en '{nombre_archivo}'.")
    except Exception as e:
        print(f"Ocurrió un error al escribir en el archivo: {e}")

