#This was saved as a .ipynb but that's not supported by git so i did python to highlight syntax and so it would load the code.


#########################################

def get_distance(enemy_x, enemy_y, player_x, player_y):
     
    import math
    distance = math.sqrt(math.pow((enemy_x-player_x),2)+math.pow((enemy_y-player_y),2))
    
    return distance

#########################################

def move(x_pos, y_pos, dist, grid, grid_size, sq_num):
     
    row,col = get_cell(grid_size,sq_num,x_pos,y_pos)
    
    sq_size = grid_size/sq_num
    tl = (x_pos,y_pos)
    bl = (x_pos,y_pos+sq_size)
    tr = (x_pos+sq_size,y_pos)
    br = (x_pos+sq_size,y_pos+sq_size)
    
    tl = (tl[0] + .0001, tl[1] + .0001)
    bl = (bl[0] + .0001, bl[1] - .0001)
    tr = (tr[0] - .0001, tr[1] + .0001)
    br = (br[0] - .0001, br[1] - .0001)
    
    if event.key == pygame.K_LEFT:
        # Check to see if a left keystroke will result in movement. If the player will be off screen as a result of the 
        # key press, do not advance the x coordinate. If the player will be moving through a barrier, do not advance the
        # x coordinate. If the player will not move into an obstruction or off screen, advance the x coordinate (accordingly)
        # by a step of size dist.
        row_tl, col_tl = get_cell(grid_size, sq_num, tl[0] - dist, tl[1])
        row_bl, col_bl = get_cell(grid_size, sq_num, bl[0] - dist, bl[1])
        if(x_pos>0):
            if (grid[row_tl][col_tl] != 1) and (grid[row_bl][col_bl] != 1):
                x_pos -= dist
        
    if event.key == pygame.K_RIGHT:
        # Repeat, as above, but for the right key press
        row_tr, col_tr = get_cell(grid_size, sq_num, tr[0] + dist, tr[1])
        row_br, col_br = get_cell(grid_size, sq_num, br[0] + dist, br[1])
        if(x_pos+sq_size < grid_size):
            if(grid[row_tr][col_tr] != 1) and (grid[row_br][col_br] != 1):
                x_pos += dist
    
    if event.key == pygame.K_UP:
        
        # Repeat, as above, but for the up key press
        row_tl, col_tl = get_cell(grid_size, sq_num, tl[0], tl[1] - dist)
        row_tr, col_tr = get_cell(grid_size, sq_num, tr[0], tr[1] - dist)
        if(y_pos > 0):
            if(grid[row_tl][col_tl] != 1) and (grid[row_tr][col_tr] != 1):
                y_pos -= dist
        
    if event.key == pygame.K_DOWN:
        
        # Repeat, as above, but for the down key press
        row_bl, col_bl = get_cell(grid_size, sq_num, bl[0], bl[1] + dist)
        row_br, col_br = get_cell(grid_size, sq_num, br[0], br[1] + dist)
        if(y_pos+sq_size < grid_size):
            if(grid[row_bl][col_bl] != 1 and grid[row_br][col_br] != 1):
                y_pos += dist
    
    
    return x_pos,y_pos 

#########################################

