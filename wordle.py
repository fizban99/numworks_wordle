const = lambda x: x 
import os
os.environ['KANDINSKY_OS_MODE'] = '0'
os.environ['KANDINSKY_ZOOM_RATIO'] = "3"
from random import randint
from time import sleep as slp
from kandinsky import fill_rect as fr,draw_string as ds
from ion import *
from ion import keydown as kd
# minifier-hide start
import kandinsky
import pygame_textinput
from kandinsky import display
import asyncio
gtext = ""
def print(text):
    global gtext
    ds(text,0,0)
    if gtext == "":
        gtext = text
    else:
        gtext += "\n" + text



async def input(text):

    # Create TextInput-object
    manager = pygame_textinput.TextInputManager()
    font = pygame.font.Font("large_font.ttf", 18)
    textinput = pygame_textinput.TextInputVisualizer(manager=manager, font_object=font)
    textinput.antialias = True

    screen = kandinsky.Core.root
    clock = pygame.time.Clock()
    text = gtext +"\n"+text
    end_input = False
    while not end_input:

        screen.fill((255, 255, 255))
        kandinsky.Core.draw_content()
        if text !="":
            for y in range(0, len(text.split("\n"))):
                line = font.render(text.split("\n")[y], True, (0, 0, 0))
                screen.blit(line, (0, 36+18*y))
        events = pygame.event.get()

        # Feed it with events every frame
        textinput.update(events)
        # Blit its surface onto the screen
        # pygame.draw.rect(screen, (255,255,255), (0, 40+2, len(manager.value)*10, 18))
        screen.blit(textinput.surface, (0, 36+18*y))

        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
                value = manager.value
                end_input = True
                break
        pygame.display.update()
        await asyncio.sleep(0.05)
        clock.tick(30)
    return value
# minifier-hide end
wlst = ['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'
,
'8R8NQcjl4sOE8Fw9uQMoJCsL5vIoHRXDa2B+UA=='
,
'D7L9JA1OINTivPDC0n/V4g1tYNPh5AUNIzVK1e1SPXYQ0fAY0LmI7TDVDQ4+1Y0OC09i1cOgFNYtUIBAfiNxCfCgatANfxHqtgjgvQDUNBzm4qGjiqTioaH7LzoNIG0YBPCo8Af87NLS4LoQHqANLT0wby1QYNENAHCH4hTw1CoNUA8BDVB+C35QcJ1eC9gegNcY2x6g1hQV9Bav1R6gZgjB0OENC08aDVBAfSfhBRbwHRBdUdUQ0eNn0BA/vU1OO81QrwFtIGHT8SAR0gXwyAXNXaKNXh8aZAlm1eC9Hl0dAI5ewNUD7WDQBPAQ1Q0Any1QjT9PCAcBfS/X8R6gUWDZJPEtBxh12KgdIC0RcwefcoDPAgzi0tXwML1nDTINXwHqDVswbigQ0e0eO9ANDjjQtH4g2ZA='
,
'9S+dRCzVBeritB1SfR8CjUNSjw2icdniHQ0LTtYFB1DbELWNkYH3Jg1PAcQvntQKIFgIo08KLVAwB+C/cg2xDZENI9E199QX1tYNMobwIM0m4g0dTlCPHPAwse1A0+C9XhvQ0OO0LRdQ2eFldjfhs/khLU4wkMwxLwFgUO0X0dRY8S4W+iHwpA1QPzHita1Q0QgHvQ0OI05eYEOdUNfhFRnxaQ0OLoDQJNYNldG+0+JjjR4QXA=='
]



def fb64(eb):
    """Decode a base64 encoded string"""
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    dl, ai = (len(eb) * 3) // 4 - eb.count('='), 0
    for i in range(0, len(eb), 4):
        bi = ((base64.index(eb[i])) << 18) | ((base64.index(eb[i+1])&0x3F) << 12) | ((base64.index(eb[i+2])&0x3F) << 6) | base64.index(eb[i+3])&0x3f
        for byte in (bi >> 16, (bi >> 8) & 0xFF, bi & 0xFF):
            if ai < dl: yield int(byte); ai += 1

