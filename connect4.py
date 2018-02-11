
#could increaase board size to 9 x 8 

# Import a library of functions called 'pygame'
import pygame
import numpy as np
import copy
 
# Initialize the game engine
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (5, 73, 183)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (244, 232, 66)

 
# Set the height and width of the screen
size = (700, 700)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("ConnectFour")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

#features (mapping from board state to features)
#i'm player 2
#no of open connected 3-chains (open on both sides = count as 2)
def connect3(mat):
    count = 0
    #horizontal
    for xh in range(6):
        for yh in range(4):
            if mat[xh][yh] == 0 and mat[xh][yh+1] == 2 \
            and mat[xh][yh+2] == 2 and mat[xh][yh+3] == 2:
                count += 1
            if mat[xh][yh] == 2 and mat[xh][yh+1] == 2 \
            and mat[xh][yh+2] == 2 and mat[xh][yh+3] == 0:
                count += 1
    #vertical
    for xv in range(3):
        for yv in range(7):
            if mat[xv][yv] == 0 and mat[xv+1][yv] == 2 \
            and mat[xv+2][yv] == 2 and mat[xv+3][yv] == 2:
                count += 1   
            if mat[xv][yv] == 2 and mat[xv+1][yv] == 2 \
            and mat[xv+2][yv] == 2 and mat[xv+3][yv] == 0:
                count += 1   
    #diagonal
    for xvr in range(3):
        for yvr in range(4):
            if mat[xvr][yvr] == 0 and mat[xvr+1][yvr+1] == 2 \
            and mat[xvr+2][yvr+2] == 2 and mat[xvr+3][yvr+3] == 2:
                count += 1
            if mat[xvr][yvr] == 2 and mat[xvr+1][yvr+1] == 2 \
            and mat[xvr+2][yvr+2] == 2 and mat[xvr+3][yvr+3] == 0:
                count += 1
    for xvl in range(5,2,-1):
        for yvl in range(4):
            if mat[xvl][yvl] == 0 and mat[xvl-1][yvl+1] == 2 \
            and mat[xvl-2][yvl+2] == 2 and mat[xvl-3][yvl+3] == 2:
                count += 1
            if mat[xvl][yvl] == 2 and mat[xvl-1][yvl+1] == 2 \
            and mat[xvl-2][yvl+2] == 2 and mat[xvl-3][yvl+3] == 0:
                count += 1
    return count
#no of open connected 2-chains (open on both sides = count as 2)
def connect2(mat):
    count = 0
    #horizontal
    for xh in range(6):
        for yh in range(5):
            if mat[xh][yh] == 0 and mat[xh][yh+1] == 2 \
            and mat[xh][yh+2] == 2:
                count += 1
            if mat[xh][yh] == 2 and mat[xh][yh+1] == 2 \
            and mat[xh][yh+2] == 0:
                count += 1
    #vertical
    for xv in range(4):
        for yv in range(7):
            if mat[xv][yv] == 0 and mat[xv+1][yv] == 2 \
            and mat[xv+2][yv] == 2:
                count += 1   
            if mat[xv][yv] == 2 and mat[xv+1][yv] == 2 \
            and mat[xv+2][yv] == 0:
                count += 1   
    #diagonal
    for xvr in range(4):
        for yvr in range(5):
            if mat[xvr][yvr] == 0 and mat[xvr+1][yvr+1] == 2 \
            and mat[xvr+2][yvr+2] == 2:
                count += 1
            if mat[xvr][yvr] == 2 and mat[xvr+1][yvr+1] == 2 \
            and mat[xvr+2][yvr+2] == 0:
                count += 1
    for xvl in range(5,1,-1):
        for yvl in range(5):
            if mat[xvl][yvl] == 0 and mat[xvl-1][yvl+1] == 2 \
            and mat[xvl-2][yvl+2] == 2:
                count += 1
            if mat[xvl][yvl] == 2 and mat[xvl-1][yvl+1] == 2 \
            and mat[xvl-2][yvl+2] == 0:
                count += 1
    return count

