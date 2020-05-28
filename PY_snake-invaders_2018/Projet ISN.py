import pygame
import sys
import math
import numpy
import random
# from lycee import *
from pygame.locals import*
import random

#initialisation de la bibliothèque Pygame
pygame.init()

# Initialisation de l'horloge
clock=pygame.time.Clock()

#Couleurs
black        = (   0,   0,   0)
white        = ( 255, 255, 255)
red          = ( 255,   0,   0)
blue         = (   0,   0, 255)
green        = (   0, 255,   0)
vert_serpent = (  34, 153,  84)
rouge_pomme  = ( 223,  13,  13)
grey         = ( 180, 180, 180)

#création de la fenetre graphique
fenetre=pygame.display.set_mode((800,600))

#polices des texte
font = pygame.font.Font(None, 80)
font2 = pygame.font.Font(None, 35)
font3 = pygame.font.Font(None, 25)

#textes et leur couleurs
text = font.render("PROJET ISN",1,white)
text2 = font2.render("SNAKE",1,red)
text3 = font2.render("SPACE INVADERS",1,green)
text4 = font3.render("Maceo PREVOST - Aurelien BENARD",1,grey)

# -------CODE SPACE INVADERS---------------------------------------------
# --- Class

class Block(pygame.sprite.Sprite):
    """ Cette class represente le block. """
    def __init__(self, color):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([25, 25])
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def update(self):
        """ Créer le mvt du block. """

        self.rect.x +=10
        if self.rect.x > 780:
            self.rect.y +=25
            self.rect.x -=780



class Player(pygame.sprite.Sprite):
    """ Cette class represente le joueur. """

    def __init__(self):
        """ Créer un representation du joueur."""

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([85, 25])
        self.image.fill(green)
        self.rect = self.image.get_rect()

    def update(self):
        """ Mettre en forme la position et le mvt du joueur. """

        pos = pygame.mouse.get_pos()

        self.rect.x = pos[0]-float(42.5)


class Bullet(pygame.sprite.Sprite):
    """ Cette class represent les bullets . """
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([4, 10])
        self.image.fill(white)

        self.rect = self.image.get_rect()

    def update(self):
        """ bouger les bullets. """
        self.rect.y -= 20


# --- Sprites listes

# C'est une liste de tout les sprite.
all_sprites_list = pygame.sprite.Group()

# Listes des blocks
block_list = pygame.sprite.Group()

# Listes des bullets
bullet_list = pygame.sprite.Group()

# --- Créer les sprites

for i in range(50):
    # Representation des blocks
    block = Block(white)

    # Faire apparaitre les blocks de manière aléatoire
    block.rect.x = random.randrange(780)
    block.rect.y = random.randrange(450)


    # Ajouter les blocks a la liste des objets
    block_list.add(block)
    all_sprites_list.add(block)

# Créer le joueur
player = Player()
player.rect.y = 520
all_sprites_list.add(player)

# ------- fin CODE SPACE INVADERS----------------------------------------




#--------CODE SNAKE------------------------------------------------------



#Données
n_apple = 1
x_apple = 300
y_apple = 290
direction = 0
n_snake = 1
score1 = 0
score2 = [0]
body_x = [390]
body_y = [290]


#Definition de la classe personnage
class snake:


    def __init__(self,x=390 ,y=290):
        self.x = x
        self.y = y

    def snakeDraw (self):
        head = pygame.draw.rect(fenetre, vert_serpent, (self.x, self.y, 10, 10))

        if direction == 0:
            for i in range (1, n_snake):
                pygame.draw.rect(fenetre, vert_serpent,(body_x[len(body_x)-i],body_y[len(body_y)-i], 10, 10))


        if direction == 1:
            for i in range (1, n_snake):
                pygame.draw.rect(fenetre, vert_serpent,(body_x[len(body_x)-i],body_y[len(body_y)-i], 10, 10))


        if direction == 2:
            for i in range (1, n_snake):
                pygame.draw.rect(fenetre, vert_serpent,(body_x[len(body_x)-i],body_y[len(body_y)-i], 10, 10))


        if direction == 3:
            for i in range (1, n_snake):
                pygame.draw.rect(fenetre, vert_serpent,(body_x[len(body_x)-i],body_y[len(body_y)-i], 10, 10))


    def snakeMove (self,direction):
        if direction == 0 :
            self.x -=  10
        if direction == 1 :
            self.y -= 10
        if direction == 2 :
            self.x += 10
        if direction == 3 :
            self.y += 10

Snake = snake()

class apple:
    def __init__(self,x_apple,y_apple):
        self.x_apple=x_apple
        self.y_apple=y_apple

    def appleDraw (self):
        pygame.draw.rect(fenetre, rouge_pomme, (x_apple,y_apple, 10, 10))

pomme = apple(x_apple, y_apple)

#--------fin CODE SNAKE--------------------------------------------------



