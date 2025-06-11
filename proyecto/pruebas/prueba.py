import tkinter as tk

# Datos simulados: géneros y sus puntuaciones
generos = {
    "Acción": 10,
    "Aventura": 7,
    "Rol/RPG": 12,
    "Shooter": 6,
    "Estrategia": 4,
    "Puzzle": 5,
    "Simulación": 8,
    "Deportes": 3,
    "Carreras": 6,
    "Mundo Abierto": 11,
    "Horror": 4,
    "Plataformas": 5
}

# Crear ventana principal
root = tk.Tk()
root.title("Puntuación por Género")
root.geometry("800x400")

# Crear canvas para dibujar la gráfica
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Configuración
padding = 50
bar_width = 30
espacio = 15
max_valor = max(generos.values())
escala = (300 / max_valor)  # Altura máxima de la barra (px)

# Dibujar barras
for i, (genero, puntos) in enumerate(generos.items()):
    x0 = padding + i * (bar_width + espacio)
    y0 = 350
    x1 = x0 + bar_width
    y1 = y0 - puntos * escala

    # Barra
    canvas.create_rectangle(x0, y0, x1, y1, fill="skyblue", outline="black")

    # Etiqueta de puntos
    canvas.create_text((x0 + x1) // 2, y1 - 10, text=str(puntos), fill="black")

    # Nombre del género
    canvas.create_text((x0 + x1) // 2, y0 + 10, text=genero, angle=45, anchor="nw", font=("Arial", 8))

root.mainloop()
