import pygame as pg
from resources import WIDTH, HEIGHT
from resources.emoji import Emoji

class Animacion:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((WIDTH, HEIGHT))
        #Podemos empezar a crear nuestros objetos aqui:
        self.emoji = Emoji(self.pantalla)
        self.clock = pg.time.Clock()
        
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
            self.emoji_ani()

            #Termina nuestro loop
            pg.display.flip()
            self.clock.tick(60)
    
    def emoji_ani(self):
        self.pantalla.fill((220,220,220))
        self.emoji.mover()
        self.emoji.muestra()
        pass

wall_of_pygame = Animacion()
wall_of_pygame.bucle()
