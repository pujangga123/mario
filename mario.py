import pygame
from animate import Animation

DIRECT_LEFT = 0
DIRECT_RIGHT = 1

STATE_STAND = 0
STATE_JUMP = 1
STATE_WALK = 2

SPEED = 10

class Mario:
    x = 10
    y = 550 # use bottom of object as reference

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
    state = STATE_STAND # stand/walk/jump

    def __init__(self):
        self.ani_stand = Animation(['images/mario-stand.png'])
        self.ani_walk = Animation([
            'images/mario-walk-1.png',
            'images/mario-walk-2.png',
            'images/mario-walk-3.png', 
            'images/mario-walk-2.png',
        ])
        self.ani_jump = Animation(['images/mario-jump.png'])

        self.img_die = pygame.image.load('images/mario6.png')
        self.sound_jump = pygame.mixer.Sound('sound/mario-jump1.wav')
        self.sound_die = pygame.mixer.Sound('sound/mario-die.wav')

    def load_img(self): # gambar mario
        img = None
        if self.state == STATE_STAND:
            #img = self.img_stand
            img = self.ani_stand.img
        if self.state == STATE_WALK:
            print('walk')            
            img = self.ani_walk.img
        if self.state == STATE_JUMP:
            img = self.ani_jump.img
        if self.direct == DIRECT_LEFT: #kalau mario sedang menghadap ke kiri, FLIP gambar
            img = pygame.transform.flip(img,True,False)

        return img

    def move_left(self):  # move to the left
        self.x -= SPEED
        self.direct = DIRECT_LEFT
        if self.state != STATE_JUMP:
            self.ani_walk.animate()
            self.state = STATE_WALK
    
    # move_char used when world side scrolling is implemented
    def move_right(self, move_char = True):  # move to the right 
        if move_char: # bergerak ke kanan tapi hanya jika move_char False
            self.x += SPEED

        self.direct = DIRECT_RIGHT
        if self.state != STATE_JUMP:
            self.ani_walk.animate()
            self.state = STATE_WALK

    def stand(self):
        self.state = STATE_STAND
        self.ani_walk.reset()
    
    def die(self):
        pass

    def gravity(self):  # gerakan jatuh
        if self.jump_height>0:
            self.y -= 15
            self.jump_height -= 1
        elif self.y<self.ground:
            self.y += 15
        else:
            self.y=self.ground
            if self.state ==  STATE_JUMP:
                self.state = STATE_STAND     

    def jump(self,height=11): # lompat
        if self.state!=STATE_JUMP:
            self.state = STATE_JUMP
            self.jump_height = height
            self.sound_jump.play()


