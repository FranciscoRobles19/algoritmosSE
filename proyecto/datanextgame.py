import sqlite3

def crear_base_datos():
    conexion = sqlite3.connect("nextgame.db")
    cursor = conexion.cursor()

    # Crear tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            decisiones INTEGER,
            accion INTEGER,
            exploracion INTEGER,
            acertijos INTEGER,
            disparos INTEGER,
            estrategia INTEGER,
            construccion INTEGER,
            historia INTEGER,
            deportes INTEGER,
            carreras INTEGER,
            horror INTEGER,
            plataformas INTEGER,
            personalizacion INTEGER,
            fantasia INTEGER,
            libertad INTEGER,
            melee INTEGER,
            habilidad INTEGER,
            simulacion INTEGER,
            offline INTEGER,
            narrativa INTEGER
        )
    ''')

    # Borrar datos anteriores
    cursor.execute('DELETE FROM games')

    # Insertar nuevos datos
    games = [
        ("accion", 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0),
        ("aventura", 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1),
        ("rpg", 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1),
        ("shooter", 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
        ("estrategia", 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
        ("puzzle", 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0),
        ("simulacion", 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0),
        ("deportes", 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
        ("carreras", 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
        ("openworld", 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1)
    ]

    cursor.executemany('''
        INSERT INTO games (nombre, decisiones, accion, exploracion, acertijos, disparos, estrategia, construccion, historia, deportes, carreras, horror, plataformas, personalizacion, fantasia, libertad, melee, habilidad, simulacion, offline, narrativa) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', games)

    conexion.commit()
    conexion.close()
    print("Base de datos limpiada y actualizada.")

if __name__ == "__main__":
    crear_base_datos()
