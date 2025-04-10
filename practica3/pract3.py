import tkinter as tk
from tkinter import messagebox
import sqlite3
import random

# Paleta de colores y fuentes
COLOR_FONDO = "#2c3e50"
COLOR_BOTON = "#3498db"
COLOR_BOTON_HOVER = "#2980b9"
COLOR_TEXTO = "#ecf0f1"
COLOR_ENTRADA = "#34495e"
FUENTE_TITULO = ("Arial", 18, "bold")
FUENTE_PREGUNTA = ("Arial", 14)
FUENTE_BOTON = ("Arial", 12)

# Conexión a la base de datos
def conectar_db():
    conexion = sqlite3.connect("mobs.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM mobs")
    mobs = cursor.fetchall()
    columnas = [desc[0] for desc in cursor.description]
    return conexion, cursor, mobs, columnas

# Lista base de preguntas
preguntas_base = [
    ("¿Tu mob es hostil?", "hostil"),
    ("¿Tu mob es neutral?", "neutral"),
    ("¿Tu mob se puede montar o montarse?", "montar"),
    ("¿Tu mob aparece en el Overworld?", "overworld"),
    ("¿Tu mob aparece en el Nether?", "nether"),
    ("¿Tu mob puede aparecer naturalmente en una aldea?", "aldea"),
    ("¿Tu mob aparece en el End?", "end"),
    ("¿Tu mob puede volar?", "vuela"),
    ("¿Tu mob es acuático?", "acuatico"),
    ("¿Tu mob puede ser domesticado o es un animal de granja?", "domesticar"),
    ("¿Tu mob es un no vivo? (ej. esqueleto, zombie)", "death"),
    ("¿Tu mob es un jefe final?", "boss"),
    ("¿Tu mob es bípedo?", "bipedo"),
    ("¿Tu mob se encuentra en alguna fortaleza?", "fortaleza"),
    ("¿Tu mob suelta algún drop?", "drops"),
    ("¿Tu mob suelta cuero?", "cuero")
]
# Función para crear botones con estilo
def crear_boton(frame, texto, comando, color=COLOR_BOTON):
    boton = tk.Button(
        frame,
        text=texto,
        command=comando,
        bg=color,
        fg=COLOR_TEXTO,
        font=FUENTE_BOTON,
        padx=15,
        pady=5,
        bd=0,
        relief=tk.FLAT,
        activebackground=COLOR_BOTON_HOVER,
        activeforeground=COLOR_TEXTO
    )
    boton.bind("<Enter>", lambda e: boton.config(bg=COLOR_BOTON_HOVER))
    boton.bind("<Leave>", lambda e: boton.config(bg=color))
    return boton


# Interfaz principal
def iniciar_juego():
    global indice_pregunta, respuestas, preguntas, filtrados, mobs, columnas
    conexion, cursor, mobs, columnas = conectar_db()
    preguntas = random.sample(preguntas_base, len(preguntas_base))
    respuestas = {}
    indice_pregunta = 0
    filtrados = mobs.copy()
     # Cargar imagen (opcional, si existe 'genio.gif')
    try:
        imagen_genio = tk.PhotoImage(file="aldeano.png")
    except:
        imagen_genio = None
    
    mostrar_pregunta()
    for widget in ventana.winfo_children():
        widget.destroy()

    mostrar_pregunta()

def mostrar_pregunta():
    for widget in ventana.winfo_children():
        widget.destroy()
        
    frame = tk.Frame(ventana, bg=COLOR_FONDO)
    frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    pregunta_actual = preguntas[indice_pregunta][0]
    etiqueta = tk.Label(
        frame,
        text=pregunta_actual,
        font=FUENTE_PREGUNTA,
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO,
        wraplength=400
    )
    etiqueta.pack(pady=20)

    botones_frame = tk.Frame(ventana, bg=COLOR_FONDO)
    botones_frame.pack(pady=10)

    crear_boton(botones_frame, "Sí", lambda: responder(1), "#2ecc71").grid(row=0, column=0, padx=10)
    crear_boton(botones_frame, "No", lambda: responder(0), "#e74c3c").grid(row=0, column=1, padx=10)
    crear_boton(botones_frame, "Tal vez", lambda: responder(-1), "#95a5a6").grid(row=0, column=2, padx=10)

    # Función para procesar respuestas
def responder(valor):
    global indice_pregunta, filtrados
    campo = preguntas[indice_pregunta][1]
    respuestas[campo] = valor

    if valor != -1:
        index = columnas.index(campo)
        filtrados = [mob for mob in filtrados if mob[index] == valor]

    indice_pregunta += 1
    if indice_pregunta < len(preguntas) and filtrados:
        mostrar_pregunta()
    else:
        mostrar_resultado()

# Función para mostrar resultados
def mostrar_resultado():
    for widget in ventana.winfo_children():
        widget.destroy()

    frame = tk.Frame(ventana, bg=COLOR_FONDO)
    frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    if filtrados:
        mob = filtrados[0][1]
        resultado = tk.Label(
            frame,
            text=f"¡Creo que es... {mob}!",
            font=FUENTE_TITULO,
            bg=COLOR_FONDO,
            fg="#f1c40f"
        )
        resultado.pack(pady=20)

        pregunta = tk.Label(
            frame,
            text="¿Es correcto?",
            font=FUENTE_PREGUNTA,
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO
        )
        pregunta.pack()

        botones_frame = tk.Frame(frame, bg=COLOR_FONDO)
        botones_frame.pack(pady=10)

        crear_boton(botones_frame, "Sí", reiniciar, "#2ecc71").pack(side=tk.LEFT, padx=10)
        crear_boton(botones_frame, "No", lambda: mostrar_formulario(True), "#e74c3c").pack(side=tk.RIGHT, padx=10)
    else:
        mostrar_formulario(True)

# Función para añadir nuevos mobs
def mostrar_formulario(mob_no_encontrado):
    for widget in ventana.winfo_children():
        widget.destroy()

    frame = tk.Frame(ventana, bg=COLOR_FONDO)
    frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    label = tk.Label(
        frame,
        text="¿Cuál era tu mob?",
        font=FUENTE_PREGUNTA,
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO
    )
    label.pack(pady=10)

    entrada = tk.Entry(frame, font=("Arial", 12), bg=COLOR_ENTRADA, fg=COLOR_TEXTO, insertbackground=COLOR_TEXTO)
    entrada.pack(pady=5)

    def guardar():
        nombre = entrada.get()
        if nombre:
            conexion = sqlite3.connect("mobs.db")
            cursor = conexion.cursor()
            datos = [nombre] + [respuestas.get(col, -1) for col in columnas[2:]]
            cursor.execute(
                f"INSERT INTO mobs ({', '.join(columnas[1:])}) VALUES ({', '.join(['?'] * (len(columnas)-1))})",
                datos
            )
            conexion.commit()
            conexion.close()
            messagebox.showinfo("¡Guardado!", f"{nombre} fue añadido a la base de datos.")
            reiniciar()

    crear_boton(frame, "Guardar", guardar, "#2ecc71").pack(pady=10)

    if mob_no_encontrado:
        crear_boton(frame, "Cancelar", reiniciar, "#95a5a6").pack(pady=5)

# Reiniciar juego
def reiniciar():
    iniciar_juego()

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Minecraft Akinator")
ventana.geometry("600x400")
ventana.configure(bg=COLOR_FONDO)
ventana.resizable(True, True)

# Iniciar aplicación
iniciar_juego()
ventana.mainloop()