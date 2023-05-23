import random
import sys
import pygame
import pygame.freetype

pygame.init()
font = pygame.font.SysFont('Chango-Regular.ttf', 45)
pygame.key.set_repeat(1)

pygame.freetype.init()
myfont = pygame.freetype.SysFont(None, 20)

width, height = 1500, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("DodgeBoules")

clock = pygame.time.Clock()

BLANC = (255, 255, 255)
RED = (255, 0, 0)
NOIR = (0, 0, 0)
RAYON_BOULE = 10
XMIN, YMIN = 0, 0
XMAX, YMAX = width, height

#rejouer = pygame.image.load("rejouer.png")


# fenetre.blit(rejouer, (1065, 540))

class Boule:
    def __init__(self):
        tableau = [-7, -6, -5, 5, 6, 7, 15]
        tableau2 = [(255, 255, 255), (255, 0, 0), (125, 45, 255), (0, 255, 0), (255, 0, 255), (255, 255, 0),
                    (0, 255, 255)]

        self.posX = 400
        self.posY = random.randint(300, 400)
        self.vitX = random.choice(tableau)
        self.vitY = random.choice(tableau)
        self.col = random.choice(tableau2)

    def deplacer_boule(self, r1):
        global bouclle

        if (self.posX < r1.posxhaut + r1.poslargeur + 5 and self.posY > r1.posyhaut and
                self.posY < r1.posyhaut + r1.poslongueur and self.posX > r1.posxhaut - 5
                and self.posY > r1.posyhaut and self.posY < r1.posyhaut +
                r1.poslongueur):
            # si la balle entre en collision avec la raquette r1 ou r2
            self.vitX = -self.vitX
            self.vitY = random.randint(-5, 5)

            screen.fill(RED)
            bouclle = False

        if (self.posY < 5 or self.posY > 795):
            self.vitY = -self.vitY
        if (self.posX < 5 or self.posX > 1495):
            self.vitX = -self.vitX

        self.posX = self.posX + self.vitX
        self.posY = self.posY + self.vitY

    def afficher_boule(self):

        pygame.draw.rect(screen, self.col,
                         (int(self.posX - RAYON_BOULE), int(self.posY - RAYON_BOULE),
                          2 * RAYON_BOULE, 2 * RAYON_BOULE), 0)


class Carre:
    def __init__(self, xhaut, yhaut, longueur, largeur, touche_up, touche_down, touche_left, touche_right):

        self.posxhaut = xhaut
        self.posyhaut = yhaut
        self.poslongueur = longueur
        self.poslargeur = largeur
        self.up = touche_up
        self.down = touche_down
        self.left = touche_left
        self.right = touche_right

    def afficher_carre(self):

        pygame.draw.rect(screen, RED, (self.posxhaut, self.posyhaut, self.poslargeur, self.poslongueur))

    def deplacer_carre(self):

        if event.type == pygame.KEYDOWN:

            if event.key == self.up:
                self.posyhaut = self.posyhaut - 1

            if event.key == self.down:
                self.posyhaut = self.posyhaut + 1
            if event.key == self.left:
                self.posxhaut = self.posxhaut - 1

            if event.key == self.right:
                self.posxhaut = self.posxhaut + 1

            if (self.posyhaut < 0):
                self.posyhaut = self.posyhaut + 5
            if (self.posyhaut > 770):
                self.posyhaut = self.posyhaut - 5
            if (self.posxhaut < 0):
                self.posxhaut = self.posxhaut + 5
            if (self.posxhaut > 1470):
                self.posxhaut = self.posxhaut - 5


def score(nbre_boules):
    score1 = "Score :" + str(len(nbre_boules))
    textsurface = font.render(score1, False, BLANC)
    screen.blit(textsurface, (0, 0))
    print(str(len(nbre_boules)))


tboule = [Boule()]

carre1 = Carre(300, 300, 30, 30, pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d)

i = 0
bouclle = True
while bouclle == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        carre1.deplacer_carre()

    screen.fill(NOIR)
    carre1.afficher_carre()
    for a in range(0, len(tboule)):
        tboule[a].deplacer_boule(carre1)
        tboule[a].afficher_boule()

    # print(i)
    if i == 200:
        tboule.append(Boule())

        i = 0

    i = i + 1

    score(tboule)

    pygame.display.flip()
    clock.tick(60)
