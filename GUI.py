import tkinter as tk

# Configuración de la ventana principal
root = tk.Tk()
root.title("Detector de Gases UI")
root.configure(bg="#322F2F")  # Color de Fondo
root.geometry("1280x720")  # Tamaño de Ventana

# Fuentes Para Variables
font_stylePorcentaje = ("Inter", 140)
font_styleGas = ("Inter", 90)

# Variables iniciales
porcentaje = 0
variableGas = tk.Label(root, text="GAS", bg="#322F2F", font=font_styleGas)  # Para Mostrar "Gas"
label = tk.Label(root, text=f"{porcentaje}%", bg="#322F2F", fg="#E05E26", font=font_stylePorcentaje)  # Mostrar Valores

# Ubicaciones de Variables
variableGas.place(x=70, y=30)
label.place(x=50, y=150)

# Crear el widget Canvas para el gráfico
canvas = tk.Canvas(root, bg="#554E4E", width=600, height=400)
canvas.place(x=550, y=100)

# Dibujar ejes en el Canvas
canvas.create_line(50, 350, 550, 350, fill="blue", width=2)  # Eje X
canvas.create_line(50, 350, 50, 50, fill="red", width=2)     # Eje Y

# Etiquetas de los ejes
canvas.create_text(300, 370, text="Tiempo", fill="white", font=("Inter", 12))
canvas.create_text(30, 200, text="Porcentaje de gas\nvariante al tiempo", fill="white", font=("Inter", 10), angle=90)

# Lista para almacenar los puntos del gráfico
puntos = []

# Función para actualizar el porcentaje y el color de la etiqueta `variableGas`
def actualizar_porcentaje():
    global porcentaje, puntos
    if porcentaje < 100:  # Limita el porcentaje hasta 100
        porcentaje += 1
        label.config(text=f"{porcentaje}%")  # Actualiza el texto en la etiqueta de porcentaje
        
        # Cambia el color de `variableGas` basado en el valor de `porcentaje`
        if porcentaje < 34:
            variableGas.config(fg="#008000")  # Menos de 34%
            label.config(fg="#008000")
        elif porcentaje < 67:
            variableGas.config(fg="#E05E26")  # Mas de 33% y 67%
            label.config(fg="#E05E26")
        else:
            variableGas.config(fg="#FF0000")  # Mas de 66%
            label.config(fg="#FF0000")
        
        # Actualiza el gráfico en el Canvas
        x = 50 + len(puntos) * 5  # Incrementa la posición en X
        y = 350 - (porcentaje * 3)  # Calcula la posición en Y según el porcentaje
        if x < 550:  # Dibuja solo dentro del Canvas
            puntos.append((x, y))
            if len(puntos) > 1:
                canvas.create_line(puntos[-2], puntos[-1], fill="white", width=2)
        
        root.after(100, actualizar_porcentaje)  # Llama a la función después de 1 segundo

# Inicia la actualización de porcentaje
actualizar_porcentaje()

root.mainloop()