def enemy_move(enemy_x, enemy_y, player_x, player_y, dist, grid, grid_size, sq_num):
    
    #grabs location
    sq_size = grid_size/sq_num
    tl = (enemy_x,enemy_y)
    bl = (enemy_x,enemy_y+sq_size)
    tr = (enemy_x+sq_size,enemy_y)
    br = (enemy_x+sq_size,enemy_y+sq_size)
    
    tl = (tl[0] + .0001, tl[1] + .0001)
    bl = (bl[0] + .0001, bl[1] - .0001)
    tr = (tr[0] - .0001, tr[1] + .0001)
    br = (br[0] - .0001, br[1] - .0001)
    
    #checks if at barrier
    row,col = get_cell(grid_size,sq_num,enemy_x,enemy_y)
     
    #analyzes the distance    
    l_m = get_distance(enemy_x - dist,enemy_y,player_x,player_y)
    r_m = get_distance(enemy_x + dist,enemy_y,player_x,player_y)
    u_m = get_distance(enemy_x,enemy_y - dist,player_x,player_y)
    d_m = get_distance(enemy_x,enemy_y + dist,player_x,player_y)  
    #print(l_m,r_m,u_m,d_m)
    #print(min(l_m,r_m,u_m,d_m)==l_m)
    #left
    if (min(l_m,r_m,u_m,d_m) == l_m):
        #print("left")
        row_tl, col_tl = get_cell(grid_size, sq_num, tl[0] - dist, tl[1])
        row_bl, col_bl = get_cell(grid_size, sq_num, bl[0] - dist, bl[1])
        if(enemy_x>0):
            if (grid[row_tl][col_tl] != 1) and (grid[row_bl][col_bl] != 1):
                enemy_x -= (dist/5)
                
    #right
    if (min(l_m,r_m,u_m,d_m) == r_m): 
        #print("right")
        row_tr, col_tr = get_cell(grid_size, sq_num, tr[0] + dist, tr[1])
        row_br, col_br = get_cell(grid_size, sq_num, br[0] + dist, br[1])
        if(x_pos+sq_size < grid_size):
            if(grid[row_tr][col_tr] != 1) and (grid[row_br][col_br] != 1):
                enemy_x += (dist/5)
    #up
    if (min(l_m,r_m,u_m,d_m) == u_m):     
        #print("up")
        row_tl, col_tl = get_cell(grid_size, sq_num, tl[0], tl[1] - dist)
        row_tr, col_tr = get_cell(grid_size, sq_num, tr[0], tr[1] - dist)
        if(enemy_y > 0):
              if(grid[row_tl][col_tl] != 1) and (grid[row_tr][col_tr] != 1):
                enemy_y -= (dist/5)
                
    #down
    if (min(l_m,r_m,u_m,d_m) == d_m): 
        #print("down")
        row_bl, col_bl = get_cell(grid_size, sq_num, bl[0], bl[1] + dist)
        row_br, col_br = get_cell(grid_size, sq_num, br[0], br[1] + dist)
        if(enemy_y+sq_size < grid_size):
            if(grid[row_bl][col_bl] != 1 and grid[row_br][col_br] != 1):
                enemy_y += (dist/5)
    
    return enemy_x, enemy_y


#########################################
# Generates a grid as a list structure
# with squares being placed randomly

# prob is the probability that a 1 shows up
# sq_num is the number of square in each row and column
#########################################

def generate_grid(prob,sq_num):
    grid = []
    
    # Your code here
    for rows in range(0,sq_num):
        grid.append(sq_num*[0])
        
    for list1 in range(0,sq_num):
        for element in range(0,sq_num):
            if (random.random() <= prob):
                grid[list1][element] = 1

    return grid


#########################################
# Use the grid generated by generate_grid()
# and draw on the display surface

# grid is the list structure with 1 if a barrier will be plotted there, 0 otherwise
# sq_size is the length and width of each cell within the grid
# sq_num is the number of squares in each row and column
# surf is the name of the display surface to which we are plotting in pygame
# im is the name of the image representing the barrier image
#########################################

def draw_barrier(grid, sq_size, sq_num, surf,b_im):
    
    # Your code here
    for row in range(0,sq_num):
        for col in range(0,sq_num):
            if grid[row][col] == 1:
                surf.blit(b_im, (sq_size*col, sq_size*row))
            #if grid[row][col] == 2:
            #    surf.blit(t_im, (sq_size*col, sq_size*row))
                
                               

#########################################
# Given the player's current location as 
# the coordinate (x_player,y_player), 
# returns the cell row/column pair 
# corresponding to its location in the grid

# m is the length and width of the game window
# cell_num is the number of cells in each row and column
#########################################
def get_cell( m, cell_num, x_player, y_player):
    
    # Your code here
    sq_size = m/cell_num
    
    row = int( y_player/sq_size )
    col = int( x_player/sq_size )
    
    return (row, col)


#########################################
# Given knowledge of an x position and y position
# produces a 4-tuple of the physical coordinates of each of the 
# four corners of the square

# m is the length and width of the game window
# cell_num is the number of cells in each row and column
# x is the current x position
# y is the current y position
#########################################

def corner_points(m, cell_num, x, y):
    
    # Your code here
    sq_size = m/cell_num
    
    top_left = (x, y)
    top_right = (x + sq_size, y)
    bottom_left = (x, y + sq_size)
    bottom_right = (x + sq_size,y + sq_size)
    
    return [top_left, top_right, bottom_left, bottom_right ]

