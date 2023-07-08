# Mario Game 1
# The program is focus on making a "confortable" character movement
# includes: Mario walk and jump

# inisialisasi
import sys
import pygame
from mario import *
from world import World

# clock tick
GAME_SPEED = 15

def run_game():
    n = 0
    pygame.init()
    screen = pygame.display.set_mode([700,500])
    clock = pygame.time.Clock()

    mario = Mario()
    world = World(screen)
    screen.blit(mario.ani_walk.imgs[0], (10,  10))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False            
                if event.key == pygame.K_SPACE and mario.state!=STATE_JUMP :
                    mario.jump()

            if event.type == pygame.QUIT:
                running = False

        # key pressed event
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            mario.move_left()
        elif keys[pygame.K_RIGHT]:
            mario.move_right(True)
        else: # STAND
            if mario.state != STATE_JUMP:
                mario.stand()

        mario.gravity()
        world.draw()
        
        img = mario.load_img()
        screen.blit(img, (mario.x, mario.y - img.get_height()))

        pygame.display.flip()
        clock.tick(GAME_SPEED)
    exit_game()

def exit_game():
    sys.exit()

if __name__ == "__main__":
    run_game()

