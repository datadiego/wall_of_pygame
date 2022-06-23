from . import *
randint = random.randint




class Emoji:
    def __init__(self, pantalla):
        self.vel_x = randint(-3,3)
        self.vel_y = randint(3,3)
        self.pantalla = pantalla
        self.img = pg.image.load(os.path.join("resources", "img", "emoji1.png"))
        self.img = pg.transform.smoothscale(self.img, (40, 40))
        self.img2 = pg.image.load(os.path.join("resources", "img", "emoji2.png"))
        self.img2 = pg.transform.smoothscale(self.img2, (40, 40))
        self.imgs = [self.img, self.img2]
        self.current_img = self.imgs[0]
        self.x = (WIDTH - self.img.get_width())/2
        self.y = 200
    def reset(self):
        self.x = (WIDTH - self.img.get_width())/2
        self.y = 200 
    def check_border(self):
        if self.x < 0:
            self.next_emoji()
            self.vel_x = -self.vel_x
        if self.x > WIDTH-self.img.get_width():
            self.next_emoji()
            self.vel_x = -self.vel_x
        if self.y < 0:
            self.next_emoji()
            self.vel_y = -self.vel_y
        if self.y > HEIGHT -self.img.get_height():
            self.next_emoji()
            self.vel_y = -self.vel_y
    def next_emoji(self):
        index = self.imgs.index(self.current_img)
        if index >= len(self.imgs)-1:
            self.current_img = self.imgs[0]
        else:
            self.current_img = self.imgs[index+1]

    def mover(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.check_border()

    def muestra(self):
        self.pantalla.blit(self.current_img,(self.x, self.y))