####################################################
####################################################
# Begin procedure for main game loop
####################################################
####################################################

# Import statements
import pygame, sys
from pygame.locals import *
import random

# Define some constants
x_pos = 0 # Player initial x position
y_pos = 0 # Player initial y position
GRID_SIZE = 600 # Pixels x Pixels of console size
SQ_NUM = 10 # Number of squares in grid
SQ_SIZE = int(GRID_SIZE/SQ_NUM) # Dimension of each square
SCORE = 0
LIVES = 3

# Boiler plate startup stuff
pygame.init() 
DISPLAYSURF = pygame.display.set_mode( (GRID_SIZE,GRID_SIZE) )
FPS = 60 
fpsClock = pygame.time.Clock()
pygame.display.set_caption('Run Squidward Run')


# Generate the grid to be used in the game loop
SQ_NUM = 10
grid = generate_grid(0.2, SQ_NUM)
# print(grid)


#Define initial enemy locations - set them randomly in the game frame, but avoid cells with barriers
empty_cells = []
for row in range(0,SQ_NUM):
    for col in range(0,SQ_NUM):
        if grid[row][col] == 0:
            empty_cells.append((col,row))
            

enemy1_start_cell = random.choice(empty_cells)
enemy2_start_cell = random.choice(empty_cells)
if(enemy2_start_cell == enemy1_start_cell):
    enemy2_start_cell = random.choice(empty_cells)            
enemy1_x = enemy1_start_cell[0]*SQ_SIZE  # had to add 1, and reverse order
enemy1_y = enemy1_start_cell[1]*SQ_SIZE  # because get cell is reversed
enemy2_x = enemy2_start_cell[0]*SQ_SIZE
enemy2_y = enemy2_start_cell[1]*SQ_SIZE

#** Define treasure locations, only 3
           
tr1_cell = random.choice(empty_cells)            
tr2_cell = random.choice(empty_cells)            
if(tr2_cell == tr1_cell):
    tr2_cell = random.choice(empty_cells)
tr3_cell = random.choice(empty_cells)
if(tr3_cell == tr1_cell or tr3_cell == tr2_cell):
    tr3_cell = random.choice(empty_cells)
    
tr1_x = tr1_cell[0]*SQ_SIZE
tr1_y = tr1_cell[1]*SQ_SIZE
tr2_x = tr2_cell[0]*SQ_SIZE
tr2_y = tr2_cell[1]*SQ_SIZE
tr3_x = tr3_cell[0]*SQ_SIZE
tr3_y = tr3_cell[1]*SQ_SIZE

#print(grid)
#print(empty_cells)
#print(tr1_cell)
#print(tr2_cell)
#print(tr3_cell)
#print(enemy1_start_cell)
#print(enemy2_start_cell)

tr1_col,tr1_row = tr1_cell
grid[tr1_col][tr1_row] = 2
tr2_col,tr2_row = tr2_cell
grid[tr2_col][tr2_row] = 2
tr3_col,tr3_row = tr3_cell
grid[tr3_col][tr3_row] = 2
#print(grid)

# boolean truth conditions:
tr1 = True
tr2 = True
tr3 = True


####################################################
# Change FILENAME.png to the file name of your image. Note that .jpg and .gif will also work
####################################################
player_im = pygame.image.load("squidward.png")
player_im = pygame.transform.scale(player_im, (SQ_SIZE, SQ_SIZE))
enemy_im = pygame.image.load("spongebob.png")
enemy_im = pygame.transform.scale(enemy_im, (SQ_SIZE, SQ_SIZE))
barrier_im = pygame.image.load("brick.png")
barrier_im = pygame.transform.scale(barrier_im, (SQ_SIZE, SQ_SIZE))

#** treasure image - squidwards clarinet:
treasure_im = pygame.image.load("clarinet.png")
treasure_im = pygame.transform.scale(treasure_im, (SQ_SIZE, SQ_SIZE))

# initialize score scree printout
font = pygame.font.Font('freesansbold.ttf', 30) # sets the font and size of the text 

