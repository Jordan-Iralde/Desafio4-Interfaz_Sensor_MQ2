import tkinter as tk

# Configuración de la ventana principal
root = tk.Tk()
root.title("Detector de Gases UI")
root.configure(bg="#322F2F") #Color de Fondo

#Fuentes Para Variables
font_stylePorcentaje = ("Inter", 140)
font_styleGas = ("Inter", 90)

root.geometry("1280x720") #Tamaño de Ventana

# Variables iniciales
# En el porcentaje vamos a poner lso valores recibidos del sensor de humo
porcentaje = 0
variableGas = tk.Label(root, text="GAS", bg="#322F2F", font=font_styleGas) #Para Mostrar "Gas"
label = tk.Label(root, text=f"{porcentaje}%", bg="#322F2F", fg="#E05E26", font=font_stylePorcentaje) #Mostrar Valores
Grafico = tk.Label(root, bg="#554E4E")

# Ubicaciones de Variables
variableGas.place(x=70, y=30)
label.place(x=50, y=150)
Grafico.place(x=550, y=100)

# Configuraciones
Grafico.config(width=100, height=30)


# Función para actualizar el porcentaje y el color de la etiqueta `variableGas`
def actualizar_porcentaje():
    global porcentaje
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
        
        root.after(100, actualizar_porcentaje)  # Llama a la función después de 1 segundo

# Inicia la actualización de porcentaje
actualizar_porcentaje()

root.mainloop()
