import pygame, sys, os, copy, time
from pygame.locals import *
import pygame as py

class Main:

    def __init__(self):
       # print('init')
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        self.setup()
        self.sound_effect()

        self.p1 = p1
        self.p2 = p2


        self.main_loop()





    def setup(self):
       # print ("in setup")

        pygame.init()

        self.DISPLAY = DISPLAY


        self.board = board
        self.board.draw(self.DISPLAY)

        self.clock = pygame.time.Clock()




    def main_loop(self):
       # print("in main loop")

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
    def __init__(self,position,direction,colour,dis, EEEEE) :
        #print('initialize player')
        self.lives = 3
        self.pos = position
        self.ogpos = copy.deepcopy(self.pos)
        self.lastpos = []
        self.pathnum = 0
        self.dir = direction
        self.olddir = copy.deepcopy(self.dir)
        self.col = colour
        self.counter = 0
        self.paths = [[self.pos[0],self.pos[1],self.pos[0] + 8, self.pos[1]+8]]
        self.turns = 0
        self.ID =EEEEE

        self.DISPLAY = dis

    def update(self):
        #print("in update")

        #paths


        print(self.paths)
        print('pos', self.pos)

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

        if self.olddir != self.dir:
            print('new')
            self.paths.append([self.pos[0],self.pos[1],self.pos[0] + 8, self.pos[1 ]+8])
            self.turns += 1
        else:
            self.paths[len(self.paths)-1][0] -= 3


    def go_right(self):
        #print("in go right")
        self.pos[0] += 3

        if self.olddir != self.dir:
            print('new')
            self.paths.append([self.pos[0],self.pos[1],self.pos[0] + 8, self.pos[1]+8])
            self.turns += 1
        else:
            self.paths[len(self.paths)-1][2] += 3

    def go_up(self):
        #print("in go up")
        self.pos[1] -= 3

        if self.olddir != self.dir:
            print('new')
            self.paths.append([self.pos[0],self.pos[1],self.pos[0] + 8, self.pos[1 ]+8])
            self.turns += 1
        else:
            self.paths[len(self.paths)-1][1] -= 3

    def go_down(self):
       # print("in go down")
        self.pos[1] += 3

        if self.olddir != self.dir:
            print('new')
            self.paths.append([self.pos[0], self.pos[1], self.pos[0] + 8, self.pos[1]+8])
            self.turns += 1
        else:
            self.paths[len(self.paths) - 1][3] += 3


    def check_collision(self):
        # print("in check collision")

        if self.pos[0] <= 7:
               #print('wallDeath')
               self.kill()
               self.start_again()
        if self.pos[1] <= 7:
               #print('wallDeath')
               self.kill()
               self.start_again()
        if self.pos[0] >= (800 - 15):
               #print('wallDeath')
               self.pos[0] = (800 - 18)
               self.kill()
               self.start_again()

        if self.pos[1] >= 492:
               #print('wallDeath')
               self.pos[1] = 489
               self.kill()
               self.start_again()

        #path collision

        valid = True
        if self.ID == 1:
            for i in range(p1.turns - 1):
                if valid == True and self.pos[0]+1 >= p1.paths[i][0] and self.pos[0] <= p1.paths[i][2] and self.pos[1] >= p1.paths[i][1] and self.pos[1]+1 <= p1.paths[i][3]:
                    print('HIT')
                    valid = False
                    self.kill()
                    self.start_again()

            for i in range(p2.turns + 1):
                if valid == True and self.pos[0]+1 >= p2.paths[i][0] and self.pos[0] <= p2.paths[i][2] and self.pos[1] >= p2.paths[i][1] and self.pos[1]+1 <= p2.paths[i][3]:
                    print('HIT')
                    valid = False
                    self.kill()
                    self.start_again()

        else:
            for i in range(p1.turns + 1):
                if valid == True and self.pos[0]+1 >= p1.paths[i][0] and self.pos[0] <= p1.paths[i][2] and self.pos[1] >= p1.paths[i][1] and self.pos[1]+1 <= p1.paths[i][3]:
                    print('HIT')
                    valid = False
                    self.kill()
                    self.start_again()

            for i in range(p2.turns - 1):
                if valid == True and self.pos[0]+1 >= p2.paths[i][0] and self.pos[0] <= p2.paths[i][2] and self.pos[1] >= p2.paths[i][1] and self.pos[1]+1 <= p2.paths[i][3]:
                    print('HIT')
                    valid = False
                    self.kill()
                    self.start_again()









    def kill(self):
        #print('kill player')
        self.lives -= 1

        p1.pos = copy.deepcopy(p1.ogpos)
        p1.dir = 2
        p2.pos = copy.deepcopy(p2.ogpos)
        p2.dir = 0

    def start_again(self):
        time.sleep(1)
        p1.turns = 0
        p2.turns = 0
        p1.paths = [[p1.pos[0],p1.pos[1],p1.pos[0] + 8, p1.pos[1]+8]]
        p2.paths = [[p2.pos[0],p2.pos[1],p2.pos[0] + 8, p2.pos[1]+8]]
        p1.lastpos = []
        p2.lastpos = []

        if p1.lives == 0 or p2.lives == 0:
            sys.exit()
        board.draw(DISPLAY)



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
        player_1_heart = pygame.image.load('heart.png')


        # display player 2 hearts
        for i in range(p1.lives):
            window.blit(player_1_heart, (i*50 + 20, 575))


        # load player 2 hearts
        player_2_heart = pygame.image.load('heart.png')


        # display player 2 hearts
        for j in range(p2.lives):
            window.blit(player_2_heart, (j * 50 + 400, 575))

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




DISPLAY = pygame.display.set_mode((800,600),0,32)
p1 = Player([99, 99],2,(255,150,0),DISPLAY,1)
p2 = Player([699,300],0,(0,100,255),DISPLAY,2)
board = GameBoard()

if __name__ == '__main__': run = Main()