#Inititalisatio des variables correspondant au 3 fenêtres du jeu
mainloop = True
mainloop1 = False
mainloop2 = False


#Creation d'une surface de la taille de la fenetre
fond=pygame.Surface(fenetre.get_size())
fond.fill(black)
fenetre.blit(fond, (0,0))

clock = pygame.time.Clock()

# ---boucle 0 (menu)---
while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False


        #faire ecire les textes voulut aux emplacements voulut
        fenetre.blit(text, (230, 100))
        fenetre.blit(text2, (115, 350))
        fenetre.blit(text3, (535, 350))
        fenetre.blit(text4, (248, 160))

        # dessins des boutons
        pygame.draw.circle(fenetre,green,(640,470),80,0)
        pygame.draw.circle(fenetre,red,(160,470),80,0)


        #mettre en place les collisions des boutons avec la souris
        if event.type == pygame.MOUSEBUTTONDOWN :

            #zone de collision du bonton de droite
            d=math.sqrt((640-event.pos[0])**2+(470-event.pos[1])**2)
            if d <=100:
                #on ferme la boucle 0 et on ouvre la 1
                mainloop = False
                mainloop1 = True

            #zone de collision du bonton de gauche
            d=math.sqrt((160-event.pos[0])**2+(470-event.pos[1])**2)
            if d <=100:
                #on ferme la boucle 0 et on ouvre la 2
                mainloop = False
                mainloop2 = True


    pygame.display.flip()

    clock.tick(20)







# ---boucle 1 (Space Invaders)---
while  mainloop1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop1 = False

        elif event.type == pygame.MOUSEBUTTONDOWN :
            # Tirer un bullet si je joueur appui sur le bouton de la souris.
            bullet = Bullet()
            # Faire que le bullet soit la ou le joueur est.
            bullet.rect.x = player.rect.x + float(42.5)
            bullet.rect.y = player.rect.y - 10
            # Ajouter les bullets a la liste d'objet
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)

    # --- Game logic

    # Appeller les update de tous les sprites
    all_sprites_list.update()


    # Calculer la mechanique des bullets
    for bullet in bullet_list:


        # Mettre en place les collisions bullets/blocks
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)


        # Pour chaque collision enlever les bullets et le block
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

        # Enlever les bullets si ils partent de l'écran
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)


    #mettre en place le game over
    for block in block_list:
        # Mettre en place les collisions player/blocks
            player_hit_list = pygame.sprite.spritecollide(player, block_list, True)

        # Si un block entre en collision avec le player fermer la fenêtre
            for player in player_hit_list:
                done = True
                pygame.quit()
                sys.exit()


    # --- Dessiner une frame

    # Effacer l'écran (pour qu'on voit le mvt)
    fenetre.fill(black)

    # Dessiner tous les sprites
    all_sprites_list.draw(fenetre)

    # Dessiner le canon
    pygame.draw.rect(fenetre,green,(player.rect.x+float(38.5),player.rect.y-8,10,10))


    pygame.display.flip()


    clock.tick(20)





# ---boucle 2 (Snake)---
while  mainloop2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop2 = False



    fenetre.fill(white)

    pygame.draw.rect(fenetre,black,(0,0,10,600))
    pygame.draw.rect(fenetre,black,(790,0,10,600))
    pygame.draw.rect(fenetre,black,(0,590,800,10))
    pygame.draw.rect(fenetre,black,(0,0,800,10))

    if n_apple < 1:
        x_pomme = random.randint(1, 78)
        x_apple = x_pomme*10
        y_pomme = random.randint(1, 58)
        y_apple = y_pomme*10
        n_apple += 1

    if event.type == KEYDOWN and event.key == K_LEFT:
        direction = 0

    if event.type == KEYDOWN and event.key == K_UP:
        direction = 1

    if event.type == KEYDOWN and event.key == K_RIGHT:
        direction = 2

    if event.type == KEYDOWN and event.key == K_DOWN:
        direction = 3

    body_x.append(Snake.x)
    body_y.append(Snake.y)

    snake.snakeDraw(Snake)
    snake.snakeMove(Snake, direction)
    pomme.appleDraw()

    if x_apple == Snake.x and y_apple == Snake.y :
        n_apple -= 1
        score1 += 1
        score2.append(score1)
        n_snake += 1
    snake.snakeDraw(Snake)

    if Snake.x > 780  or Snake.x < 10:
        mainloop2 = False
    if Snake.y > 580 or Snake.y < 10:
        mainloop2 = False

    for i in range (1, n_snake):
            if Snake.x == (body_x[len(body_x)-i]) and Snake.y == (body_y[len(body_y)-i]):
                    mainloop2= False
    if mainloop2 == False:
        print (score1)

#Rafraichissement de l'ecran*

    pygame.display.flip()
    clock.tick(15)


pygame.quit()
