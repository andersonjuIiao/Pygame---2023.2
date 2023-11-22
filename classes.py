import pygame

class Botao(pygame.sprite.Sprite):
    def __init__(self,*groups):
        super().__init__(*groups)
        


        self.image = pygame.image.load("imagem/BotaogameIN.png").convert_alpha()
        self.image = pygame.transform.scale(self.image , [ 190 , 49  ] )
        self.rect = pygame.Rect(190 , 49 , 190 , 49)
        self.rect = self.image.get_rect()

        self.image1 = pygame.image.load("imagem/BotaogameIN.png").convert_alpha()
        self.image2 = pygame.image.load("imagem/BotaogameOUT.png").convert_alpha()


        self.touche = False

    def update(self):
        self.mouse = pygame.mouse.get_pressed()
        self.MousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(self.MousePos):
            
            if self.mouse[0]:
                self.touche = True
                pygame.mouse.get_rel()
                self.image = self.image2
                
            else:
                self.touche = False
                self.image = self.image1

        pass