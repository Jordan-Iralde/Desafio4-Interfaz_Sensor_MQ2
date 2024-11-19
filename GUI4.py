import tkinter as tk
from tkinter import ttk, messagebox
import random

# Función para abrir la ventana con gráficos
def abrir_graficos(opcion, sensor):
    # Crear una nueva ventana
    graph_window = tk.Toplevel(root)
    graph_window.title(f"Conectado a {opcion} - {sensor}")
    graph_window.geometry("800x600")
    graph_window.configure(bg="#1E3D59")
    
    # =================== TÍTULO ===================
    title_label = tk.Label(graph_window, text=f"Porcentaje de Gas en {sensor}", font=("Arial", 18, "bold"), bg="#1E3D59", fg="white")
    title_label.pack(pady=10)
    
    # =================== GRÁFICO ===================
    graph_frame = tk.Frame(graph_window, bg="#1E3D59")
    graph_frame.pack(pady=20, fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(graph_frame, bg="#554E4E", width=600, height=300, highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Dibujar ejes
    canvas.create_line(50, 250, 550, 250, fill="blue", width=2)  # Eje X
    canvas.create_line(50, 250, 50, 50, fill="red", width=2)     # Eje Y

    # Etiquetas de los ejes
    canvas.create_text(300, 270, text="Tiempo", fill="white", font=("Arial", 10))
    canvas.create_text(30, 150, text="Porcentaje de Gas", fill="white", font=("Arial", 10), angle=90)

    # Lista de puntos para el gráfico
    puntos = []

    # =================== PORCENTAJE DE GAS ===================
    font_stylePorcentaje = ("Arial", 40)
    font_styleGas = ("Arial", 20)

    variableGas = tk.Label(graph_window, text="GAS", bg="#1E3D59", fg="white", font=font_styleGas)
    variableGas.place(x=100, y=400)

    label_porcentaje = tk.Label(graph_window, text="0%", bg="#1E3D59", fg="#E05E26", font=font_stylePorcentaje)
    label_porcentaje.place(x=100, y=450)

    # Función para actualizar el gráfico y el porcentaje
    def actualizar_graficos():
        nonlocal puntos
        porcentaje = random.randint(0, 100)
        label_porcentaje.config(text=f"{porcentaje}%")

        # Cambia el color según el porcentaje
        if porcentaje < 34:
            label_porcentaje.config(fg="#008000")  # Verde
        elif porcentaje < 67:
            label_porcentaje.config(fg="#E05E26")  # Naranja
        else:
            label_porcentaje.config(fg="#FF0000")  # Rojo

        # Actualiza el gráfico en el canvas
        x = 50 + len(puntos) * 5
        y = 250 - (porcentaje * 2)

        if x < 550:  # Dibuja dentro del Canvas
            puntos.append((x, y))
            if len(puntos) > 1:
                canvas.create_line(puntos[-2], puntos[-1], fill="white", width=2)
        else:
            # Reinicia el gráfico
            puntos = []
            canvas.delete("all")
            canvas.create_line(50, 250, 550, 250, fill="blue", width=2)  # Eje X
            canvas.create_line(50, 250, 50, 50, fill="red", width=2)     # Eje Y
            canvas.create_text(300, 270, text="Tiempo", fill="white", font=("Arial", 10))
            canvas.create_text(30, 150, text="Porcentaje de Gas", fill="white", font=("Arial", 10), angle=90)

        graph_window.after(1000, actualizar_graficos)  # Actualiza cada segundo

    # Botón de Desconectar
    def cerrar_ventana():
        graph_window.destroy()

    boton_desconectar = tk.Button(graph_window, text="Desconectar", bg="#FF5555", fg="white", font=("Arial", 14), command=cerrar_ventana)
    boton_desconectar.pack(pady=10)

    # Iniciar la actualización de gráficos
    actualizar_graficos()

# Validar selección y abrir gráficos
def validar_y_conectar():
    opcion = dropdown.get()
    seleccion = listbox.curselection()

    if not opcion:
        messagebox.showwarning("Error", "Selecciona del desplegable.")
        return
    
    if not seleccion:
        messagebox.showwarning("Error", "Selecciona un sensor de la lista.")
        return
    
    sensor = listbox.get(seleccion[0])
    abrir_graficos(opcion, sensor)

# =================== VENTANA PRINCIPAL ===================
root = tk.Tk()
root.title("Detector de Gases")
root.geometry("800x600")
root.configure(bg="#1E3D59")

# =================== TÍTULO ===================
title_label = tk.Label(root, text="Detector de Gases", font=("Arial", 24, "bold"), bg="#1E3D59", fg="white")
title_label.pack(pady=20)

# =================== CONTENEDOR ===================
container = tk.Frame(root, bg="#D9D9D9", relief="flat", bd=0)
container.place(relx=0.5, rely=0.5, anchor="center")
container.config(padx=50, pady=20)

# =================== DESPLEGABLE ===================
dropdown_label = tk.Label(container, text="Selecciona una opción:", bg="#D9D9D9", font=("Arial", 14))
dropdown_label.pack(pady=10)

options = ["USB1", "USB2", "Bluetooth"]
dropdown = ttk.Combobox(container, values=options, font=("Arial", 14), width=25, state="readonly")
dropdown.pack(pady=10)

# =================== LISTA ===================
list_label = tk.Label(container, text="Sensores Detectados:", bg="#D9D9D9", font=("Arial", 12))
list_label.pack(pady=5)

listbox = tk.Listbox(container, font=("Arial", 12), height=6)
listbox.pack(pady=10, fill=tk.BOTH, expand=True)

for item in ["Sensor 1", "Sensor 2", "Sensor 3", "Sensor 4"]:
    listbox.insert(tk.END, item)

# =================== BOTÓN ===================
connect_button = tk.Button(container, text="Conectar", bg="#2599D2", fg="white", font=("Arial", 14), width=20, command=validar_y_conectar)
connect_button.pack(pady=20)

# =================== INICIAR APLICACIÓN ===================
root.mainloop()
