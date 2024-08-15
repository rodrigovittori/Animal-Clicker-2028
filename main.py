#pgzero

"""
M6.L3: Actividad #3 - "Añadiendo bonificaciones"
Objetivo: Agregar botones de bonus, (sólo dibujarlos)

PACK DE ASSETS: 
ANIMALES: https://kenney.nl/assets/animal-pack-redux 
BOTONES:  https://kenney.nl/assets/ui-pack
"""

WIDTH = 600  # Ancho de la ventana
HEIGHT = 400 # Altura de la ventana

TITLE = "Animal Clicker" # Título de la ventana de juego
FPS = 30 # Fotogramas por segundo

# VARIABLES
puntuacion = 10000
click_mult = 1 # multiplicador del valor por click


#OBJETOS
fondo = Actor("background")
animal = Actor("giraffe", (150, 250))

bonus_1 = Actor("bonus", (450, 100))
bonus_2 = Actor("bonus", (450, 200))
# To-do: Agregar 3er bonus

def draw():
    fondo.draw()
    animal.draw()
    # Dibujamos puntuacion
    # To-do: Agregar control que chequee que el texto no se salga de la pantalla (ajusta vble fontsize) 
    screen.draw.text((str(puntuacion) + "🙃"), center=(150, 70), color="white", fontsize = 96)

    # Dibujamos botones bonus

    bonus_1.draw()
    screen.draw.text("+1 ☻ cada 2 seg", center = (450, 80), color = "black", fontsize = 20)
    screen.draw.text("PRECIO: 15 ☻", center = (450, 110), color = "black", fontsize = 20)
    
    bonus_2.draw()
    screen.draw.text("+15 ☻ cada 2 seg", center = (450, 180), color = "black", fontsize = 20)
    screen.draw.text("PRECIO: 200 ☻", center = (450, 210), color = "black", fontsize = 20)
    
def on_mouse_down(button, pos):
    global puntuacion
    
    if (button == mouse.LEFT):

        if animal.collidepoint(pos):
            puntuacion += click_mult
            animal.y = 200
            animate(animal, tween="bounce_end", duration = 0.5, y = 250)