def hisconnect3(mat):
    count = 0
    #horizontal
    for xh in range(6):
        for yh in range(4):
            if mat[xh][yh] == 0 and mat[xh][yh+1] == 1 \
            and mat[xh][yh+2] == 1 and mat[xh][yh+3] == 1:
                count += 1
            if mat[xh][yh] == 1 and mat[xh][yh+1] == 1 \
            and mat[xh][yh+2] == 1 and mat[xh][yh+3] == 0:
                count += 1
    #vertical
    for xv in range(3):
        for yv in range(7):
            if mat[xv][yv] == 0 and mat[xv+1][yv] == 1 \
            and mat[xv+2][yv] == 1 and mat[xv+3][yv] == 1:
                count += 1   
            if mat[xv][yv] == 1 and mat[xv+1][yv] == 1 \
            and mat[xv+2][yv] == 1 and mat[xv+3][yv] == 0:
                count += 1   
    #diagonal
    for xvr in range(3):
        for yvr in range(4):
            if mat[xvr][yvr] == 0 and mat[xvr+1][yvr+1] == 1 \
            and mat[xvr+2][yvr+2] == 1 and mat[xvr+3][yvr+3] == 1:
                count += 1
            if mat[xvr][yvr] == 1 and mat[xvr+1][yvr+1] == 1 \
            and mat[xvr+2][yvr+2] == 1 and mat[xvr+3][yvr+3] == 0:
                count += 1
    for xvl in range(5,2,-1):
        for yvl in range(4):
            if mat[xvl][yvl] == 0 and mat[xvl-1][yvl+1] == 1 \
            and mat[xvl-2][yvl+2] == 1 and mat[xvl-3][yvl+3] == 1:
                count += 1
            if mat[xvl][yvl] == 1 and mat[xvl-1][yvl+1] == 1 \
            and mat[xvl-2][yvl+2] == 1 and mat[xvl-3][yvl+3] == 0:
                count += 1
    return count
#no of open connected 2-chains (open on both sides = count as 2)
def hisconnect2(mat):
    count = 0
    #horizontal
    for xh in range(6):
        for yh in range(5):
            if mat[xh][yh] == 0 and mat[xh][yh+1] == 1 \
            and mat[xh][yh+2] == 1:
                count += 1
            if mat[xh][yh] == 1 and mat[xh][yh+1] == 1 \
            and mat[xh][yh+2] == 0:
                count += 1
    #vertical
    for xv in range(4):
        for yv in range(7):
            if mat[xv][yv] == 0 and mat[xv+1][yv] == 1 \
            and mat[xv+2][yv] == 1:
                count += 1   
            if mat[xv][yv] == 1 and mat[xv+1][yv] == 1 \
            and mat[xv+2][yv] == 0:
                count += 1   
    #diagonal
    for xvr in range(4):
        for yvr in range(5):
            if mat[xvr][yvr] == 0 and mat[xvr+1][yvr+1] == 1 \
            and mat[xvr+2][yvr+2] == 1:
                count += 1
            if mat[xvr][yvr] == 1 and mat[xvr+1][yvr+1] == 1 \
            and mat[xvr+2][yvr+2] == 0:
                count += 1
    for xvl in range(5,1,-1):
        for yvl in range(5):
            if mat[xvl][yvl] == 0 and mat[xvl-1][yvl+1] == 1 \
            and mat[xvl-2][yvl+2] == 1:
                count += 1
            if mat[xvl][yvl] == 1 and mat[xvl-1][yvl+1] == 1 \
            and mat[xvl-2][yvl+2] == 0:
                count += 1
    return count

#no of my pieces in center col
def mycenter(mat):
    count = 0
    for i in range(6):
        if mat[i][3] == 2:
            count += 1
    return count
    
#no of opponent's pieces in center col
def hiscenter(mat):
    count = 0
    for i in range(6):
        if mat[i][3] == 1:
            count += 1
    return count

#no of winning moves opponent has
mathyp = []

def hiswinning(mat):
#take matrix, drop 1 of opponents pieces in each col, count + 1 if this means he wins
    global mathyp
    mathyp = copy.deepcopy(mat)
    count = 0
    for col in range(7):
        dropped = 0
        for i in range(6):
            if mathyp[i][col] == 0 and dropped == 0:
                mathyp[i][col] = 1
                dropped = 1
                rowdropped = i
        if checkwin(mathyp) == 1:
            count += 1
        if dropped == 1: #if managed to drop, remove hypothetical piece, go to next column
            mathyp[rowdropped][col] = 0 
    return count

#choose control that max reward (which is linear weighting of features
#acc to weight vector. also if win, +1000)

