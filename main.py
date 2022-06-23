import pygame as pg
from resources import emoji

WIDTH = 1080
HEIGHT = 720

class Animacion:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((WIDTH, HEIGHT))
        #Podemos empezar a crear nuestros objetos aqui:

    def bucle(self):
        loop = True
        while loop:
            for evento in pg.event.get():
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_ESCAPE:
                        loop = False   
                if evento.type == pg.QUIT:
                    loop = False
            #Aqui situaremos nuestros objetos y sus metodos
            self.ani()
            pg.display.flip()
    
    def ani(self):
        self.pantalla.fill((220,220,220))
        pass

wall_of_pygame = Animacion()
wall_of_pygame.bucle()
