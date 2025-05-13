import os
import math
import subprocess
from datetime import date
from tkinter import Tk, Button, Label, filedialog, messagebox
from PyPDF2 import PdfMerger

# Constantes
ARCHIVOS_POR_LOTE = 200
hoy = date.today().strftime("%Y-%m-%d")

# Función para combinar PDFs en lotes
def combinar_pdfs_en_lotes(carpeta):
    pdf_files = sorted([f for f in os.listdir(carpeta) if f.endswith('.pdf')])
    total_pdfs = len(pdf_files)
    num_lotes = math.ceil(total_pdfs / ARCHIVOS_POR_LOTE)
    generados = []

    for lote in range(num_lotes):
        merger = PdfMerger()
        start = lote * ARCHIVOS_POR_LOTE
        end = min(start + ARCHIVOS_POR_LOTE, total_pdfs)

        for i in range(start, end):
            merger.append(os.path.join(carpeta, pdf_files[i]))

        output_name = f"consolidado_{lote + 1}_{hoy}.pdf"
        output_path = os.path.join(carpeta, output_name)
        merger.write(output_path)
        merger.close()
        generados.append(output_path)

    return total_pdfs, len(generados), generados

# Abrir carpeta en el explorador de archivos
def abrir_explorador(path):
    try:
        if os.name == 'nt':
            os.startfile(path)
        elif os.name == 'posix':
            subprocess.Popen(['open', path])
    except Exception as e:
        messagebox.showerror("Error al abrir carpeta", str(e))

# Ejecutar proceso al seleccionar carpeta
def seleccionar_y_procesar():
    carpeta = filedialog.askdirectory()
    if carpeta:
        total, generados, archivos = combinar_pdfs_en_lotes(carpeta)
        mostrar_reporte(carpeta, total, generados)
        abrir_explorador(carpeta)

# Mostrar resultados en ventana
def mostrar_reporte(carpeta, total_archivos, total_generados):
    mensaje = (
        f"📂 Carpeta seleccionada: {carpeta}\n\n"
        f"📄 Total de archivos PDF encontrados: {total_archivos}\n"
        f"🧾 Total de archivos generados: {total_generados}\n\n"
        f"✔️ Los archivos se han guardado como 'consolidado_NUM_FECHA.pdf'."
    )
    messagebox.showinfo("Reporte Final", mensaje)

# Interfaz gráfica
root = Tk()
root.title("Consolidador de PDFs en Lotes de 200")
root.geometry("500x280")

Label(root, text="Combinar PDFs escaneados en bloques de 200", font=("Helvetica", 14), pady=20).pack()
Button(root, text="Seleccionar carpeta de PDFs y Consolidar", command=seleccionar_y_procesar, width=40, height=2).pack(pady=20)

# Leyenda final
Label(root, text="Desarrollado por Nuevas Tecnologías - División TI", font=("Helvetica", 9), fg="gray").pack(side="bottom", pady=10)

root.mainloop()
