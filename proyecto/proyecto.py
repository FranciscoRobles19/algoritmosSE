import tkinter as tk
import sqlite3


imagen_genero = None
imagen_genero_label = None
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
ventana.geometry("750x800")
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



# Diccionario de juegos recomendados por género
recomendaciones_juegos = {
    "accion": [
        "God of War Ragnarok",
        "Metal Gear Solid 5",
        "The Witcher 3"
    ],
    "aventura": [
        "Assassins Creed 4 black flag",
        "Cyberpunk 2077",
        "The legend of zelda"
    ],
    "rpg": [
        "The Elder Scrolls V: Skyrim",
        "Elden Ring",
        "Baldurs Gate 3"
    ],
    "shooter": [#revisar shooter duplicado con accion
        "Call of duty MW/Black OPS",
        "DOOM Eternal",
        "Gears of war 5"
    ],
    "estrategia": [
        "Civilization VI",
        "Age of empires",
        "Cruzader Kings II"
    ],
    "deportes": [
        "EA Sports FC",
        "NBA 2K25",
        "F1 25"
    ],
    "simulacion": [
        "Truck simulator",
        "Cities: Skylines 2",
        "Microsoft Flight Simulator 24"
    ],
    "carreras": [
        "W2C 10",
        "Forza Motorsport",
        "Need For Speed"
    ],
    "puzzle": [
        "Tetris",
        "Portal 2",
        "Limbo"
    ],
    "openworld": [
        "Grand Theft Auto V",
        "Red Dead Redemption 2",
        "Cyberpunk 2077"
    ]
    
}

def reiniciar_test():
    global respuestas_usuario, indice_pregunta, imagen_genero_label

    respuestas_usuario = [-1] * len(preguntas)
    indice_pregunta = 0
    pregunta_label.config(text=preguntas[indice_pregunta])
    resultado_label.config(text="")

    # Ocultar imagen anterior si existe
    if imagen_genero_label:
        imagen_genero_label.pack_forget()
        imagen_genero_label = None

    # Reactivar botones
    boton_si.config(state="normal")
    boton_no.config(state="normal")
    boton_prob.config(state="normal")

    # Ocultar el botón de reinicio
    boton_reiniciar.pack_forget()

def responder(valor):
    global indice_pregunta
    respuestas_usuario[indice_pregunta] = valor
    indice_pregunta += 1
    if indice_pregunta < len(preguntas):
        pregunta_label.config(text=preguntas[indice_pregunta])
    else:
        mostrar_recomendacion()

