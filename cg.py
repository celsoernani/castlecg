import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *    

##desenhando o castelo
vertices=(
    # Plano 0
    # Quadrado central
    (-1,0,0),
    (2,0,0),
    (2,2,0),
    (-1,2,0),
    # Porta
    (0,0,0),
    (1,0,0),
    (1,1,0),
    (0,1,0),
    # Retangulo lateral esquerda
    (-2,0,0),
    (-1,0,0),
    (-1,3,0),
    (-2,3,0),
    # Retangulo lateral direita
    (2,0,0),
    (3,0,0),
    (3,3,0),
    (2,3,0),
    #----------------------------------------
    # Plano -1
    # Quadrado central
    (-1,0,-1),
    (2,0,-1),
    (2,2,-1),
    (-1,2,-1),
    # Retangulo lateral esquerda
    (-2,0,-1),
    (-1,0,-1),
    (-1,3,-1),
    (-2,3,-1),
    # Retangulo lateral direita
    (2,0,-1),
    (3,0,-1),
    (3,3,-1),
    (2,3,-1),
    
    # Frente
    # Detalhe da parte superior
    # Quadrado 01
    (-2,3,0),
    (-1.6,3,0),
    (-1.6,3.4,0),
    (-2,3.4,0),
    # Quadrado 02
    (-1.4,3,0),
    (-1,3,0),
    (-1,3.4,0),
    (-1.4,3.4,0),
    # Quadrado 03
    (2,3,0),
    (2.4,3,0),
    (2.4,3.4,0),
    (2,3.4,0),
    # Quadrado 04
    (2.6,3,0),
    (3,3,0),
    (3,3.4,0),
    (2.6,3.4,0),

    # Costas
    # Detalhe da parte superior
    # Quadrado 01
    (-2,3,-1),
    (-1.6,3,-1),
    (-1.6,3.4,-1),
    (-2,3.4,-1),
    # Quadrado 02
    (-1.4,3,-1),
    (-1,3,-1),
    (-1,3.4,-1),
    (-1.4,3.4,-1),
    # Quadrado 03
    (2,3,-1),
    (2.4,3,-1),
    (2.4,3.4,-1),
    (2,3.4,-1),
    # Quadrado 04
    (2.6,3,-1),
    (3,3,-1),
    (3,3.4,-1),
    (2.6,3.4,-1),

    )

edges = (
    # Plano 0
    # Quadrado central
    (0,1),
    (0,3),
    (1,2),
    (2,3),
    # Porta
    (4,5),
    (4,7),
    (5,6),
    (6,7),
    # Retangulo lateral esquerda
    (8,9),
    (8,11),
    (9,10),
    (10,11),
    # Retangulo lateral direita
    (12,13),
    (12,15),
    (13,14),
    (14,15),

    # Plano -1
    # Quadrado central
    (16,17),
    (16,19),
    (17,18),
    (18,19),
    # Retangulo lateral esquerda
    (20,21),
    (20,23),
    (21,22),
    (22,23),
    # Retangulo lateral direita
    (24,25),
    (24,27),
    (25,26),
    (26,27),

    # Ligações para tornar a figura 3D
    (2,18),
    (3,19),
    (8,20),
    (13,25),
    (11,23),
    (10,22),
    (15,27),
    (14,26),
    
    # Frente
    # Detalhe da parte superior
    # Quadrado 01
    (28,29),
    (28,31),
    (29,30),
    (30,31),
    # Quadrado 02
    (32,33),
    (32,35),
    (33,34),
    (34,35),
    # Quadrado 02
    (36,37),
    (36,39),
    (37,38),
    (38,39),
    # Quadrado 02
    (40,41),
    (40,43),
    (41,42),
    (42,43),

    # Costas
    # Detalhe da parte superior
    # Quadrado 01
    (44,45),
    (44,47),
    (45,46),
    (46,47),
    # Quadrado 02
    (48,49),
    (48,51),
    (49,50),
    (50,51),
    # Quadrado 02
    (52,53),
    (52,55),
    (53,54),
    (54,55),
    # Quadrado 02
    (56,57),
    (56,59),
    (57,58),
    (58,59),
    # Ligações para tornar a figura 3D
    (31,47),
    (30,46),
    (35,51),
    (34,50),
    (39,55),
    (38,54),
    (43,59),
    (42,58),
    
    
)

def Castle():
    glLineWidth(5)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
            glColor3f(0,1,0)
    glEnd()

def Circle(x,y,side,radius):
    posx, posy = x,y    
    sides = side   
    radius = radius   
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

def main():
    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50)

    glTranslatef(0,0,-10)

    clock = pygame.time.Clock()
    while True:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 0, 1, 2)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Castle()
        Circle(-1.5,2,20,0.3)
        Circle(2.5,2,20,0.3)
        pygame.display.flip()


main()
