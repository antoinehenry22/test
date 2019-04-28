
import pygame
from pygame.locals import *
  
pygame.init()
dim_x=320
dim_y=240
fenetre = pygame.display.set_mode((dim_x, dim_y))
  
fond = pygame.image.load("background.jpg").convert()
  
perso = pygame.image.load("perso.png").convert_alpha()
position_perso = [0,0]
size = perso.get_size()[1]
v=10 #définis la vitesse du perso. plus V est élevé, plus il va lentement
speed=(size/v)#définis la vitesse en fonction de la taille du perso
continuer = 1
pygame.key.set_repeat(400, 30)
x=0
y=0
n=1
m=1
while continuer:
    for event in pygame.event.get():  
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_UP:   #Si "flèche haut"
                #On monte le perso
                position_perso[1] -= speed
            if event.key == K_DOWN: #Si "flèche bas"
                #On descend le perso
                if m==2 and dim_y-11*speed<position_perso[0]< dim_y+11*speed :
                    position_perso[1]=dim_y-10*speed
                else :
                    if dim_y-speed<position_perso[0]< dim_y+speed :
                        y=-dim_y*m
                        m=m+1
                        position_perso[1]=0-speed
                    else :
                        position_perso[1] += speed
            if event.key == K_LEFT: #Si "flèche gauche"
                #On bouge le perso a gauche
                if 0-speed<position_perso[0]< 0+speed :
                    if x==0 and position_perso==0:
                        position_perso[0] = 0
                    else :
                        n=n-1
                        if n==0 :
                            position_perso[0] = 0
                            n=1
                        else:
                            x=+dim_x*(n-1)
                            position_perso[0]=dim_x
                else : 
                    position_perso[0] -= speed


            if event.key == K_RIGHT:    #Si "flèche droite"
                #On bouge le perso a droite
                if n==2 and dim_x-11*speed<position_perso[0]< dim_x+11*speed :
                    position_perso[0]=dim_x-10*speed
                else :
                    if dim_x-speed<position_perso[0]< dim_x+speed :
                        x=-dim_x*n
                        n=n+1
                        position_perso[0]=0-speed
                    else :
                        position_perso[0] += speed




              
    #Re-collage
    fenetre.blit(fond, (x,y)) 
    fenetre.blit(perso, tuple(position_perso))
    #Rafraichissement
    pygame.display.flip()
 
pygame.quit()