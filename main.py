import random
import tkinter as tk
from tkinter import ttk, messagebox

# Configuración del juego (sin emojis)
personajes = {
    1: {"nombre": "Dr. Black", "profesion": "Médico forense"},
    2: {"nombre": "Profesora Plum", "profesion": "Catedrática"},
    3: {"nombre": "Coronel Mustard", "profesion": "Militar"},
    4: {"nombre": "Señorita Scarlet", "profesion": "Empresaria"},
    5: {"nombre": "Reverendo Green", "profesion": "Clérigo"}
}

locaciones = {
    1: {"nombre": "Biblioteca"},
    2: {"nombre": "Cocina"},
    3: {"nombre": "Jardín de invierno"},
    4: {"nombre": "Sala de billar"},
    5: {"nombre": "Dormitorio principal"}
}

armas = {
    1: {"nombre": "Candelabro"},
    2: {"nombre": "Cuchillo"},
    3: {"nombre": "Pistola"},
    4: {"nombre": "Tubería de plomo"},
    5: {"nombre": "Cuerda"}
}

# Grafo simple de las locaciones
grafo_locaciones = {
    "Biblioteca": ["Cocina", "Sala de billar"],
    "Cocina": ["Biblioteca", "Jardín de invierno"],
    "Jardín de invierno": ["Cocina", "Dormitorio principal"],
    "Sala de billar": ["Biblioteca", "Dormitorio principal"],
    "Dormitorio principal": ["Jardín de invierno", "Sala de billar"]
}


class ClueGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Misterio en la Mansión Boddy")
        self.root.geometry("700x800")
        
        # Solución aleatoria
        self.culpable = random.choice(list(personajes.values()))
        self.locacion = random.choice(list(locaciones.values()))
        self.arma = random.choice(list(armas.values()))
        
        self.crear_interfaz()
        self.mostrar_historia()
    
    def encontrar_camino(self, origen, destino):
        visitados = set()
        cola = [(origen, [origen])]
        while cola:
            actual, camino = cola.pop(0)
            if actual == destino:
                return camino
            visitados.add(actual)
            for vecino in grafo_locaciones.get(actual, []):
                if vecino not in visitados:
                    cola.append((vecino, camino + [vecino]))
        return None

    def crear_interfaz(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.historia_label = ttk.Label(
            main_frame, 
            text="", 
            wraplength=600,
            font=('Helvetica', 10),
            justify=tk.CENTER
        )
        self.historia_label.pack(pady=10)
        
        ttk.Separator(main_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        
        acusacion_frame = ttk.LabelFrame(main_frame, text="Haz tu acusación", padding=10)
        acusacion_frame.pack(fill=tk.X, pady=5)
        
                # Botón para mostrar grafo
        ttk.Button(
            main_frame,
            text="Mostrar Mapa de Locaciones",
            command=self.mostrar_grafo
        ).pack(pady=10)



        # Personaje
        ttk.Label(acusacion_frame, text="Personaje:").grid(row=0, column=0, sticky=tk.W)
        self.personaje_var = tk.StringVar()
        personaje_combobox = ttk.Combobox(
            acusacion_frame, 
            textvariable=self.personaje_var,
            values=[f"{p['nombre']} ({p['profesion']})" for p in personajes.values()],
            state="readonly"
        )
        personaje_combobox.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=2)
        
        # Locación
        ttk.Label(acusacion_frame, text="Locación:").grid(row=1, column=0, sticky=tk.W)
        self.locacion_var = tk.StringVar()
        locacion_combobox = ttk.Combobox(
            acusacion_frame, 
            textvariable=self.locacion_var,
            values=[l['nombre'] for l in locaciones.values()],
            state="readonly"
        )
        locacion_combobox.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=2)
        
        # Arma
        ttk.Label(acusacion_frame, text="Arma:").grid(row=2, column=0, sticky=tk.W)
        self.arma_var = tk.StringVar()
        arma_combobox = ttk.Combobox(
            acusacion_frame, 
            textvariable=self.arma_var,
            values=[a['nombre'] for a in armas.values()],
            state="readonly"
        )
        arma_combobox.grid(row=2, column=1, sticky=tk.EW, padx=5, pady=2)
        
        # Botón resolver
        ttk.Button(
            acusacion_frame, 
            text="¡Resolver Misterio!", 
            command=self.resolver_misterio
        ).grid(row=3, column=0, columnspan=2, pady=10)
        
        self.pistas_frame = ttk.LabelFrame(main_frame, text="Pistas Visuales", padding=10)
        self.pistas_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.actualizar_pistas()
    
    def mostrar_historia(self):
        camino = self.encontrar_camino("Biblioteca", self.locacion["nombre"])
        if camino:
            texto_camino = " -> ".join(camino)
            historia = f"Ruta desde Biblioteca hasta la escena del crimen:\n{texto_camino}\n\n"
        else:
            historia = ""
        historias = [
            f"El magnate Mr. Boddy ha sido encontrado muerto en su mansión. {self.culpable['nombre']} fue visto por última vez cerca de {self.locacion['nombre']}.",
            f"Durante una cena en la mansión, se cortó la luz. Al restaurarse, Mr. Boddy estaba muerto. {self.culpable['nombre']} actuaba sospechosamente.",
            f"La fiesta de gala terminó en tragedia. {self.culpable['nombre']} salió abruptamente hacia {self.locacion['nombre']}.",
            f"El mayordomo encontró el cuerpo en {self.locacion['nombre']}. {self.culpable['nombre']} estaba interesado en {self.arma['nombre']}.",
            f"Una llamada anónima alertó a la policía. Al llegar, encontraron a {self.culpable['nombre']} en {self.locacion['nombre']} con {self.arma['nombre']}."
        ]
        self.historia_label.config(text=historia + random.choice(historias))
    
    def actualizar_pistas(self):
        for widget in self.pistas_frame.winfo_children():
            widget.destroy()
        
        pista_texto = "ESCENA DEL CRIMEN\n\n"
        pista_texto += "Personajes presentes:\n"
        for p in personajes.values():
            pista_texto += f"- {p['nombre']}\n"
        pista_texto += "\nArmas encontradas:\n"
        for a in armas.values():
            pista_texto += f"- {a['nombre']}\n"
        pista_texto += "\nLugares clave:\n"
        for l in locaciones.values():
            pista_texto += f"- {l['nombre']}\n"
        
        pista_label = ttk.Label(
            self.pistas_frame, 
            text=pista_texto,
            font=('Courier', 10),
            justify=tk.LEFT
        )
        pista_label.pack(anchor=tk.W)
    




    def mostrar_grafo(self):
        # Nueva ventana
        ventana_grafo = tk.Toplevel(self.root)
        ventana_grafo.title("Mapa de Locaciones")

        canvas = tk.Canvas(ventana_grafo, width=500, height=400, bg="white")
        canvas.pack()

        # Posiciones fijas para las locaciones (puedes ajustar si lo deseas)
        posiciones = {
            "Biblioteca": (100, 100),
            "Cocina": (200, 200),
            "Jardín de invierno": (300, 300),
            "Sala de billar": (300, 100),
            "Dormitorio principal": (400, 200)
        }

        # Dibujar conexiones (aristas)
        for origen, vecinos in grafo_locaciones.items():
            x1, y1 = posiciones[origen]
            for destino in vecinos:
                x2, y2 = posiciones[destino]
                canvas.create_line(x1, y1, x2, y2, fill="gray", width=2)

        # Dibujar nodos (locaciones)
        for nombre, (x, y) in posiciones.items():
            canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue")
            canvas.create_text(x, y, text=nombre, font=("Arial", 8), justify=tk.CENTER)






    
    def resolver_misterio(self):
        selec_personaje = self.personaje_var.get()
        selec_locacion = self.locacion_var.get()
        selec_arma = self.arma_var.get()
        
        if not all([selec_personaje, selec_locacion, selec_arma]):
            messagebox.showwarning("Advertencia", "¡Debes seleccionar personaje, locación y arma!")
            return
        
        nombre_personaje = selec_personaje.split('(')[0].strip()
        nombre_locacion = selec_locacion.strip()
        nombre_arma = selec_arma.strip()
        
        if (nombre_personaje == self.culpable['nombre'] and 
            nombre_locacion == self.locacion['nombre'] and 
            nombre_arma == self.arma['nombre']):
            mensaje = f"✅ ¡Correcto!\n\n{self.culpable['nombre']} cometió el asesinato en {self.locacion['nombre']} con {self.arma['nombre']}.\n\n¡Has resuelto el misterio!"
            messagebox.showinfo("¡Misterio Resuelto!", mensaje)
        else:
            mensaje = f"❌ ¡Incorrecto!\n\nLa solución era:\n\n{self.culpable['nombre']} en {self.locacion['nombre']} con {self.arma['nombre']}.\n\n¡Sigue investigando!"
            messagebox.showerror("Solución Incorrecta", mensaje)


# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = ClueGame(root)
    root.mainloop()
