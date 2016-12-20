
class Main:

    def __init__(self):
        print('init')

        self.setup()

        self.p1 = Player([100,100],2,(255,150,0),self.DISPLAY)
        self.p2 = Player([700,500],0,(0,100,255),self.DISPLAY)


        self.main_loop()





    def setup(self):
        print ("in setup")

        pygame.init()

        self.DISPLAY = pygame.display.set_mode((800,600),0,32)

        self.WHITE = (255,255,255)
        self.blue = (0,0,255)

        self.DISPLAY.fill(self.WHITE)
        #pygame.draw.rect(self.DISPLAY,self.blue,(200,150,100,50))
        self.clock = pygame.time.Clock()




    def main_loop(self):
        print("in main loop")
        while True:
            #60 frames/sec
            self.clock.tick(1000/30)

            pygame.display.update()
            self.DISPLAY.fill(self.WHITE)
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
            self.control()
            self.p1.update()
            self.p2.update()

    def control(self):

        Key = pygame.key.get_pressed()

        if Key[pygame.K_UP] :
            self.p1.dir = 0

        if Key[pygame.K_RIGHT]:
            self.p1.dir = 1

        if Key[pygame.K_LEFT]:
            self.p1.dir = 3

        if Key[pygame.K_DOWN]:
            self.p1.dir = 2

        #p2 move
        if Key[pygame.K_w]:
            self.p2.dir = 0

        if Key[pygame.K_d]:
            self.p2.dir = 1

        if Key[pygame.K_a]:
            self.p2.dir = 3

        if Key[pygame.K_s]:
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
        print("in sound effect")


    
class Player:
    def __init__(self,position,direction,colour,dis) :
        print('initialize player')
        self.lives = 3
        self.pos = position
        self.dir = direction
        self.col = colour
        self.paths = []

        self.DISPLAY = dis

    def update(self):
        #print("in update")


        #move player



        self.draw()

    def draw(self):
        #print("in draw")

        pygame.draw.rect(self.DISPLAY, self.col, (self.pos[0],self.pos[1], 8, 8))
        #print('pos',self.pos)


    def go_left(self):
        print("in go left")
        self.pos[0] -= 3

    def go_right(self):
        print("in go right")
        self.pos[0] += 3

    def go_up(self):
        print("in go up")
        self.pos[1] -= 3

    def go_down(self):
        print("in go down")
        self.pos[1] += 3


    def check_collision(self):
          print("in check collision")

    def make_path(self):
          print("in make path")

      
class GameBoard:

  def update:
      print("in update")

  def draw:
      print("in draw")
class Path:

  def draw:
      print("in draw")

  def makepath:
      print("in make path")
