from PIL import Image

# Abrir una imagen
imagen = Image.open("imagen.jpg")  # Asegúrate de que "imagen.jpg" exista en el mismo directorio

# Convertir a escala de grises
imagen_gris = imagen.convert("L")

# Mostrar la imagen
imagen_gris.show()

# Guardar la nueva imagen
imagen_gris.save("imagen_gris.jpg")

print("¡Imagen convertida a escala de grises y guardada como 'imagen_gris.jpg'!")