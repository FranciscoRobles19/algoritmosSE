import tkinter as tk
import sqlite3

# Conectar a la base de datos correcta
conn = sqlite3.connect('nextgame.db')
cursor = conn.cursor()

# Preguntas (ordenadas según las columnas en la tabla)
preguntas = [
    "¿Te gusta tomar decisiones que afectan la historia del juego?",
    "¿Prefieres juegos con combates rápidos y llenos de acción?",
    "¿Te interesa explorar mundos abiertos y grandes sin un camino fijo?",
    "¿Disfrutas resolver acertijos o rompecabezas durante el juego?",
    "¿Te gustan los juegos en primera o tercera persona con disparos?",
    "¿Te interesan los juegos de estrategia donde debes pensar cada movimiento?",
    "¿Te gusta crear, construir o administrar recursos en el juego?",
    "¿Te atraen las historias profundas y los personajes con desarrollo emocional?",
    "¿Te interesa competir en juegos de deportes como fútbol o baloncesto?",
    "¿Te gustan los juegos de carreras con autos, motos o vehículos de fantasía?",
    "¿Disfrutas los juegos que causan miedo o tensión?",
    "¿Te gustan los juegos donde debes saltar y moverte entre plataformas?",
    "¿Prefieres juegos en los que puedes personalizar tu personaje o mundo?",
    "¿Te atraen los juegos ambientados en mundos de fantasía o medievales?",
    "¿Te gustaría tener libertad total para hacer lo que quieras en el juego?",
    "¿Te gusta jugar con armas cuerpo a cuerpo como espadas o martillos?",
    "¿Prefieres juegos donde no importa la historia, solo la habilidad o rapidez?",
    "¿Te interesan los juegos que simulan la vida real o profesiones?",
    "¿Te gustan los juegos que puedes jugar solo sin necesidad de internet?",
    "¿Te interesa una narrativa bien contada como parte clave del juego?"
]

respuestas_usuario = [-1] * len(preguntas)
indice_pregunta = 0

# Colores
COLOR_FONDO = "#0a0f1a"
COLOR_PREGUNTA = "#F3F3F3"
COLOR_BOTON_SI = "#00b0ff"
COLOR_BOTON_NO = "#00b0ff"
COLOR_BOTON_TALVEZ = "#00b0ff"
COLOR_RESULTADO = "#007c6c"

# Interfaz
ventana = tk.Tk()
ventana.title("NextGame - Recomendador de Género de Videojuegos")
ventana.geometry("750x400")
ventana.configure(bg=COLOR_FONDO)

pregunta_label = tk.Label(
    ventana,
    text="",
    wraplength=700,
    font=("Helvetica", 16, "bold"),
    fg=COLOR_PREGUNTA,
    bg=COLOR_FONDO
)
pregunta_label.pack(pady=30)


def responder(valor):
    global indice_pregunta
    respuestas_usuario[indice_pregunta] = valor
    indice_pregunta += 1
    if indice_pregunta < len(preguntas):
        pregunta_label.config(text=preguntas[indice_pregunta])
    else:
        mostrar_recomendacion()

def mostrar_recomendacion():
    cursor.execute("SELECT * FROM games")
    resultados = cursor.fetchall()

    mejor_genero = None
    mejor_puntaje = -1

    for fila in resultados:
        nombre = fila[1]
        valores = fila[2:]
        puntaje = sum(r * g if r != -1 else 0 for r, g in zip(respuestas_usuario, valores))

        if puntaje > mejor_puntaje:
            mejor_genero = nombre
            mejor_puntaje = puntaje

    if mejor_genero and mejor_puntaje > 0:
        resultado_label.config(text=f"🎮 Género recomendado: {mejor_genero.upper()}")
    else:
        resultado_label.config(
            text="⚠️ No se encontró una coincidencia clara.\n¡Pero podrías probar con: {}!".format(mejor_genero.upper() if mejor_genero else "ninguno")
        )

# Frame para botones
botones_frame = tk.Frame(ventana, bg=COLOR_FONDO)
botones_frame.pack(pady=10)

def crear_boton(texto, color, comando):
    return tk.Button(
        botones_frame,
        text=texto,
        width=15,
        height=2,
        bg=color,
        fg="black",
        font=("Helvetica", 11),
        relief="raised",
        bd=2,
        command=comando,
        activebackground="#dddddd"
    )

boton_si = crear_boton("Sí", COLOR_BOTON_SI, lambda: responder(1))
boton_prob = crear_boton("Tal vez", COLOR_BOTON_TALVEZ, lambda: responder(-1))
boton_no = crear_boton("No", COLOR_BOTON_NO, lambda: responder(0))

boton_si.grid(row=0, column=0, padx=20)
boton_prob.grid(row=0, column=1, padx=20)
boton_no.grid(row=0, column=2, padx=20)

resultado_label = tk.Label(
    ventana,
    text="",
    font=("Helvetica", 14),
    wraplength=700,
    fg=COLOR_RESULTADO,
    bg=COLOR_FONDO,
    justify="center"
)
resultado_label.pack(pady=30)

# Iniciar la primera pregunta
pregunta_label.config(text=preguntas[indice_pregunta])

ventana.mainloop()
