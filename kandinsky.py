from pygame import display as screen, image, draw, event, key, init
from pygame.constants import *
from pygame.font import Font
from pygame.time import wait
import pygame
from math import floor


######### Main class #########
DEBUG = False
class Core:
  init()

  APP_NAME = "kandinsky"
  TOP_SIZE = 34
  SCREEN = (320, 256)
  PATH = "./"
  COLORS = {
    "red": (248, 0, 0), "cyan": (0, 252, 248), "blue": (0, 0, 248), "grey": (160, 164, 160), "green": (80, 192, 0), 
    "gray": (160, 164, 160), "pink": (248, 168, 176), "purple": (104, 44, 120), "magenta": (248, 4, 136), "black": (0, 0, 0), 
    "orange": (248, 132, 24), "brown": (136, 112, 80), "white": (248, 252, 248), "yellow": (248, 252, 0)
  }
  MODES = ("Numworks mode", "Omega mode", "PC mode")
  mode = 2
  quit = False

  def __init__(self):
    pygame.init()
    self.root = screen.set_mode(self.SCREEN)
    self.windowFont, self.font = Font(self.PATH+"small_font.ttf", 12), Font(self.PATH+"large_font.ttf", 16)

    screen.set_caption(self.APP_NAME)
    screen.set_icon(image.load(self.PATH+"icon.ico"))

    self.root.fill(self.COLORS["white"])
    self.draw_content()
    self.refresh()

  def draw_content(self):
    draw.rect(self.root, "white", (0, 0, 320, 15))
    # self.root.blit(self.windowFont.render("CTRL+M: to change the refresh mode", True, "black"), (2, 0))
    draw.line(self.root, "black", (0, 15), (self.SCREEN[0], 15))
    draw.rect(self.root, "#ffb531" if self.mode == 0 or self.mode == 2 else "#c53431", (0, 16, self.SCREEN[0], 18))
    self.root.blit(self.windowFont.render("deg" if self.mode == 0 or self.mode == 2 else "sym/deg", True, self.COLORS["white"]), (5, 16))
    self.root.blit(self.windowFont.render("PYTHON", True, self.COLORS["white"]), (139, 17))
    if self.mode == 0 or self.mode == 2:
      draw.line(self.root, self.COLORS["white"], (300, 21), (300, 28))
      draw.rect(self.root, self.COLORS["white"], (302, 21, 10, 8))
      draw.line(self.root, self.COLORS["white"], (313, 21), (313, 28))
      draw.line(self.root, self.COLORS["white"], (314, 23), (314, 26))
    else:
      draw.line(self.root, self.COLORS["white"], (260, 21), (260, 28))
      draw.rect(self.root, self.COLORS["white"], (262, 21, 10, 8))
      draw.line(self.root, self.COLORS["white"], (273, 21), (273, 28))
      draw.line(self.root, self.COLORS["white"], (274, 23), (274, 26))
      self.root.blit(self.windowFont.render("12:00", True, self.COLORS["white"]), (280, 17))

  def get_pixel(self, x, y):
    if self.quit: return
    self.type_test(x)
    self.type_test(y)

    if y < 0 or x < 0 or x >= self.SCREEN[0] or y+self.TOP_SIZE >= self.SCREEN[1]: return (0, 0, 0)
    return self.convert_color(self.root.get_at((x, y+self.TOP_SIZE))[:-1])

  def set_pixel(self, x, y, color):
    if self.quit: return
    self.type_test(x)
    self.type_test(y)

    if y < 0: return
    self.root.set_at((x, y+self.TOP_SIZE), self.convert_color(color))
    self.refresh()

  def color(self, rOrColor, g, b):
    if g == None and b == None: return self.convert_color(rOrColor)
    elif g != None and b != None: 
      self.type_test(g)
      self.type_test(b)
      return self.convert_color((rOrColor, g, b))
    else: raise TypeError("color takes 1 or 3 arguments")

  def drawString(self, text, x, y, color, background):
    draw.rect(self.root, self.convert_color(background), (x, y+2, len(text)*10, 18))
    self.root.blit(self.font.render(text, True, self.convert_color(color)), (x, y))

  def draw_string(self, text, x, y, color, background):
    if self.quit: return
    self.type_test(text, "str")
    self.type_test(x)
    self.type_test(y)

    y += self.TOP_SIZE-2
    text = text.replace(chr(13), '').replace(chr(9), "    ").split(chr(10))
    self.drawString(text[0], x, y, color, background)
    for i in range(1, len(text)): self.drawString(text[i], 0, y+i*18, color, background)

    if y < self.TOP_SIZE: self.draw_content()
    self.refresh()
  
  def fill_rect(self, x, y, width, height, color):
    if self.quit: return
    self.type_test(x)
    self.type_test(y)
    self.type_test(width)
    self.type_test(height)
    
    y += self.TOP_SIZE
    if width < 0:  x, width = x+width, -width
    if height < 0: y, height = y+height, -height
    if y < self.TOP_SIZE and y+height > self.TOP_SIZE: height, y = height-self.TOP_SIZE-y, self.TOP_SIZE
    elif y+height <= self.TOP_SIZE: return
    
    draw.rect(self.root, self.convert_color(color), (x, y, width, height))
    self.refresh()

  def display(self):
    while not self.quit: self.refresh(False)
    
  def refresh(self, withError=True):
    try: screen.flip()
    except: self.quit = True
    else: 
      if self.mode == 0: wait(2)
      elif self.mode == 1: wait(1)

      for e in event.get():
        if e.type == QUIT: 
          screen.quit()
          self.quit = True
          if withError: raise RuntimeError("kandinsky window destroyed")
        # elif e.type == KEYDOWN: 
        #   if key.get_mods() & KMOD_CTRL and key.get_pressed()[K_m]:
        #     self.mode = 0 if self.mode == 2 else self.mode+1
        #     screen.set_caption(self.APP_NAME+": "+self.MODES[self.mode])
        #     self.draw_content()

  def convert_color(self, color):
    self.type_test(color, "color")

    if type(color) == str: 
      if color in self.COLORS: return self.COLORS[color]
      else: raise ValueError("invalid syntax for number")
    elif type(color) == tuple: color = list(color)
    
    for i in range(len(color)):
      if type(color[i]) == float: color[i] = floor(color[i])
      else: self.type_test(color[i])

      if color[i] < 0: color[i] = 0
      elif color[i] > 255: color[i] %= 256
    return (floor(color[0] / 8) * 8, floor(color[1] / 4) * 4, floor(color[2] / 8) * 8)

  def type_test(self, _object, mode="int"):
    _type = type(_object)
    
    if mode == "int": 
      if _type != int: raise TypeError("can't convert {} to float".format(_type.__name__))
    
    elif mode == "color":
      if _type == int: raise TypeError("Int are not colors")
      elif _type == str: return
      elif _type != tuple and _type != list: 
        raise TypeError("object '{}' isn't a tuple or list".format(_type.__name__))
      elif len(_object) != 3: raise TypeError("Color needs 3 components")

    elif mode == "str":
      if _type != str: raise TypeError("can't convert '{}' object to str implicitly".format(_type.__name__))

    else: raise ValueError("Core: invalid type test mode")

Core = Core()

def display(justRefresh=False):
  """Run an infinite loop (a little modified) allowing to keep the window open
  If justRefresh == True: Just refresh the screen and dont run the loop.
  """
  try: 
    if justRefresh: Core.refresh()
    else: Core.display()
  except Exception as e:
    raise \
      e if DEBUG else e.with_traceback(None)

def fill_rect(x, y, width, height, color):
  """Fill a rectangle at pixel (x, y)"""
  try: Core.fill_rect(x, y, width, height, color)
  except Exception as e: 
    raise \
      e if DEBUG else e.with_traceback(None)

def draw_string(text, x, y, color=(0,0,0), background=(248,252,248)):
  try: Core.draw_string(text, x, y, color, background)
  except Exception as e: 
    raise \
      e if DEBUG else e.with_traceback(None)