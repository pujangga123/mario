import pygame
from animate import Animation

DIRECT_LEFT = 0
DIRECT_RIGHT = 1
SPEED = 10

class Mario:
    x = 10
    y = 550 # posisi terhitung dari dasar objek    

    height = 0
    width = 0
    ani_walk = []

    jump_height = 0
    ground = 430

    img = None

    z = 0
    ani_stand = None
    img_jump = None
    img_die = None
    sound_jump = None
    sound_die = None
    screen = None   
    direct = DIRECT_RIGHT  # left / right
    condition = 'stand' # stand/walk/jump

    def __init__(self):
        self.ani_stand = Animation(['images/mario-stand.png'])
        self.ani_walk = Animation([
            'images/mario-walk-1.png',
            'images/mario-walk-2.png',
            'images/mario-walk-3.png', 
            'images/mario-walk-2.png',
        ])

        self.img_jump = pygame.image.load('images/mario4.png')
        self.img_die = pygame.image.load('images/mario6.png')
        self.sound_jump = pygame.mixer.Sound('sound/mario-jump1.wav')
        self.sound_die = pygame.mixer.Sound('sound/mario-die.wav')

    def load_img(self): # gambar mario
        img = None
        if self.condition == 'stand':
            #img = self.img_stand
            img = self.ani_stand.img
        if self.condition == "walk":            
            img = self.ani_walk.img
        if self.condition == 'jump':
            img = self.img_jump
        if self.condition == 'die':
            img = self.img_die
        if self.direct == DIRECT_LEFT: #kalau mario sedang menghadap ke kiri, FLIP gambar
            img = pygame.transform.flip(img,True,False)

        return img

    def move_left(self):  # gerakan ke kiri
        self.x -= SPEED
        self.direct = DIRECT_LEFT
        self.ani_walk.animate()
        if self.condition != 'jump':
            self.condition = 'walk'
    
    def move_right(self, move_char = True):  # bergerak ke kanan 
        if move_char: # bergerak ke kanan tapi hanya jika move_char False
            self.x += SPEED
        self.direct = DIRECT_RIGHT
        self.ani_walk.animate()
        if self.condition != 'jump':
            self.condition = 'walk'

    def stand(self):
        self.condition = 'stand'
        self.ani_walk.reset()
    
    def die(self):
        if self.condition!= 'die':
            self.condition = 'die'
            self.sound_die.play()

    def gravity(self):  # gerakan jatuh
        if self.jump_height>0:
            self.y -= 15
            self.jump_height -= 1
        elif self.y<self.ground:
            self.y += 15
        else:
            self.y=self.ground
            if self.condition ==  "jump":
                self.condition = 'stand'        

    def jump(self,height): # lompat
        if self.condition!='jump':
            self.condition = 'jump'
            self.jump_height = height
            self.sound_jump.play()


