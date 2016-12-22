import pygame, sys, os, copy, time
from pygame.locals import *
import pygame as py

class Main:

    def __init__(self):
        print('init')
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        self.setup()
        self.sound_effect()

        self.p1 = Player([100,100],2,(255,150,0),self.DISPLAY)
        self.p2 = Player([700,300],0,(0,100,255),self.DISPLAY)


        self.main_loop()





    def setup(self):
        print ("in setup")

        pygame.init()

        self.DISPLAY = pygame.display.set_mode((800,600),0,32)


        self.board = GameBoard()
        self.board.draw(self.DISPLAY)

        self.clock = pygame.time.Clock()




    def main_loop(self):
        print("in main loop")

        while True:
            #60 frames/sec
            self.clock.tick(1000/30)

            pygame.display.update()
            #self.board.draw(self.DISPLAY)
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
            self.control()
            self.p1.update()
            self.p2.update()

    def control(self):

        Key = pygame.key.get_pressed()

        if Key[pygame.K_UP] and self.p1.dir != 2:
            self.p1.dir = 0

        if Key[pygame.K_RIGHT] and self.p1.dir != 3:
            self.p1.dir = 1

        if Key[pygame.K_LEFT] and self.p1.dir != 1:
            self.p1.dir = 3

        if Key[pygame.K_DOWN] and self.p1.dir != 0:
            self.p1.dir = 2

        #p2 move
        if Key[pygame.K_w] and self.p2.dir != 2:
            self.p2.dir = 0

        if Key[pygame.K_d] and self.p2.dir != 3:
            self.p2.dir = 1

        if Key[pygame.K_a] and self.p2.dir != 1:
            self.p2.dir = 3

        if Key[pygame.K_s] and self.p2.dir != 0:
            self.p2.dir = 2

        #move p1
        if self.p1.dir==0:

            self.p1.go_up()
        if self.p1.dir==1:

            self.p1.go_right()
        if self.p1.dir==3:

            self.p1.go_left()
        if self.p1.dir==2:

            self.p1.go_down()
        #p2 move
        if self.p2.dir==0:

            self.p2.go_up()
        if self.p2.dir==1:

            self.p2.go_right()
        if self.p2.dir==3:

            self.p2.go_left()
        if self.p2.dir==2:

            self.p2.go_down()




    def sound_effect(self):
        if pygame.mixer:
            music = os.path.join(self.main_dir, 'Music.wav')
            pygame.mixer.music.load(music)
            pygame.mixer.music.play(-1)


class Player:
    def __init__(self,position,direction,colour,dis) :
        print('initialize player')
        self.lives = 3
        self.pos = position
        self.lastpos = []
        self.pathnum = 0
        self.dir = direction
        self.olddir = copy.deepcopy(self.dir)
        self.col = colour
        self.counter = 0
        self.paths = []

        self.DISPLAY = dis

    def update(self):
        #print("in update")

        #paths
        if len(self.lastpos) != 0:
            self.paths.append(self.lastpos)
        self.lastpos = copy.deepcopy(self.pos)

        self.check_collision()
        self.olddir = copy.deepcopy(self.dir)

        self.draw()

    def draw(self):
        #print("in draw")

        pygame.draw.rect(self.DISPLAY, self.col, (self.pos[0],self.pos[1], 8, 8))
        #print('pos',self.pos)


    def go_left(self):
        #print("in go left")
        self.pos[0] -= 3

    def go_right(self):
        #print("in go right")
        self.pos[0] += 3

    def go_up(self):
        #print("in go up")
        self.pos[1] -= 3

    def go_down(self):
       # print("in go down")
        self.pos[1] += 3


    def check_collision(self):
       # print("in check collision")

        if self.pos[0] <= 10:
            self.pos[0] = 10

        if self.pos[1] <= 10:
            self.pos[1] = 10

        if self.pos[0] >= (800 - 18):
            self.pos[0] = (800 - 18)
        if self.pos[1] >= 489:
            self.pos[1] = 489

        #path collision

        for i in range(len(self.paths)):
           for x in range(8):
               for y in range(8):
                   if self.pos[0] + x == self.paths[i][0]+ x and self.pos[1] + y == self.paths[i][1] + y:
                       self.kill()
                       sys.exit()





    def kill(self):
        print('kill player')
        time.sleep(1)


#Jakob's code
class GameBoard:

    def update(self):
      print("in update")

    def draw(self,dis):
        window = dis
        backround = (0,150,255)
        white = (255,255,255)
        black = (0,0,0)

        # blank game board
        window.fill(white)

        # creates game board border
        pygame.draw.lines(window, backround, False, [(5, 5), (5, 500)], 8)#py.draw.rect(window, backround, (1, 10, 800, 500), 0)
        pygame.draw.lines(window, backround, False, [(5, 5), (795, 5)], 8)
        pygame.draw.lines(window, backround, False, [(793, 5), (793, 500)], 8)
        pygame.draw.lines(window, backround, False, [(793, 500), (5, 500)], 8)

        # hearts image
        # load player 1 hearts
        player_1_heart_1 = pygame.image.load('heart.png')
        player_1_heart_2 = pygame.image.load('heart.png')
        player_1_heart_3 = pygame.image.load('heart.png')

        # display player 2 hearts
        window.blit(player_1_heart_1, (20, 575))
        window.blit(player_1_heart_2, (70, 575))
        window.blit(player_1_heart_3, (120, 575))


        # load player 2 hearts
        player_2_heart_1 = pygame.image.load('heart.png')
        player_2_heart_2 = pygame.image.load('heart.png')
        player_2_heart_3= pygame.image.load('heart.png')

        # display player 2 hearts
        window.blit(player_2_heart_1, (400, 575))
        window.blit(player_2_heart_2, (450, 575))
        window.blit(player_2_heart_3, (500, 575))

        # load font
        myfont = pygame.font.SysFont("arial bold", 30)

        # displays player 1 label
        player1 = myfont.render("Player 1:", 1, black)
        score1 = myfont.render("Score:", 1, black)
        window.blit(score1, (20, 540))
        window.blit(player1, (20, 510))

        # displays player 2 label
        player2 = myfont.render("Player 2:", 1, black)
        score2 = myfont.render("Score:", 1, black)
        window.blit(score2, (400, 540))
        window.blit(player2, (400, 510))

class Path:
    def __init__(self, VorH):
        print('NNJGHJDFYRDUIJGFHJTUJTYDTRSE')
        self.VorH = VorH


    def makepath(self):
        print("in make path")


if __name__ == '__main__': run = Main()


