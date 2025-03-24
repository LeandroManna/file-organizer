# Organizador de Archivos

Este script en Python organiza automáticamente los archivos en una carpeta específica (por defecto, `D:\Documentos`) según su tipo, moviéndolos a subcarpetas categorizadas. Es especialmente útil para la carpeta de Descargas, evitando que se acumule desorden.

## Características
- Clasifica archivos en categorías como **Imágenes, Documentos, Música, Vídeos, Programas, Comprimidos y Otros**.
- Detecta automáticamente las extensiones de archivo y las mueve a la carpeta correspondiente.
- Si la carpeta de destino no existe, el script la crea automáticamente.
- Los archivos sin una categoría definida se mueven a la carpeta "Otros".
- Soporte para extensiones en mayúsculas y minúsculas.
- Manejo de errores si un archivo está en uso.
- Se puede ejecutar manualmente o programar con el **Task Scheduler** de Windows.

## Instalación y Uso
### Requisitos
- Python 3.x instalado en el sistema.

### Instalación
1. Clonar o descargar el script en tu PC.
2. Asegurarse de que tienes Python instalado.
3. Opcionalmente, instalar dependencias (aunque el script solo usa librerías estándar de Python).

### Ejecución
Ejecuta el script desde la terminal o consola de comandos:

```sh
python organizador.py
```

## Personalización
El script permite modificar la ruta de la carpeta a organizar. Para ello, edita la siguiente línea en `organizador.py`:

```python
carpeta_descargas = Path(r"D:\Documentos")  # Modifica esta ruta según necesites
```

Puedes cambiarla, por ejemplo, para organizar la carpeta de Descargas:

```python
carpeta_descargas = Path(r"C:\Users\TuUsuario\Downloads")
```

También puedes añadir nuevas categorías y extensiones en el diccionario `categorias_archivos`:

```python
categorias_archivos = {
    'Código': {'.py', '.js', '.html', '.css', '.cpp', '.java'},
    'Libros': {'.epub', '.mobi', '.azw3', '.pdf'}
}
```

## Automatización con el Task Scheduler de Windows
Si deseas que el script se ejecute automáticamente cada cierto tiempo, puedes programarlo con el **Task Scheduler** de Windows:
1. Abre **Programador de Tareas** en Windows.
2. Crea una **nueva tarea básica**.
3. Configura la frecuencia de ejecución (por ejemplo, diariamente o al iniciar sesión).
4. En **Acción**, selecciona **Iniciar un programa** y elige `python.exe`.
5. En **Argumentos**, indica la ruta completa del script `organizador.py`.
6. Guarda la tarea y actívala.

## Contribuciones
Si tienes ideas para mejorar el script, ¡cualquier contribución es bienvenida! Puedes hacer un **fork** y enviar un **pull request** en el repositorio.

## Licencia
Este proyecto se distribuye bajo la licencia **MIT**, lo que significa que puedes usarlo, modificarlo y distribuirlo libremente.

---

🎯 **Mantén tu carpeta de Descargas organizada automáticamente con este script! 🚀**

