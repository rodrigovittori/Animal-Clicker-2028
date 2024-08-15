#pgzero

"""
M6.L3: Actividad #7 (Extra) - "Superbonificación"
Objetivo: Agregar un tercer bonus

PACK DE ASSETS: 
ANIMALES: https://kenney.nl/assets/animal-pack-redux 
BOTONES:  https://kenney.nl/assets/ui-pack
"""

WIDTH = 600  # Ancho de la ventana
HEIGHT = 400 # Altura de la ventana

TITLE = "Animal Clicker" # Título de la ventana de juego
FPS = 30 # Fotogramas por segundo

# VARIABLES
puntuacion = 0
click_mult = 1 # multiplicador del valor por click
modo_actual = "menu"

#OBJETOS
fondo = Actor("background")
animal = Actor("giraffe", (150, 250))

bonus_1 = Actor("bonus", (450, 100))
bonus_2 = Actor("bonus", (450, 200))
bonus_3 = Actor("bonus", (450, 300))

boton_jugar = Actor("play", (300, 100))

""" #####################
   # FUNCIONES PROPIAS #
  ##################### """

def el_bonus_1():
    global puntuacion
    puntuacion += 1

def el_bonus_2():
    global puntuacion
    puntuacion += 15

def el_bonus_3():
    global puntuacion
    puntuacion += 50

""" ####################
   # FUNCIONES PGZERO #
  #################### """

def draw():

    if (modo_actual == "menu"):
        fondo.draw()
        boton_jugar.draw()
        
    elif (modo_actual == "juego"):
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

        bonus_3.draw()
        screen.draw.text("+50 ☻ cada 2 seg", center = (450, 280), color = "black", fontsize = 20)
        screen.draw.text("PRECIO: 600 ☻", center = (450, 310), color = "black", fontsize = 20)
    
def on_mouse_down(button, pos):
    global puntuacion, modo_actual
    
    if ((button == mouse.LEFT) and (modo_actual == "juego")):

        if animal.collidepoint(pos):
            puntuacion += click_mult
            animal.y = 200
            animate(animal, tween="bounce_end", duration = 0.5, y = 250)
        
        elif bonus_1.collidepoint(pos):
            # Si el click fue sobre el botón de bonus # 1:
            if (puntuacion >= 15):
                schedule_interval(el_bonus_1, 2)
                puntuacion -= 15
                
        elif bonus_2.collidepoint(pos):
            # Si el click fue sobre el botón de bonus # 2:
            if (puntuacion >= 200):
                schedule_interval(el_bonus_2, 2)
                puntuacion -= 200
                
        elif bonus_3.collidepoint(pos):
            # Si el click fue sobre el botón de bonus # 3:
            if (puntuacion >= 600):
                schedule_interval(el_bonus_3, 2)
                puntuacion -= 600

    elif ((button == mouse.LEFT) and (modo_actual == "menu")):
         if boton_jugar.collidepoint(pos):
             # Si el click fue sobre el boton "Jugar":
            modo_actual = "juego"

######################

def on_key_down(key):
    global puntuacion, modo_actual
    
    if keyboard.d:
        puntuacion += 500
        
    if keyboard.a:
        puntuacion = 0

    if keyboard.q:
        modo_actual = "menu"





