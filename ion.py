import pygame
import sys

KEY_LEFT = 0
KEY_UP = 1
KEY_DOWN = 2
KEY_RIGHT = 3
KEY_OK = 4
KEY_BACK = 5
KEY_HOME = 6
KEY_ONOFF = 7
KEY_SHIFT = 12
KEY_ALPHA = 13
KEY_XNT = 14
KEY_VAR = 15
KEY_TOOLBOX = 16
KEY_BACKSPACE = 17
KEY_EXP = 18
KEY_LN = 19
KEY_LOG = 20
KEY_IMAGINARY = 21
KEY_COMMA = 22
KEY_POWER = 23
KEY_SINE = 24
KEY_COSINE = 25
KEY_TANGENT = 26
KEY_PI = 27
KEY_SQRT = 28
KEY_SQUARE = 29
KEY_SEVEN = 30
KEY_EIGHT = 31
KEY_NINE = 32
KEY_LEFTPARENTHESIS = 33
KEY_RIGHTPARENTHESIS = 34
KEY_FOUR = 36
KEY_FIVE = 37
KEY_SIX = 38
KEY_MULTIPLICATION = 39
KEY_DIVISION = 40
KEY_ONE = 42
KEY_TWO = 43
KEY_THREE = 44
KEY_PLUS = 45
KEY_MINUS = 46
KEY_ZERO = 48
KEY_DOT = 49
KEY_EE = 50
KEY_ANS = 51
KEY_EXE = 52
KEYS = [
    pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_RETURN, pygame.K_DELETE, pygame.K_HOME, pygame.K_END, None, None,
    None, None, pygame.K_LSHIFT, pygame.K_LCTRL, pygame.K_COLON, pygame.K_SEMICOLON, pygame.K_BACKSLASH, pygame.K_BACKSPACE, pygame.K_a, pygame.K_b,
    pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l,
    pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, None, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u,
    pygame.K_v, None, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, pygame.K_MINUS, None, pygame.K_0, pygame.K_PERIOD,
    pygame.K_INSERT, pygame.K_AT, pygame.K_RETURN, None, pygame.K_F1, pygame.K_F2, pygame.K_F3, pygame.K_F4, pygame.K_F5, pygame.K_F6,
    pygame.K_F7, pygame.K_F8, pygame.K_F9, pygame.K_F10, pygame.K_F11, pygame.K_F12, None, None, None, pygame.K_ESCAPE, pygame.K_TAB, pygame.K_SPACE,
    None, None, None
]


def keydown(key):
  # Handle system events
  # for event in pygame.event.get():
  #   if event.type == pygame.QUIT:
  #     pygame.quit()
  #     sys.exit()
  # Check for keys being pressed
  if key < 0 or key > 52 or KEYS[key] == None: return False
  keys = pygame.key.get_pressed()
  return keys[KEYS[key]]

def get_keys(): return KEYS