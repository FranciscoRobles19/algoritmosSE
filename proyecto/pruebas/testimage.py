import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo con imagen")

# Cargar imagen (asegúrate de que esté en el mismo directorio)
imagen = tk.PhotoImage(file="C:/Users/javro/OneDrive/Escritorio/ceti colomos/7mo semestre/sistemas expertos/proyecto/imagenes/imagen.png")

# Etiqueta que muestra la imagen
imagen_label = tk.Label(ventana, image=imagen)
imagen_label.pack()

ventana.mainloop()