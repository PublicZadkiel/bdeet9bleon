import os

def eliminar_archivos_txt(carpeta):
    print(f"\nEjercicio 2 - Eliminando archivos .txt en: {carpeta}")
    if not os.path.isdir(carpeta):
        print(f"Error: La carpeta '{carpeta}' no existe.")
        return

    archivos_txt = [f for f in os.listdir(carpeta) if f.endswith('.txt') and os.path.isfile(os.path.join(carpeta, f))]

    if not archivos_txt:
        print("No se encontraron archivos .txt en esta carpeta.")
        return

    print("Se encontraron los siguientes archivos .txt:")
    for archivo in archivos_txt:
        print(f"- {archivo}")

    confirmacion = input("¿Estás seguro de que quieres eliminar estos archivos? (s/n): ")

    if confirmacion.lower() == 's':
        for archivo in archivos_txt:
            ruta_completa = os.path.join(carpeta, archivo)
            try:
                os.remove(ruta_completa)
                print(f"Eliminado: {archivo}")
            except OSError as e:
                print(f"Error al eliminar {archivo}: {e}")
        print("Proceso de eliminación completado.")
    else:
        print("Eliminación cancelada.")