# Main game loop
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if (SCORE == 3 or LIVES == 0): # repeat condition
            ####################################################
            # Define some constants
            x_pos = 0 # Player initial x position
            y_pos = 0 # Player initial y position
            GRID_SIZE = 600 # Pixels x Pixels of console size
            SQ_NUM = 10 # Number of squares in grid
            SQ_SIZE = int(GRID_SIZE/SQ_NUM) # Dimension of each square
            SCORE = 0
            LIVES = 3
            SQ_NUM = 10
            grid = generate_grid(0.2, SQ_NUM)
            
    
            # Boiler plate startup stuff
            pygame.init() 
            DISPLAYSURF = pygame.display.set_mode( (GRID_SIZE,GRID_SIZE) )
            FPS = 60 
            fpsClock = pygame.time.Clock()
            pygame.display.set_caption('Run Squidward Run')
            
            
            # Generate the grid to be used in the game loop
            SQ_NUM = 10
            grid = generate_grid(0.2, SQ_NUM)
            # print(grid)
            
            
            #Define initial enemy locations - set them randomly in the game frame, but avoid cells with barriers
            empty_cells = []
            for row in range(0,SQ_NUM):
                for col in range(0,SQ_NUM):
                    if grid[row][col] == 0:
                        empty_cells.append((col,row))
                        
            
            enemy1_start_cell = random.choice(empty_cells)            
            enemy2_start_cell = random.choice(empty_cells)
            if(enemy2_start_cell == enemy1_start_cell):
                enemy2_start_cell = random.choice(empty_cells)    
            enemy1_x = enemy1_start_cell[0]*SQ_SIZE  # had to add 1, and reverse order
            enemy1_y = enemy1_start_cell[1]*SQ_SIZE  # because get cell is reversed
            enemy2_x = enemy2_start_cell[0]*SQ_SIZE
            enemy2_y = enemy2_start_cell[1]*SQ_SIZE
            
            #** Define treasure locations, only 3
                       
            tr1_cell = random.choice(empty_cells)            
            tr2_cell = random.choice(empty_cells)            
            if(tr2_cell == tr1_cell):
                tr2_cell = random.choice(empty_cells)
            tr3_cell = random.choice(empty_cells)
            if(tr3_cell == tr1_cell or tr3_cell == tr2_cell):
                tr3_cell = random.choice(empty_cells)
            tr1_x = tr1_cell[0]*SQ_SIZE
            tr1_y = tr1_cell[1]*SQ_SIZE
            tr2_x = tr2_cell[0]*SQ_SIZE
            tr2_y = tr2_cell[1]*SQ_SIZE
            tr3_x = tr3_cell[0]*SQ_SIZE
            tr3_y = tr3_cell[1]*SQ_SIZE
            
            #print(grid)
            #print(empty_cells)
            #print(tr1_cell)
            #print(tr2_cell)
            #print(tr3_cell)
            #print(enemy1_start_cell)
            #print(enemy2_start_cell)
            
            tr1_col,tr1_row = tr1_cell
            grid[tr1_col][tr1_row] = 2
            tr2_col,tr2_row = tr2_cell
            grid[tr2_col][tr2_row] = 2
            tr3_col,tr3_row = tr3_cell
            grid[tr3_col][tr3_row] = 2
            #print(grid)
            
            # boolean truth conditions:
            tr1 = True
            tr2 = True
            tr3 = True
            ####################################################
        
        p_tl, p_tr, p_bl, p_br = corner_points(GRID_SIZE, SQ_NUM, x_pos, y_pos)
        pmin_x = p_tl[0]
        pmin_y = p_tl[1]
        pmax_x = p_br[0]
        pmax_y = p_br[1]
        
        e1_tl, e1_tr, e1_bl, e1_br = corner_points(GRID_SIZE, SQ_NUM, enemy1_x, enemy1_y)
        e1min_x = e1_tl[0]
        e1min_y = e1_tl[1]
        e1max_x = e1_br[0]
        e1max_y = e1_br[1]
        
        e2_tl, e2_tr, e2_bl, e2_br = corner_points(GRID_SIZE, SQ_NUM, enemy2_x, enemy2_y)
        e2min_x = e2_tl[0]
        e2min_y = e2_tl[1]
        e2max_x = e2_br[0]
        e2max_y = e2_br[1]
        
        if(((e1min_x <= pmin_x <= e1max_x) or (e1min_x <= pmax_x <= e1max_x)) and ((e1min_y <= pmin_y <= e1max_y) or (e1min_y <= pmax_y <= e1max_y))):
            LIVES-=1
            x_pos = 0
            y_pos = 0
        
        if(((e2min_x <= pmin_x <= e2max_x) or (e2min_x <= pmax_x <= e2max_x)) and ((e2min_y <= pmin_y <= e2max_y) or (e2min_y <= pmax_y <= e2max_y))):
            LIVES-=1
            x_pos = 0
            y_pos = 0
        
        
        
        # test grid catch
        row, col = get_cell( GRID_SIZE, SQ_NUM, x_pos, y_pos)
        row1, col1 = get_cell( GRID_SIZE, SQ_NUM, (x_pos+SQ_SIZE-.005), y_pos)
        row2, col2 = get_cell( GRID_SIZE, SQ_NUM, x_pos, (y_pos+SQ_SIZE-.005))
        row3, col3 = get_cell( GRID_SIZE, SQ_NUM, (x_pos+SQ_SIZE-.005), (y_pos+SQ_SIZE-.005))
        
        check = col,row
        check1 = col1,row1
        check2 = col2,row2
        check3 = col3,row3
        
        #print(check)
        #print(col,row)
        #print(grid[col][row])
        if (grid[col][row] == 2 or grid[col1][row1] == 2 or grid[col2][row2] == 2 or grid[col3][row3] == 2):
            if (check == tr1_cell or check1 == tr1_cell or check2 == tr1_cell or check3 == tr1_cell):
                tr1 = False
                grid[tr1_col][tr1_row] = 0
            elif (check == tr2_cell or check1 == tr2_cell or check2 == tr2_cell or check3 == tr2_cell):
                tr2 = False
                grid[tr2_col][tr2_row] = 0
            elif (check == tr3_cell or check1 == tr3_cell or check2 == tr3_cell or check3 == tr3_cell):
                tr3 = False
                grid[tr3_col][tr3_row] = 0
    
            SCORE += 1
            if SCORE == 3:
                pygame.display.set_caption('PRESS ANY ARROW-KEY TO CONTINUE')
            #print(SCORE)
            
        # Update Score:
        text = 'Score: '+str(SCORE) 
        text = font.render(text, True, (50,50,50), (100,100,100)) #This renders the text
        textRect = text.get_rect() # Creates a rectangular object for the text
        textRect.center = (100, 200) # Places the center of the text at (100,200) on the screen    
        
        #Update Lives:
        text1 = 'Lives: '+str(LIVES) 
        text1 = font.render(text1, True, (50,50,50), (100,100,100)) #This renders the text
        textRect1 = text1.get_rect() # Creates a rectangular object for the text
        textRect1.center = (400, 200) # Places the center of the text at (200,200) on the screen 
     
        
        # Fill the surface background with the RGB color
        DISPLAYSURF.fill( (204,255,255) )
        
        # Draw the barriers based on values in the grid list
        # created before the game loop
        draw_barrier(grid, 60, SQ_NUM, DISPLAYSURF, barrier_im)
        
        # Check to see if a button has been pressed.
        # If an arrow key has been pressed, call the move() function and determine new x and y coordinates.
        if event.type == pygame.KEYDOWN:
            
            x_pos,y_pos = move(x_pos, y_pos, 5, grid, GRID_SIZE, SQ_NUM)
    
        #Get new coordinates the enemies will move to
        enemy1_x, enemy1_y = enemy_move(enemy1_x, enemy1_y, x_pos, y_pos, 1, grid, GRID_SIZE, SQ_NUM)
        enemy2_x, enemy2_y = enemy_move(enemy2_x, enemy2_y, x_pos, y_pos, 1, grid, GRID_SIZE, SQ_NUM)
             
        # Draw player and both enemy images to the screen using the blit() function
        DISPLAYSURF.blit(player_im, (x_pos,y_pos))
        DISPLAYSURF.blit(enemy_im, (enemy1_x, enemy1_y))
        DISPLAYSURF.blit(enemy_im, (enemy2_x, enemy2_y))
        if (tr1):
            DISPLAYSURF.blit(treasure_im, (tr1_x, tr1_y))
        if (tr2):
            DISPLAYSURF.blit(treasure_im, (tr2_x, tr2_y))
        if (tr3):
            DISPLAYSURF.blit(treasure_im, (tr3_x, tr3_y))
        DISPLAYSURF.blit(text,textRect)
        DISPLAYSURF.blit(text1,textRect1)

        
    # Advance the game counter
    pygame.display.update()
    fpsClock.tick(FPS)
