import sys
import pygame
from pygame.locals import QUIT
from math import sin,cos,radians

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255,255,255))

        pointlist0,pointlist1 = [],[]
        for theta in range(0,720,144):
            rad = radians(theta)
            pointlist0.append((cos(rad)*100+100,sin(rad)*100+150))
            pointlist1.append((cos(rad)*100+300,sin(rad)*100+150))

        pygame.draw.lines(SURFACE,(0,0,255),True,pointlist0,5)
        pygame.draw.lines(SURFACE,(0,255,0),True,pointlist1,5)
        #print(pointlist0)

        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == "__main__":
    main()