import sqlite3

def crear_base_datos():
    conexion = sqlite3.connect("mobs.db")
    cursor = conexion.cursor()

    # Crear tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            imagen TEXT,
            hostil INTEGER,       
            neutral INTEGER,  
            montar INTEGER,
            overworld INTEGER,     
            nether INTEGER,
            aldea INTEGER,      
            end INTEGER, 
            vuela INTEGER,
            acuatico INTEGER,
            domesticar INTEGER,
            death INTEGER,
            boss INTEGER,
            bipedo INTEGER,
            fortaleza INTEGER,
            drops INTEGER,       
            cuero INTEGER
        )
    ''')

    # Borrar datos anteriores
    cursor.execute('DELETE FROM mobs')

    # Insertar nuevos datos
    mobs = [
    ("aldeano", "aldeano.png", 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
    ("caballo", "caballo.png", 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1),
    ("caballo esqueleto", "caballo_esqueleto.png", 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0),
    ("cerdo", "cerdo.png", 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0),
    ("oveja", "oveja.png", 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0),
    ("vaca", "vaca.png", 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1),
    ("pollo", "pollo.png", 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0),
    ("abeja", "abeja.png", 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ("araña", "araña.png", 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
    ("murcielago", "murcielago.png", 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0),
    ("golem de hierro", "golem_de_hierro.png", 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0),
    ("lobo", "lobo.png", 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
    ("oso polar", "oso_polar.png", 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    ("panda", "panda.png", 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
    ("slime", "slime.png", 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
    ("zombie", "zombie.png", 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0),
    ("bruja", "bruja.png", 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0),
    ("creeper", "creeper.png", 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
    ("saqueador", "saqueador.png", 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0),
    ("esqueleto", "esqueleto.png", 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0),
    ("fantasma", "fantasma.png", 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0),
    ("esqueleto glacial", "esqueleto_glacial.png", 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0),
    ("calamar", "calamar.png", 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0),
    ("delfin", "delfin.png", 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
    ("ahogado", "ahogado.png", 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0),
    ("guardian", "guardian.png", 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0),
    ("cubo de magma", "cubo_de_magma.png", 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
    ("lavagante", "lavagante.png", 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    ("blaze", "blaze.png", 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0),
    ("esqueleto del wither", "esqueleto_del_wither.png", 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0),
    ("piglin", "piglin.png", 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0),
    ("ghast", "ghast.png", 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0),
    ("hoglin", "hoglin.png", 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
    ("shulker", "shulker.png", 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0),
    ("enderman", "enderman.png", 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0),
    ("warden", "warden.png", 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0),
    ("enderdragon", "enderdragon.png", 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0),
    ("wither", "wither.png", 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0),
    ("guardian anciano", "guardian_anciano.png", 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0)
]


    cursor.executemany('''
        INSERT INTO mobs (nombre, imagen, hostil, neutral, montar, overworld, nether, aldea, end, vuela, acuatico, domesticar, death, boss, bipedo, fortaleza, drops, cuero)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', mobs)

    conexion.commit()
    conexion.close()
    print("Base de datos limpiada y actualizada.")

if __name__ == "__main__":
    crear_base_datos()
