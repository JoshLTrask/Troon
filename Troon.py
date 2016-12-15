class Main:

def setup:
    print ("in setup")

def main_loop:
    print("in main loop")

def sound_effect:
    print("in sound effect")

    
class Player: 
  def init(self,position,direction,colour) :
     print("in position direction image")

  def update:
      print("in update")

  def draw:
      print("in draw")

  def go_left:
      print("in go left")

  def go_right:
      print("in go right")

  def go_up:
      print("in go up")

  def go_down:
      print("in go down")

  def check_collision:
      print("in check collision")

  def make_path:
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
