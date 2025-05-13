# 📁 UnificaPDF – Consolidación inteligente de archivos escaneados

**Desarrollado por Nuevas Tecnologías - División TI**

**UnificaPDF** es una herramienta de escritorio para Windows que permite consolidar archivos PDF escaneados en lotes de hasta 200 documentos, generando archivos de salida numerados y con fecha automática. Está diseñada para procesar grandes volúmenes de escaneos de forma rápida y organizada.

---

## 🚀 ¿Cómo funciona?

1. El usuario selecciona una carpeta que contenga múltiples archivos PDF (cada uno con una imagen escaneada).
2. La aplicación agrupa esos archivos en bloques de 200 y genera archivos consolidados con nombre:

consolidado_1_YYYY-MM-DD.pdf
consolidado_2_YYYY-MM-DD.pdf

3. Los archivos se guardan en la **misma carpeta original**.
4. Se muestra un resumen con:
- Total de archivos leídos
- Total de archivos consolidados creados
5. Se abre automáticamente el explorador en la carpeta de salida.

---

## 📦 Requisitos del sistema

- Windows 10 o superior
- Python 3.10 o superior (para desarrollo o ejecución en modo script)
- 8 GB de RAM recomendados para procesamiento fluido

---

## 📚 Dependencias (instalación)

Este proyecto utiliza:

- [`PyPDF2`](https://pypi.org/project/PyPDF2/)
- Librerías estándar de Python: `tkinter`, `os`, `subprocess`, `datetime`, etc.

Instalación:

```bash
pip install PyPDF2

🧑‍💻 Guía de uso para desarrolladores

Clonar el proyecto
git clone https://github.com/tu_usuario/unificapdf.git
cd unificapdf

Ejecutar en modo desarrollo
python unificapdf_gui.py

🛠️ Compilación como ejecutable .exe
Este proyecto se puede distribuir como una aplicación independiente usando PyInstaller:

Instalar PyInstaller
pip install pyinstaller

Generar .exe
pyinstaller --onefile --noconsole --name "UnificaPDF" unificapdf_gui.py

👨‍🔧 Créditos
Autor: Equipo de Nuevas Tecnologías – División TI

Nombre de producto: UnificaPDF
