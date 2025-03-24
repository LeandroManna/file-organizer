from pathlib import Path
import logging

# Configuración del logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

# Ruta de la carpeta Descargas
carpeta_desorganizada = Path(r"D:\Documentos")

# Diccionario que asocia extensiones con categorías
categorias_archivos = {
    'Imágenes': {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.avif'},
    'Documentos': {'.pdf', '.docx', '.txt', '.pptx', '.xlsx', '.xls', '.xlsm', '.csv', '.json', '.php', '.xml'},
    'Música': {'.mp3', '.wav', '.flac', '.aac', '.ogg', '.m3u8'},
    'Vídeos': {'.mp4', '.mkv', '.avi', '.mov', '.wmv'},
    'Programas': {'.exe', '.msi', '.apk', '.dmg', '.deb', '.sh', '.dll', '.iso', '.bin'},
    'Comprimidos': {'.zip', '.rar', '.7z', '.tar', '.gz', '.xz'},
    'Otros': set()  # Para archivos sin una categoría específica
}

def organizar_descargas():
    """Organiza archivos en la carpeta Descargas según su tipo."""
    
    for archivo in carpeta_desorganizada.iterdir():
        if archivo.is_dir():
            continue  # Ignorar carpetas

        extension = archivo.suffix.lower()  # Obtener extensión en minúsculas
        movido = False

        for categoria, extensiones in categorias_archivos.items():
            if extension in extensiones:
                carpeta_destino = carpeta_desorganizada / categoria
                carpeta_destino.mkdir(exist_ok=True)  # Crear si no existe
                
                try:
                    archivo.rename(carpeta_destino / archivo.name)
                    logging.info(f"Movido: {archivo.name} → {categoria}/")
                except Exception as e:
                    logging.error(f"No se pudo mover {archivo.name}: {e}")
                movido = True
                break

        # Si no se encontró categoría, mover a 'Otros'
        if not movido:
            carpeta_otros = carpeta_desorganizada / 'Otros'
            carpeta_otros.mkdir(exist_ok=True)
            try:
                archivo.rename(carpeta_otros / archivo.name)
                logging.info(f"Movido: {archivo.name} → Otros/")
            except Exception as e:
                logging.error(f"No se pudo mover {archivo.name}: {e}")

# Ejecutar la función
if __name__ == "__main__":
    organizar_descargas()