class Storage:
    letters     = "seaoriltnudycpmhgbkfwvzjxq"
    num_w = (141, 314, 512, 623, 695, 831, 946, 1015, 1049, 1069, 1089, 1177, 1284, 1321, 1362, 1504, 1527, 1632, 1998, 2147, 2180, 2223, 2306, 2312, 2315)

    def _init(self, wl ):
        self.lind =None
        self.seq = None
        self.last_char = 0
        self.wl = wl
        if self._letter_get(0)==0:
            self.padding = 1
        else:
            self.padding = 0        
        self.lind=None
        self.word = ""
        self.s_word = None
        self.word_num = None

    def _get_pos(self, i):
        if self.lind is not None and i == self.lind-1:
            return self.last_char
        if self.lind is None or i<self.lind:
            self.seq = fb64(self.wl)
            self.lind = 0
        while self.lind < i:
            next(self.seq)
            self.lind += 1
        self.last_char = next(self.seq)
        self.lind += 1
        return self.last_char

    def _letter_get(self, i):
        try:
            pos = (self._get_pos(i >> 1) >> ((i & 1) ^ 1) * 4) & 0xF
        except StopIteration:
            pos = 0
        return pos


    def _parse_sibl(self, c_ind, d, num=0, word=""):
        if d > 3:
            if self._letter_get(c_ind) == 15:
                c_ind += 1
                num = num+1
                self.word = word
            if word == self.s_word:
                self.word = word
            return [], c_ind, num    
        sibl = []
        n_sibl = self._letter_get(c_ind)
        # read number of siblings
        if n_sibl == 14:
            c_ind += 1
            n_sibl = 2
        elif n_sibl == 15:
            c_ind += 1
            n_sibl = self._letter_get(c_ind)+3
            if n_sibl == 18:
                c_ind += 1
                n_sibl += self._letter_get(c_ind)
            c_ind += 1
        else:
            n_sibl = 1
        for _ in range(n_sibl):
            # read node value
            node = self._letter_get(c_ind)
            if node == 13:
                c_ind += 1
                node = node + self._letter_get(c_ind)
            c_ind += 1
            sibl.append((node, c_ind))
            # Recursively parse children
            c_word = word + Storage.letters[node]
            _, c_ind, num = self._parse_sibl(c_ind , d+1, num, c_word)
            # if word is found return
            if num == self.word_num or self.word == self.s_word:
                break
        
        return sibl, c_ind, num
    
    def get_word_num(self, num):
       for i, max_n in enumerate(Storage.num_w):
              if num <= max_n:
                self._init(wlst[i])
                num = num - Storage.num_w[i-1] if i > 0 else num
                break
       self.word_num = num
       self.s_word = None
       self._parse_sibl(self.padding, 0)
       self.word_num = None
       return chr(ord("a") +i) + self.word 

    def is_word(self, word):
       i = ord(word[0])-ord("a")
       self._init(wlst[i])
       self.word_num = None
       self.word = None
       self.s_word = word[1:]
       self._parse_sibl(self.padding, 0)
       return self.word == self.s_word

