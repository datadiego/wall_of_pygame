import pygame as pg
from resources import WIDTH, HEIGHT
from resources.emoji import Emoji
from resources.imagen_estatica import Imagen_estatica

class Animacion:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((WIDTH, HEIGHT))
        #Podemos empezar a crear nuestros objetos aqui:
        self.emoji = Emoji(self.pantalla)
        self.test = Imagen_estatica(self.pantalla, 200, 200, "emoji3.png")
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
            self.pantalla.fill((220,220,220))
            self.capa_0()
            self.capa_1()
            

            #Termina nuestro loop
            pg.display.flip()
            self.clock.tick(60)
    
    def capa_0(self):
        self.test.mostrar()
        
    def capa_1(self):
        self.emoji.mover()
        self.emoji.muestra()


wall_of_pygame = Animacion()
wall_of_pygame.bucle()
