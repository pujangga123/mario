# inisialisasi
import pygame
from mario import Mario
from world import World


def run_game():
    pygame.init()
    screen = pygame.display.set_mode([700,500])
    clock = pygame.time.Clock()

    mario = Mario(screen)
    world = World(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False            
                if event.key == pygame.K_SPACE:
                    mario.jump(11)
                if event.key == pygame.K_x:
                    fire = Fire(screen,mario)

            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if mario.condition!='die':
            if keys[pygame.K_LEFT]:
                mario.move_left()
            elif keys[pygame.K_RIGHT]:
                mario.move_right(True)
            else:
                if mario.condition != 'jump':
                    mario.stand()

        mario.gravity()
        world.draw()
        mario.draw()
        
        pygame.display.flip()
        clock.tick(18)
    exit_game()

def exit_game():
    sys.exit()

if __name__ == "__main__":
    run_game()

