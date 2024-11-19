import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana de Conexión")
root.geometry("800x600")

ventana_selector = tk.Frame(root, bg="#1E3D59")
ventana_selector.pack(fill="both", expand=True)

# Crear el contenedor con fondo #D9D9D9 y padding
container = tk.Frame(root, bg="#D9D9D9")
container.place(relx=0.5, rely=0.5, anchor="center")  # Centrado en la ventana

# Añadir un padding dentro del contenedor
container.config(padx=100, pady=20)  # Padding alrededor del contenido

# Crear el desplegable con las opciones
dropdown_label = tk.Label(container, text="Selecciona una opción:", bg="#D9D9D9", font=("Arial", 14))
dropdown_label.pack(pady=10)

options = ["USB1", "USB2", "Bluetooth"]
dropdown = ttk.Combobox(container, values=options, font=("Arial", 14), width=25 )
dropdown.pack(pady=10)

# Crear la lista de valores (puedes modificarla según lo que necesites)
list_label = tk.Label(container, text="Sensores Detectados:", bg="#D9D9D9")
list_label.pack(pady=5)

listbox = tk.Listbox(container)
listbox.pack(pady=10, fill=tk.BOTH, expand=True)

# Agregar algunos valores a la lista
for item in ["Valor 1", "Valor 2", "Valor 3", "Valor 4"]:
    listbox.insert(tk.END, item)


# Crear el botón de conectar
connect_button = tk.Button(container, text="Conectar", bg="#2599D2", fg="white", width=25)
connect_button.pack(pady=20)



# Iniciar la aplicación
root.mainloop()