import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def get_images_folder():
    # Encuentra carpeta Imagenes
    if os.name == 'nt':  # Windows
        return os.path.expanduser("~/Pictures")


def convert_to_ico(input_image_path, output_ico_path):
    try:
        # Abre la imagen de entrada
        image = Image.open(input_image_path)

        # Convierte la imagen a un ícono de ico
        image.save(output_ico_path, format="ICO")
        result_label.config(text="¡Conversión exitosa!")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

        # Obtén el nombre de archivo sin la extensión y agrega .ico
        file_name = ".".join(file_path.split("/")[-1].split(".")[:-1])
        images_folder = get_images_folder()
        output_path = os.path.join(images_folder, file_name + ".ico")
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_path)

def convert_image():
    input_image = input_entry.get()
    output_ico = output_entry.get()
    convert_to_ico(input_image, output_ico)

# Configurar la ventana de la aplicación
app = tk.Tk()
app.title("Convertidor de Imágenes a .ico")

# Etiqueta para mostrar el resultado
result_label = tk.Label(app, text="", fg="green")
result_label.pack()

# Entrada de archivo de entrada
input_label = tk.Label(app, text="Selecciona una imagen de entrada:")
input_label.pack()
input_entry = tk.Entry(app)
input_entry.pack()
browse_button = tk.Button(app, text="Buscar", command=browse_image)
browse_button.pack()

# Entrada de archivo de salida
output_label = tk.Label(app, text="Ruta del archivo de salida:")
output_label.pack()
output_entry = tk.Entry(app)
output_entry.pack()

# Botón para convertir
convert_button = tk.Button(app, text="Convertir", command=convert_image)
convert_button.pack()

app.mainloop()
