import pygame
from sys import exit

class Engine():
  def __init__(self, Fps=30):
    self.Fps= Fps
    pygame.init()
    self.Screen = pygame.display.set_mode((500,500))
    self.Clock = pygame.time.Clock()
    self.RunLoop()

  def RunLoop(self):
    while True:
      for event in pygame.event.get():
        if event.type== pygame.QUIT:
          pygame.quit()
          exit()
      pygame.display.update()
      self.Clock.tick(self.Fps)

if __name__ == "__main__":
  Engine()