def mostrar_recomendacion():
    global imagen_genero_label, imagen_genero  # Para que la imagen no se borre

    cursor.execute("SELECT * FROM games")
    resultados = cursor.fetchall()

    mejor_genero = None
    mejor_puntaje = -1

    mejores = []
    for fila in resultados:
        nombre = fila[1]
        valores = fila[2:]
        puntaje = sum(r * g if r != -1 else 0 for r, g in zip(respuestas_usuario, valores))
        mejores.append((nombre, puntaje))

    # Ordenar por puntaje y quedarnos con el mayor
    mejores.sort(key=lambda x: x[1], reverse=True)
    mejor_genero, mejor_puntaje = mejores[0]


    if mejor_genero and mejor_puntaje > 0:
        texto = f"🎮 Género recomendado: {mejor_genero.upper()}"

        # Agregar juegos sugeridos si existen
        if mejor_genero in recomendaciones_juegos:
            juegos = recomendaciones_juegos[mejor_genero]
            texto += "\n\nTe recomendamos probar:\n" + "\n".join(f"• {j}" for j in juegos)

        resultado_label.config(text=texto)

        # Mostrar imagen si el género es Acción
        if mejor_genero == "accion":
            try:
                imagen_genero = tk.PhotoImage(file="C:/Users/javro/OneDrive/Escritorio/ceti colomos/7mo semestre/sistemas expertos/proyecto/imagenes/accion.png").subsample(2, 2)
                imagen_genero_label = tk.Label(ventana, image=imagen_genero, bg=COLOR_FONDO)
                imagen_genero_label.image = imagen_genero  # Previene que la imagen se borre por el recolector de basura
                imagen_genero_label.pack()
            except Exception as e:
                print("Error cargando imagen de acción:", e)


        if mejor_genero == "aventura":
            try:
                imagen_genero = tk.PhotoImage(file="C:/Users/javro/OneDrive/Escritorio/ceti colomos/7mo semestre/sistemas expertos/proyecto/imagenes/aventura.png")
                imagen_genero_label = tk.Label(ventana, image=imagen_genero, bg=COLOR_FONDO)
                imagen_genero_label.image = imagen_genero  # Previene que la imagen se borre por el recolector de basura
                imagen_genero_label.pack()
            except Exception as e:
                print("Error cargando imagen de aventura:", e)

        if mejor_genero == "rpg":
            try:
                imagen_genero = tk.PhotoImage(file="C:/Users/javro/OneDrive/Escritorio/ceti colomos/7mo semestre/sistemas expertos/proyecto/imagenes/rpg.png")
                imagen_genero_label = tk.Label(ventana, image=imagen_genero, bg=COLOR_FONDO)
                imagen_genero_label.image = imagen_genero  # Previene que la imagen se borre por el recolector de basura
                imagen_genero_label.pack()
            except Exception as e:
                print("Error cargando imagen de rpg:", e)
        
        #revisar el shooter duplicado con accion
        if mejor_genero == "shooter":
            try:
                imagen_genero = tk.PhotoImage(file="C:/Users/javro/OneDrive/Escritorio/ceti colomos/7mo semestre/sistemas expertos/proyecto/imagenes/shooter.png")
                imagen_genero_label = tk.Label(ventana, image=imagen_genero, bg=COLOR_FONDO)
                imagen_genero_label.image = imagen_genero  # Previene que la imagen se borre por el recolector de basura
                imagen_genero_label.pack()
            except Exception as e:
                print("Error cargando imagen de shooter:", e)

        if mejor_genero == "estrategia":
            try:
                imagen_genero = tk.PhotoImage(file="C:/Users/javro/OneDrive/Escritorio/ceti colomos/7mo semestre/sistemas expertos/proyecto/imagenes/estrategia.png").subsample(2, 2)
                imagen_genero_label = tk.Label(ventana, image=imagen_genero, bg=COLOR_FONDO)
                imagen_genero_label.image = imagen_genero  # Previene que la imagen se borre por el recolector de basura
                imagen_genero_label.pack()
            except Exception as e:
                print("Error cargando imagen de estrategia:", e)

        if mejor_genero == "puzzle":
            try:
                imagen_genero = tk.PhotoImage(file="C:/Users/javro/OneDrive/Escritorio/ceti colomos/7mo semestre/sistemas expertos/proyecto/imagenes/puzzle.png")
                imagen_genero_label = tk.Label(ventana, image=imagen_genero, bg=COLOR_FONDO)
                imagen_genero_label.image = imagen_genero  # Previene que la imagen se borre por el recolector de basura
                imagen_genero_label.pack()
            except Exception as e:
                print("Error cargando imagen de puzzle:", e)

        if mejor_genero == "simulacion":
            try:
                imagen_genero = tk.PhotoImage(file="C:/Users/javro/OneDrive/Escritorio/ceti colomos/7mo semestre/sistemas expertos/proyecto/imagenes/simulacion.png").subsample(2, 2)
                imagen_genero_label = tk.Label(ventana, image=imagen_genero, bg=COLOR_FONDO)
                imagen_genero_label.image = imagen_genero  # Previene que la imagen se borre por el recolector de basura
                imagen_genero_label.pack()
            except Exception as e:
                print("Error cargando imagen de simulacion:", e)
        
        if mejor_genero == "deportes":
            try:
                imagen_genero = tk.PhotoImage(file="C:/Users/javro/OneDrive/Escritorio/ceti colomos/7mo semestre/sistemas expertos/proyecto/imagenes/deportes.png").subsample(2, 2)
                imagen_genero_label = tk.Label(ventana, image=imagen_genero, bg=COLOR_FONDO)
                imagen_genero_label.image = imagen_genero  # Previene que la imagen se borre por el recolector de basura
                imagen_genero_label.pack()
            except Exception as e:
                print("Error cargando imagen de deportes:", e)

#error duplicado con accion
        if mejor_genero == "carreras":
            try:
                imagen_genero = tk.PhotoImage(file="C:/Users/javro/OneDrive/Escritorio/ceti colomos/7mo semestre/sistemas expertos/proyecto/imagenes/carreras.png")
                imagen_genero_label = tk.Label(ventana, image=imagen_genero, bg=COLOR_FONDO)
                imagen_genero_label.image = imagen_genero  # Previene que la imagen se borre por el recolector de basura
                imagen_genero_label.pack()
            except Exception as e:
                print("Error cargando imagen de carreras:", e)
#error repetido  con rpg
        if mejor_genero == "openworld":
            try:
                imagen_genero = tk.PhotoImage(file="C:/Users/javro/OneDrive/Escritorio/ceti colomos/7mo semestre/sistemas expertos/proyecto/imagenes/openworld.png")
                imagen_genero_label = tk.Label(ventana, image=imagen_genero, bg=COLOR_FONDO)
                imagen_genero_label.image = imagen_genero  # Previene que la imagen se borre por el recolector de basura
                imagen_genero_label.pack()
            except Exception as e:
                print("Error cargando imagen de openworld:", e)

        # Desactivar botones de respuesta
        boton_si.config(state="disabled")
        boton_no.config(state="disabled")
        boton_prob.config(state="disabled")

        # Mostrar botón de reinicio
        boton_reiniciar.pack(pady=20)






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
resultado_label.pack(pady=30, fill="x")

boton_reiniciar = tk.Button(
    ventana,
    text="Reiniciar Test",
    bg="#ffaa00",
    fg="black",
    font=("Helvetica", 12, "bold"),
    command=reiniciar_test,
    relief="raised",
    bd=3,
    activebackground="#ffcc66"
)
boton_reiniciar.pack_forget()  # Se ocultará hasta que termine el test


# Iniciar la primera pregunta
pregunta_label.config(text=preguntas[indice_pregunta])

ventana.mainloop()