weights = [3,2,1,-10,-5,-3,-50,100] #last weight is for a winning move

def choosebest(mat,weights):
    feat = []
    matchoice = copy.deepcopy(mat)
    bestcol = 100
    highestrew = -1000
    for col in range(7):
        #drop
        dropped = 0
        reward = 0
        for i in range(6):
            if matchoice[i][col] == 0 and dropped == 0:
                matchoice[i][col] = 2
                dropped = 1
                rowdropped = i
        #construct vector of features
        feat.append(connect3(matchoice))
        feat.append(connect2(matchoice))
        feat.append(mycenter(matchoice))
        feat.append(hisconnect3(matchoice))
        feat.append(hisconnect2(matchoice))
        feat.append(hiscenter(matchoice))
        feat.append(hiswinning(matchoice))
        if checkwin(matchoice) == 2:
            feat.append(1) #1 if win
        else:
            feat.append(0) #0 if no win
            
        #calculate reward
        for j in range(len(weights)):
            reward = reward + weights[j]*feat[j] 
        
        if reward > highestrew:
            highestrew = reward
            bestcol = col
            print(feat)
        
        if dropped == 1: #if managed to drop, remove hypothetical piece, go to next column
            matchoice[rowdropped][col] = 0     
        feat = []
    
    return bestcol

