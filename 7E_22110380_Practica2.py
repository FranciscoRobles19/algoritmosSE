import json
import os

# Archivo donde se guardará la base de conocimiento
ARCHIVO_DB = "base_conocimiento.json"

# Verificar si el archivo existe, si no, crear uno con datos iniciales
if not os.path.exists(ARCHIVO_DB):
    base_conocimiento = {
        "hola": "¡Hola! ¿Cómo estás?",
        "ocupo ayuda con el codigo": "Perfecto! Que tienes pensado hacer y/o proporcioname el codigo",
        "ocupo ayuda con un trbajo": "Perfecto! En que podria ayudarte?"
    }
    with open(ARCHIVO_DB, "w") as file:
        json.dump(base_conocimiento, file, indent=4)
else:
    with open(ARCHIVO_DB, "r") as file:
        try:
            base_conocimiento = json.load(file)
        except json.JSONDecodeError:
            # Si hay un error en el JSON, se reinicia la base de datos
            base_conocimiento = {}
            with open(ARCHIVO_DB, "w") as file:
                json.dump(base_conocimiento, file, indent=4)

def chatbot():
    while True:
        pregunta = input("Tú: ").strip().lower()

        if pregunta in base_conocimiento:
            print("Bot:", base_conocimiento[pregunta])
        else:
            nueva_respuesta = input("No sé qué responder. ¿Cómo debería responder a eso?\n").strip()
            base_conocimiento[pregunta] = nueva_respuesta
            with open(ARCHIVO_DB, "w") as file:
                json.dump(base_conocimiento, file, indent=4)
            print("Bot: ¡Gracias! Ahora lo recordaré.")

if __name__ == "__main__":
    chatbot()
