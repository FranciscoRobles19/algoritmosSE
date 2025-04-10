class Nodo:
    def __init__(self, pregunta=None, si=None, no=None, conclusion=None):
        self.pregunta = pregunta  # Pregunta para decidir
        self.si = si  # Rama si la respuesta es sí
        self.no = no  # Rama si la respuesta es no
        self.conclusion = conclusion  # Conclusión en caso de ser hoja

def dfs(nodo):
    if nodo is None:
        return None
    
    if nodo.conclusion is not None:
        print(f"Recomendación: {nodo.conclusion}")
        return nodo.conclusion
    
    respuesta = input(nodo.pregunta + " (si/no): ").strip().lower()
    if respuesta == "si":
        return dfs(nodo.si)
    else:
        return dfs(nodo.no)

# Construcción del árbol de decisión
nodo6 = Nodo(conclusion="Usa una bicicleta.")
nodo7 = Nodo(conclusion="Toma un taxi o un servicio de transporte privado.")
nodo8 = Nodo(conclusion="Usa transporte público como bus o metro.")
nodo9 = Nodo(conclusion="Camina hasta tu destino.")

nodo4 = Nodo("¿Hay transporte público disponible?", si=nodo8, no=nodo7)
nodo5 = Nodo("¿La distancia es mayor a 5 km?", si=nodo4, no=nodo6)
nodo2 = Nodo("¿Tienes prisa?", si=nodo5, no=nodo9)
nodo3 = Nodo("¿Tu destino está a menos de 2 km?", si=nodo9, no=nodo2)
nodo1 = Nodo("¿Dispones de un medio de transporte propio?", si=nodo6, no=nodo3)

# Iniciar sistema experto
print("Sistema Experto de Recomendación de Transporte")
dfs(nodo1)
