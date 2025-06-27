import os
import shutil

def copy_file_to_subfolders():
    # Define las rutas
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Directorio donde se encuentra el script .py
    pending_dir = os.path.join(current_dir, "Pendiente")  # Carpeta "Pendiente"

    # Busca el archivo "General" en el directorio actual
    source_file = None
    for file in os.listdir(current_dir):
        if file.startswith("RESPUESTA DEVOLUCION"):
            source_file = os.path.join(current_dir, file)
            break

    # Recorre todas las subcarpetas dentro de la carpeta "Pendiente"
    for subdir in os.listdir(pending_dir):
        subdir_path = os.path.join(pending_dir, subdir)
        if os.path.isdir(subdir_path):
            # Ruta de destino donde se copiará el archivo PDF
            destination_path = os.path.join(subdir_path, os.path.basename(source_file))
            try:
                shutil.copy2(source_file, destination_path)
                print(f"Archivo copiado a {destination_path}")
            except Exception as e:
                print(f"Error al copiar el archivo a {destination_path}: {e}")

if __name__ == "__main__":
    copy_file_to_subfolders()
