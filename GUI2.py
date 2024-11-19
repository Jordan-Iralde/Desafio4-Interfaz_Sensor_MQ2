import tkinter as tk
from tkinter import ttk

# FUNCIONES
def abrir_ventana_grafico():
    """Cambia a la ventana del gráfico si se ha seleccionado un puerto."""
    if selector_puerto.get() == "":
        error_label.config(text="¡Por favor selecciona un puerto!")
    else:
        ventana_selector.pack_forget()
        ventana_grafico.pack(fill="both", expand=True)
        error_label.config(text="")  # Elimina el mensaje de error si se ha seleccionado un puerto

def regresar_ventana_selector():
    """Regresa a la ventana del selector."""
    ventana_grafico.pack_forget()
    ventana_selector.pack(fill="both", expand=True)

# VENTANA PRINCIPAL
root = tk.Tk()
root.title("Detector de Gases")
root.geometry("800x600")
root.configure(bg="#1E3D59")

# ======================= VENTANA 1: SELECCIONAR PUERTO =======================
ventana_selector = tk.Frame(root, bg="#1E3D59")
ventana_selector.pack(fill="both", expand=True)

# Etiqueta para seleccionar el puerto
label_seleccion = tk.Label(ventana_selector, text="Seleccione un puerto:", font=("Arial", 16), bg="#1E3D59", fg="white")
label_seleccion.pack(pady=20)

# Crear el combobox para elegir el tipo de conexión (solo selección, no edición)
selector_puerto = ttk.Combobox(ventana_selector, values=["USB1", "USB2", "Bluetooth"], font=("Arial", 14), state="readonly")
selector_puerto.pack(pady=10)

# Etiqueta de error si no se ha seleccionado un puerto
error_label = tk.Label(ventana_selector, text="", font=("Arial", 12), bg="#1E3D59", fg="red")
error_label.pack(pady=5)

# Botón para conectar (solo habilitado cuando se selecciona una opción)
btn_conectar = tk.Button(ventana_selector, text="Conectar", font=("Arial", 14), command=abrir_ventana_grafico)
btn_conectar.pack(pady=20)

# ======================= VENTANA 2: GRÁFICO DE GASES =======================
ventana_grafico = tk.Frame(root, bg="#1E3D59")

# Etiqueta para el título
titulo_grafico = tk.Label(ventana_grafico, text="Porcentaje de gas variante al tiempo", font=("Arial", 18), bg="#1E3D59", fg="white")
titulo_grafico.place(x=200, y=20)

# Botón para regresar a la ventana del selector
btn_regresar = tk.Button(ventana_grafico, text="Volver", font=("Arial", 14), command=regresar_ventana_selector)
btn_regresar.place(x=350, y=450)

# INICIAR LA APLICACIÓN
root.mainloop()