class Button(object):
    def __init__(self, x, y, r, col):

        self.normal_colour = RED
        self.x = x
        self.y = y
        self.r = r
        self.shiny = False
        self.col = col
        self._rect = pygame.Rect(x-r,y-r,2*r,2*r)

        self.buttonDown = False # is the button currently pushed down?
        self.mouseOverButton = False # is the mouse currently hovering over the button?
        self.lastMouseDownOverButton = False # was the last mouse down event over the mouse button? (Used to track clicks.)
    
    def draw(self, screen):
        if self.shiny:
            bg = GREEN
        else:
            bg = self.normal_colour

        circ = (self.x, self.y)
        pygame.draw.circle(screen,bg,circ,self.r)

    def on_button(self, pos):
        return self.x - self.r <= pos[0] and self.x + self.r > pos[0] and \
               self.y - self.r <= pos[1] and self.y + self.r > pos[1]
               
    def mouseClick(self, event):
        drop(self.col)
    def mouseEnter(self, event):
        pass # This class is meant to be overridden.
    def mouseMove(self, event):
        pass # This class is meant to be overridden.
    def mouseExit(self, event):
        pass # This class is meant to be overridden.
    def mouseDown(self, event):
        pass # This class is meant to be overridden.
    def mouseUp(self, event):
        pass # This class is meant to be overridden.
    
    def handleEvent(self, eventObj):
        if eventObj.type not in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
            # The button only cares bout mouse-related events (or no events, if it is invisible)
            return []
    
        retVal = []
    
        hasExited = False
        if not self.mouseOverButton and self._rect.collidepoint(eventObj.pos):
            # if mouse has entered the button:
            self.mouseOverButton = True
            self.mouseEnter(eventObj)
            retVal.append('enter')
        elif self.mouseOverButton and not self._rect.collidepoint(eventObj.pos):
            # if mouse has exited the button:
            self.mouseOverButton = False
            hasExited = True # call mouseExit() later, since we want mouseMove() to be handled before mouseExit()
    
        if self._rect.collidepoint(eventObj.pos):
            # if mouse event happened over the button:
            if eventObj.type == pygame.MOUSEMOTION:
                self.mouseMove(eventObj)
                retVal.append('move')
            elif eventObj.type == pygame.MOUSEBUTTONDOWN:
                self.buttonDown = True
                self.lastMouseDownOverButton = True
                self.mouseDown(eventObj)
                retVal.append('down')
        else:
            if eventObj.type in (pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
                # if an up/down happens off the button, then the next up won't cause mouseClick()
                self.lastMouseDownOverButton = False
    
        # mouse up is handled whether or not it was over the button
        doMouseClick = False
        if eventObj.type == pygame.MOUSEBUTTONUP:
            if self.lastMouseDownOverButton:
                doMouseClick = True
            self.lastMouseDownOverButton = False
    
            if self.buttonDown:
                self.buttonDown = False
                self.mouseUp(eventObj)
                retVal.append('up')
    
            if doMouseClick:
                self.buttonDown = False
                self.mouseClick(eventObj)
                retVal.append('click')
    
        if hasExited:
            self.mouseExit(eventObj)
            retVal.append('exit')
    
        return retVal

buttons = []
b0 = Button(140,80,25,col=0)
b1 = Button(210,80,25,col=1)
b2 = Button(280,80,25,col=2)
b3 = Button(350,80,25,col=3)
b4 = Button(420,80,25,col=4)
b5 = Button(490,80,25,col=5)
b6 = Button(560,80,25,col=6)
buttons=[b0,b1,b2,b3,b4,b5,b6]


def drop(col):
    global winner
    global mat
    global weights
    dropped = 0
    dropped2 = 0
    for i in range(6):
        if mat[i][col] == 0 and dropped == 0:
            mat[i][col] = 1
            dropped = 1
    winner = checkwin(mat)
    if winner == None:
        #ran = np.random.randint(0,7)
        ran = choosebest(mat,weights)
        for j in range(6):
            if mat[j][ran] == 0 and dropped2 == 0:
                mat[j][ran] = 2
                dropped2 = 1
        print(mat)
        print(hiswinning(mat))
    winner = checkwin(mat)
    print(winner)


def checkwin(mat):
    #horizontal
    for xh in range(6):
        for yh in range(4):
            if mat[xh][yh] == 1 and mat[xh][yh+1] == 1 \
            and mat[xh][yh+2] == 1 and mat[xh][yh+3] == 1:
                return 1
            if mat[xh][yh] == 2 and mat[xh][yh+1] == 2 \
            and mat[xh][yh+2] == 2 and mat[xh][yh+3] == 2:
                return 2
    #vertical
    for xv in range(3):
        for yv in range(7):
            if mat[xv][yv] == 1 and mat[xv+1][yv] == 1 \
            and mat[xv+2][yv] == 1 and mat[xv+3][yv] == 1:
                return 1
            if mat[xv][yv] == 2 and mat[xv+1][yv] == 2 \
            and mat[xv+2][yv] == 2 and mat[xv+3][yv] == 2:
                return 2   
    #diagonal
    for xvr in range(3):
        for yvr in range(4):
            if mat[xvr][yvr] == 1 and mat[xvr+1][yvr+1] == 1 \
            and mat[xvr+2][yvr+2] == 1 and mat[xvr+3][yvr+3] == 1:
                return 1
            if mat[xvr][yvr] == 2 and mat[xvr+1][yvr+1] == 2 \
            and mat[xvr+2][yvr+2] == 2 and mat[xvr+3][yvr+3] == 2:
                return 2
    for xvl in range(5,2,-1):
        for yvl in range(4):
            if mat[xvl][yvl] == 1 and mat[xvl-1][yvl+1] == 1 \
            and mat[xvl-2][yvl+2] == 1 and mat[xvl-3][yvl+3] == 1:
                return 1
            if mat[xvl][yvl] == 2 and mat[xvl-1][yvl+1] == 2 \
            and mat[xvl-2][yvl+2] == 2 and mat[xvl-3][yvl+3] == 2:
                return 2
mat = []
row = []
winner = None

# initialize empty matrix
for i in range(6): #row
    for j in range(7): #column
        row.append(0)
    mat.append(row)
    row = []

# Loop as long as done == False
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        b0.handleEvent(event)
        b1.handleEvent(event)
        b2.handleEvent(event)
        b3.handleEvent(event)
        b4.handleEvent(event)
        b5.handleEvent(event)
        b6.handleEvent(event)
        
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill(WHITE)
    
    #draw winning end screen
    if winner == 1:
        screen.fill(RED)
    if winner == 2:
        screen.fill(YELLOW)
        
    mouse = pygame.mouse.get_pos()
    
    #draw game board
    pygame.draw.rect(screen, BLUE, [100,100,500,480], 0)
    
    for i in buttons:
        i.draw(screen)
    for y_offset in range(0,420,70):
        for x_offset in range(0, 490, 70):
            pygame.draw.circle(screen, WHITE, [140 + x_offset, 150 + y_offset], 25, 0)
    
    #draw dropped pieces
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 1:
                pygame.draw.circle(screen, RED, [140 + j*70, 500 - i*70], 25, 0)
            if mat[i][j] == 2:
                pygame.draw.circle(screen, YELLOW, [140 + j*70, 500 - i*70], 25, 0)
    

 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.

    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.        
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()
