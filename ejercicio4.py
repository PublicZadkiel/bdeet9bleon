import os
import re

def renombrar_archivos_con_prefijo(carpeta):
    print(f"\nEjercicio 4 - Renombrando archivos en: {carpeta}")
    if not os.path.isdir(carpeta):
        print(f"Error: La carpeta '{carpeta}' no existe.")
        return

    archivos = [f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))]

    if not archivos:
        print("No se encontraron archivos para renombrar en esta carpeta.")
        return

    archivos.sort()

    for i, nombre_antiguo in enumerate(archivos):
        prefijo = i + 1
        nombre_nuevo = f"{prefijo}_{nombre_antiguo}"

        ruta_antigua = os.path.join(carpeta, nombre_antiguo)
        ruta_nueva = os.path.join(carpeta, nombre_nuevo)

        try:
            if re.match(r'^\d+_', nombre_antiguo):
                 print(f"Saltando '{nombre_antiguo}': Ya parece tener un prefijo numérico.")
                 continue

            os.rename(ruta_antigua, ruta_nueva)
            print(f"Renombrado: {nombre_antiguo} -> {nombre_nuevo}")
        except OSError as e:
            print(f"Error al renombrar {nombre_antiguo}: {e}")

    print("Proceso de renombrado completado.")

