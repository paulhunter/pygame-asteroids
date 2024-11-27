
import pygame

class Button:


    def __init__(self, x, y, width, height, text):
        self.position = pygame.Vector2(x,y)
        self.width = width
        self.height = height
        self.text = text
        self.onClick = None

        self.__hover = False
        self.__rect = pygame.Rect(  self.position.x,
                                    self.position.y,
                                    self.width,
                                    self.height)


    def draw(self, screen, font):
        t = font.render(self.text, False, "white")

        pygame.draw.rect(screen, (30,30,30) if self.__hover else "black", self.__rect)
        pygame.draw.rect(screen, "white", self.__rect, 2)

        t_offset = pygame.Vector2((self.width - t.get_width()) / 2,
                (self.height - t.get_height()) / 2)

        screen.blit(t, (self.position.x + t_offset.x,
                        self.position.y + t_offset.y))


    def update(self, dt, events):
        for ev in events:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if (self.onClick != None
                        and self.__rect.collidepoint(ev.pos)
                        and ev.button == 1):
                    self.onClick()




        
