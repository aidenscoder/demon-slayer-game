import pygame,sys,anim

running = True

def main():
    global running
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Simple Pygame Window")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    anim.lightning_anim.add_pending_draw(400,300,50,50)
        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()  # Update the display
        anim.lightning_anim.update(screen)

    pygame.quit()
    
if __name__ == "__main__":
    sys.exit(int(main()) or 0)