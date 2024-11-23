
import pygame

class Button:


    def __init__(self, x, y, width, height, text):
        self.position = pygame.Vector2(x,y)
        self.width = width
        self.height = height
        self.text = text
        self.onClick = None

    def draw(self, screen, font):
        r = [self.position.x, self.position.y, self.width, self.height]
        t = font.render(self.text, False, "white", "black")

        pygame.draw.rect(screen, "black", r)
        pygame.draw.rect(screen, "white", r, 2)

        tp = pygame.Vector2((self.width - t.get_width()) / 2, 
                (self.height - t.get_height()) / 2)

        screen.blit(t, (self.position.x + tp.x, self.position.y + tp.y))  


    def update(self, dt, events):
        for ev in events:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                p = pygame.mouse.get_pos()

                # Todo - Rect Collision Check instead?
                if (self.position.x <= p[0] <= self.position.x + self.width \
                        and self.position.y <= p[1] <= self.position.y + self.height):
                    if (self.onClick != None):
                        self.onClick()


        
