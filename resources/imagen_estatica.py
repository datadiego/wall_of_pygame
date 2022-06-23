from . import *
randint = random.randint

class Imagen_estatica:
    def __init__(self, pantalla, x, y, nombre_imagen):
        self.pantalla = pantalla
        self.nombre_img = nombre_imagen
        self.img = pg.image.load(os.path.join("resources", "img", self.nombre_img))
        self.x = x
        self.y = y
    
    def mostrar(self):
        self.pantalla.blit(self.img, (self.x, self.y))