def rgb(c): return ((c>>11&0x1F)*255//31, (c>>5&0x3F)*255//63, (c&0x1F)*255//31)


def dr_fr(x, y, c, i, o=0):
    fr(x*37+11-i-o, y*37+2-i  , 32+i*2, 1, rgb(c))
    fr(x*37+42+i-o, y*37+2-i  , 1, 32+i*2, rgb(c))
    fr(x*37+11-i-o, y*37+33+i  , 32+i*2, 1, rgb(c))
    fr(x*37+11-i-o, y*37+2-i  , 1, 32+i*2, rgb(c))


_BLACK = const(0) # black    
_WHITE = const(65535) # white
_LGRAY = const(52890) # light gray
_DGRAY= const(29647) # dark gray
_GREEN = const(25932) # green
_YELLOW = const(64901)  # yellow
_TOTAL_WORDS = 2315

def draw_board():   
    for x in range (5):
        for y in range (6):
            dr_fr(x, y, _LGRAY, 0)



stor = Storage()

async def trn_tile(x, y, c, l):
    for i in range(16):
        fr(x*37+11, y*37+2+i  , 32, 1, rgb(_DGRAY))
        fr(x*37+11, y*37+33-i  , 32, 1, rgb(_DGRAY))
        await asyncio.sleep(0.01)
        fr(x*37+11, y*37+2+i  , 32, 1, rgb(_WHITE))
        fr(x*37+11, y*37+33-i  , 32, 1, rgb(_WHITE))
    for i in range(16):
        fr(x*37+11, y*37+18-i  , 32, 1, rgb(c))
        fr(x*37+11, y*37+18+i  , 32, 1, rgb(c))
        if i == 7:
            ds(l, x*37+22, y*37+9, rgb(65535),rgb(c) )
        await asyncio.sleep(0.01)


async def highl(x,y):
    for i in range(1,4):
        dr_fr(x, y, _WHITE, i-1)
        dr_fr(x, y, _DGRAY, i)
        await asyncio.sleep(0.03)

    for i in range(3,-1,-1):
        dr_fr(x, y, _WHITE, i+1)
        dr_fr(x, y, _DGRAY, i)
        await asyncio.sleep(0.03)

async def vibr(y, curr_wrd):
    for x in range(5):
        dr_fr(x, y, _WHITE,0)
    await asyncio.sleep(0.01)
    for j in range(6):
        for o in ((0,3,1), (3,-3,-1), (-2,0,1)):
            for i in range(o[0],o[1],o[2]):
                for x in range(5):
                    dr_fr(x, y, _DGRAY,0,i)
                    ds(curr_wrd[x], x*37+22-i, y*37+9)
                await asyncio.sleep(0.01)
                for x in range(5):
                    dr_fr(x, y, _WHITE,0,i)
    for x in range(5):
        dr_fr(x, y, _DGRAY,0)
    await asyncio.sleep(0.01)

def dr_letter(l, c):
    i = ord(l) - ord("A")
    x = i%6 if i < 24 else i%6+2
    y = i//6
    fr(x*20+199, y*24+103, 16, 20, rgb(c))
    fc = _BLACK if c == _LGRAY else _WHITE
    ds(l, x*20+202, y*24+104, rgb(fc), rgb(c))    


msgs = ("  Genius!", 
       "Magnificent!", 
       "Impressive!", 
       " Splendid!", 
       "   Great!", 
       "   Phew!")

async def main():
    w_num = randint(1, 2315)
    w_num = 1851
    # conceal the word number
    w_id = ((w_num>>6) | ((w_num<<6)&0xFC0)) ^0xAAA
    print("Selected NW-Wordle id: #"+ str(w_id))
    await asyncio.sleep(0.1)
    w_id2 = ""
    msg = ""
    while w_id2 == "":
        w_id2 = await input(msg +"Press OK or enter\nanother id to start\n")
        if w_id2 == "" or (w_id2.isdigit() and int(w_id2) < 4096):
            w_id  = int(w_id2) if w_id2 != "" else w_id
            break
        else:
            msg = "Invalid id\n"
            w_id2 = ""

    w_num = (w_id ^ 0xAAA)
    w_num = ((((w_num>>6) | ((w_num<<6)&0xFC0))-1)%_TOTAL_WORDS)+1
    word = stor.get_word_num(w_num)

    # minifier-hide start
    kandinsky.Core.root.fill((255, 255, 255))
    kandinsky.Core.draw_content()
    # minifier-hide end
    draw_board()

    ds ("#" + str(w_id), 230,9)
    for i in range(26):
        dr_letter(chr(ord("A")+i), _LGRAY)



    keys =         '\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2A\x2B\x2C\x2D\x34\x04'
    key_pressing = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'    
    curr_x = 0
    curr_wrd = ""
    curr_y = 0
    end_game = False

    while True:
    # minifier-hide start
        display(True)
    # minifier-hide end
        for ik, k in enumerate(keys):
            k = ord(k)
            if kd(k) and not end_game:
                if  not ord(key_pressing[ik]):
                    key_pressing= key_pressing[:ik] + '\x01' + key_pressing[ik+1:]
                    if k==KEY_BACKSPACE:
                        if curr_x > 0:
                            curr_x = curr_x-1
                            curr_wrd = curr_wrd[:-1]
                            dr_fr(curr_x, curr_y, _LGRAY, 0)
                            ds(" ",curr_x*37+22,curr_y*37+9)
                    elif k==KEY_EXE or k==KEY_OK:
                        matches = ""
                        if curr_x == 5:
                            if stor.is_word(curr_wrd.lower()):
                                for i, (l, wl) in enumerate(zip(curr_wrd.lower(), word)):
                                    if l==wl:
                                        matches += l
                                        c = _GREEN
                                    elif l in word and curr_wrd.lower()[i+1:].count(l) < word.count(l)-matches.count(l):
                                        c = _YELLOW
                                    else:
                                        c = _DGRAY
                                    await trn_tile(i,curr_y,c, curr_wrd[i])
                                    dr_letter(l.upper(),c)
                                if curr_wrd.lower() == word:
                                    ds(msgs[curr_y], 200, 50)
                                    end_game = True
                                curr_y += 1
                                curr_x = 0
                                curr_wrd = ""
                                if curr_y == 6 and not end_game:
                                    ds(word.upper(), 220, 50)
                                    end_game = True
                            else:
                                ds("Not in word", 200, 50)
                                ds("   list    ", 200, 70)
                                await vibr(curr_y, curr_wrd)
                                ds("           ", 200, 50)
                                ds("           ", 200, 70)
                    elif curr_x < 5:
                        k = chr(k+47) if k < 35 else chr(k+46) if k<42 else chr(k+45)
                        curr_wrd += k
                        ds(k, curr_x*37+22, curr_y*37+9)
                        await highl(curr_x, curr_y)
                        curr_x += 1
            else:
                key_pressing=key_pressing[:ik] + '\x00' + key_pressing[ik+1:]


        await asyncio.sleep(0.05)

if __name__ == "__main__":
    asyncio.run(main())