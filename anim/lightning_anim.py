import pygame
pygame.init()
main_img = pygame.image.load("images/lightning_anim.png").convert_alpha()
pending_draw = []

def add_pending_draw(x:int, y:int, width:int, height:int):
    global pending_draw, main_img
    to_draw = pygame.transform.scale(main_img, (width, height))
    pending_draw.append((to_draw, x, y, 0))

def update(screen:pygame.Surface):
    global pending_draw
    for i in range(len(pending_draw)):
        img, x, y, life = pending_draw[i]
        img = img.set_alpha(255 - life * 25)
        if life < 10:
            screen.blit(img, (x, y))
        else:
            del pending_draw[i]