#Developing a similar game to the pythonprogramming.net but in a different way

'''
Author: Olaoluwa Raji
Inspired by sentdex pythonprogramming.net
'''
import pygame
import random
import time
from pygame.locals import*
pygame.init()

GameDifficulty = 1#(Default) #int(input('Enter the difficulty level:'))
display_width = 800#int(input('display width:'))
display_height = 500#int(input('display height:'))

screen = pygame.display.set_mode((display_width,display_height))
title = pygame.display.set_caption('BLOXX')
ROBOT = pygame.image.load('Robot.png').convert_alpha()

RobotIcon = pygame.image.load('RobotIcon.png').convert_alpha() #Game's Icon
pygame.display.set_icon(RobotIcon) #Adding Game's Icon to screen

######BACKGROUND COLOURS########
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
##Darker shades
dark_red = (180,0,0)
dark_green = (0,180,0)
dark_blue = (0,0,150)
################################

def RobotImage(X,Y):
    screen.blit(ROBOT,(X,Y))

#Function to change colour of button when cursor is around it
def Blink(colour):
    if colour == dark_red:
        return red
    elif colour == dark_green:
        return green
    elif colour == dark_blue:
        return blue

#Buttons for Game Menu (Title of game , Start button , Quit Button)
ButtonFont = pygame.font.SysFont('Freesanbold.ttf',60)

#Function for displaying level of difficulty --> (to appear in the SETTINGS)  , for explaining how to play the game --> (to appear in HELP)
def Msg(info):
    Font = pygame.font.SysFont('freesanbold.ttf',57)
    message = Font.render(info,True,white)
    Mode = message.get_rect()
    Mode.center = (550,455)
    screen.blit(message,(Mode))
    
#The CreateButton function creates game buttons to perform certain actions
def CreateButton(text,button_x,button_y,button_width,button_height,colour = red):
    global GameDifficulty
    ''' Create button given the following parameters:
    text = information on the button
    button_x = x position of button
    button_y = y position of button
    button_width = width of button
    button_height = height of button
    colour = colour of button (red by default)
    '''
    #mouse position = mouse_x , mouse_y
    mouse_x , mouse_y = pygame.mouse.get_pos()
    pygame.draw.rect(screen,colour,[button_x,button_y,button_width,button_height])
    
    if button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height:
        pygame.draw.rect(screen,Blink(colour),[button_x,button_y,button_width,button_height])
        #click -> if click[0] = 1 then left clicking the buttons makes them perform their action
        click = pygame.mouse.get_pressed()
        
        if click[0] == 1 and text == 'START':
            time.sleep(0.8)
            GameLoop()
    
        elif click[0] == 1 and text == 'QUIT':
            pygame.quit()
            quit()

        elif click[0] == 1 and text == 'SETTINGS':
            time.sleep(1)
            SETTINGS()

        elif click[0] == 1 and text == 'HELP':
            time.sleep(1)
            HELP()

        elif click[0] == 1 and text == 'ABOUT':
            time.sleep(1)
            ABOUT()

        elif click[0] == 1 and text == 'BACK':
            GameMenu()
    
        elif click[0] == 1 and text == 'EASY':
            GameDifficulty = 1
    
        elif click[0] == 1 and text == 'MEDIUM':
            GameDifficulty = 2
        
        elif click[0] == 1 and text == 'HARD':
            GameDifficulty = 3
            
        elif click[0] == 1 and text == 'VERY HARD':
            GameDifficulty = 4
            
    BoldText = ButtonFont.render(text,True,black)
    Rect = BoldText.get_rect()
    Rect.center = (button_x + (button_width / 2)) , (button_y + (button_height / 2))
    screen.blit(BoldText,Rect)
    
def GameMenu():
    intro = False
    while not intro:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        screen.fill(white)
        CreateButton('START',30,250,137,60,dark_green)
        CreateButton('QUIT',800 - 30 - 137,250,137,60,dark_red)
        CreateButton('SETTINGS',332 - 50,250,215,60,dark_blue)
        CreateButton('ABOUT',150,380,165,60,dark_red)
        CreateButton('HELP',495,380,137,60,dark_green)
        #Game Title#
        bloxx_txt = 'BLOXX!!'
        bloxx_font = pygame.font.SysFont('freesanbold.ttf',65)
        Bloxx_text = bloxx_font.render(bloxx_txt,True,black)
        
        pos_of_title = Bloxx_text.get_rect()
        pos_of_title.center = (display_width / 2 - 10 , 40)
        
        screen.blit(Bloxx_text,pos_of_title)
        RobotImage(display_width / 2 - 40 , 100)
        
        pygame.display.update()
###########################################            

#CODE -> FUNCTIONALITIES OF BUTTONS IN THE GAME MENU
def SETTINGS():

    #Info on settings screen
    diff = 'Difficulty: '
    diff_font = pygame.font.SysFont('freesanbold.ttf',57)
    BoldDiff = diff_font.render(diff,True,white)
    
    settings = False
    while not settings:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameMenu()
        screen.fill(red)
        screen.blit(BoldDiff,(30,30))
        CreateButton('EASY',260,30,125,50,dark_blue)
        CreateButton('MEDIUM',260,100,170,50,dark_blue)
        CreateButton('HARD',260,170,125,50,dark_blue)
        CreateButton('VERY HARD',260,240,252,50,dark_blue)
        CreateButton('BACK',30,430,125,50,dark_blue)

        if GameDifficulty == 1:
            Msg('MODE : EASY')
        elif GameDifficulty == 2:
            Msg('MODE : MEDIUM')
        elif GameDifficulty == 3:
            Msg('MODE : HARD')
        elif GameDifficulty == 4:
            Msg('MODE : VERY HARD')    
        pygame.display.update()
        
def ABOUT():
    About = False
    while not About:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameMenu()
        screen.fill(white)
        help_msg('BLOXX is a simple game in which the player has to dodge falling obstacles',15,10)
        help_msg("Basic idea and inspiration for the game owes to sentdex's 'A bit Racey Game'",15,50)
        help_msg('This game was created using complete procedural programming',15,90)
        help_msg('Possible corrections and suggestions would be appreciated as this is an open source project',15,130)
        help_msg('Gmail : olaoluwaraji1999@gmail.com',15,210)
        help_msg('Author : Olaoluwa Raji',15,250)
        help_msg('Date created : 02-06-2018',15,290)
        help_msg('Date modified: 29-06-2023',15,330)
        CreateButton('BACK',30,430,120,48,dark_blue)
        pygame.display.update()
        
## help_msg is used for writing text into ABOUT menu as well ##
def help_msg(help_text,pos1,pos2):
    ''' (pos1,pos2) represent the coordinates in which
    help_text is added to screen
    '''
    help_font = pygame.font.SysFont('freesanbold.ttf',25)
    disp_help = help_font.render(help_text,True,black)
    screen.blit(disp_help,(pos1,pos2))
################################################
    
## HELP FUNCTION ##
def HELP():
    Help = False
    while not Help:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameMenu()

        screen.fill(white)
        help_msg(' -> The arrow keys are used for navigating through 8 possible directions',10,10)
        help_msg(' -> The forward key : Move Right',10,50)
        help_msg(' -> The backward key : Move Left',10,90)
        help_msg(' -> The up key : Move Up',10,130)
        help_msg(' -> The down key : Move Down',10,170)
        help_msg('The aim of the game is to dodge falling obstacles (red and black)',10,220)
        help_msg('Difficulties can be adjusted in the SETTINGS menu',10,260)
        help_msg('The higher the difficulty, the faster the obstacles',10,300)
        help_msg('Press P to pause the game and Q to resume',10,340)
        help_msg('Diagonal movements are possible when two adjacent arrow keys are combined',10,370)
        CreateButton('BACK',30,430,120,48,dark_blue)
        pygame.display.update()
##########################################
        
#CODE -> Displays a message when player crashes into barriers or falling obstacles
text = 'Game Over'
font = pygame.font.SysFont('freesanbold.ttf',100)
def GameOver():
    BoldText = font.render(text,True,blue)
    Rect = BoldText.get_rect()
    Rect.center = (display_width / 2,display_height / 2)
    screen.blit(BoldText,Rect)
    pygame.display.update()
    time.sleep(2)
    GameLoop()
#################################

#CODE -> Displays points earned i.e number of obstacles avoided
#Value(value) reveals the player's score 
def Value(value):
    value_font = pygame.font.SysFont('freesanbold.ttf',50)
    BoldValue = value_font.render(value,True,blue)
    screen.blit(BoldValue,(20,20))
    pygame.display.update()
################################
    
#CODE -> Creates falling obstacles that must be avoided
def obstacles(obsX,obsY,obsW,obsH):
    pygame.draw.rect(screen,black,(obsX,obsY,obsW,obsH))

def minor_red_obstacles(obsX,obsY,obsW,obsH):
    pygame.draw.rect(screen,red,(obsX,obsY,obsW,obsH))
#################################
  
#CODE -> GameLoop() controls most activities of the game
def GameLoop():
    #Initial score = 0
    score = '0'
    int_score = int(score)
    
    x = random.randrange(int(display_width / 3),int(display_width / 1.5))#display_width  / 2
    y = random.randrange(int(display_height / 3),int(display_height / 1.5))#display_height / 1.5
    x_change = 0
    y_change = 0

    #####PARAMETERS FOR FALLING OBSTACLE#########
    obstacle_width = ROBOT.get_width() + 10
    obstacle_height = ROBOT.get_height() + 10
    obs_startx = random.randint(20,display_width - 20 - obstacle_width)
    obs_starty = -750
    #obstacle speed determines the game's difficulty
    if GameDifficulty == 1:
        obs_speed = 1.75 * GameDifficulty
    if GameDifficulty == 2:
        obs_speed = 1.25 * GameDifficulty 
    if GameDifficulty == 3:
        obs_speed = 0.98 * GameDifficulty 
    if GameDifficulty == 4:
        obs_speed = 0.85 * GameDifficulty 
    #############################################

    ######PARAMETERS FOR MINOR RED OBSTACLE######
    red_obstacle_width = ROBOT.get_width() - 10
    red_obstacle_height = ROBOT.get_height() - 10
    red_obs_startx = random.randint(40,display_width - 30 - obstacle_width)
    red_obs_starty = -1000
    #obstacle speed determines the game's difficulty
    if GameDifficulty == 1:
        red_obs_speed = 1.95 * GameDifficulty
    if GameDifficulty == 2:
        red_obs_speed = 1.4 * GameDifficulty 
    if GameDifficulty == 3:
        red_obs_speed = 1.02 * GameDifficulty 
    if GameDifficulty == 4:
        red_obs_speed = 0.9 * GameDifficulty 
    ##############################################
    storage1 = obs_speed #This variable keeps the black obstacle's speed in case game is paused and then resumed
    storage2 = red_obs_speed#This variable keeps the red obstacle's speed in case game is paused and then resumed
    ##############################################
    Exit = False
    while not Exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               GameMenu()
                
            if event.type == pygame.KEYDOWN:
                
                    if event.key == pygame.K_LEFT:
                        x_change = -1.98
                    elif event.key == pygame.K_RIGHT:
                        x_change = 1.98 
                    elif event.key == pygame.K_UP:
                        y_change = -1.98
                    elif event.key == pygame.K_DOWN:
                        y_change = 1.98
                    #####EVENT FOR PAUSING AND RESUMING GAME########
                    elif event.key == pygame.K_p:
                        obs_speed = 0
                        red_obs_speed = 0
                    elif event.key == pygame.K_q:
                        obs_speed = storage1
                        red_obs_speed = storage2
              ###################################          
            elif event.type == pygame.KEYUP:
                x_change = 0
                y_change = 0
        #When Game is not paused the obstacles are in motion then player can change position
        if obs_speed != 0 and red_obs_speed != 0:
            x += x_change
            y += y_change
        #The else..clause handles a condition in which the game is paused hence player's displacement = 0
        else:
            x_change = 0
            y_change = 0
        ################################
        screen.fill(white)
        RobotImage(x,y)
        #########BOUNDARIES#############
        pygame.draw.line(screen,black,(20,0),(20,display_height - 20))
        pygame.draw.line(screen,black,(display_width - 20,0),(display_width - 20,display_height - 20))
        pygame.draw.line(screen,black,(20,display_height - 20),(display_width - 20,display_height - 20))
        ################################
        if x < 20 or x > display_width - 20 - ROBOT.get_width() or y > display_height - 20 - ROBOT.get_height() or y < 0:
            GameOver()
            score = 0 #Score is 0 until obstacle is avoided

        obstacles(obs_startx,obs_starty,obstacle_width,obstacle_height)
        obs_starty += obs_speed

        minor_red_obstacles(red_obs_startx,red_obs_starty,red_obstacle_width,red_obstacle_height)
        red_obs_starty += red_obs_speed
        ##CALLING Value Function to display player's successful points
        Value('Score : ' + score)
    
        if obs_starty > display_height:
            obs_starty = -200
            obs_startx = random.randint(20,display_width - 20 - obstacle_width)
            ##CODE -> For increase in score
            int_score += 1
            score = str(int_score) #Score increases by 1 after a successful dodge of major obstacle

        if red_obs_starty > display_height:
            red_obs_starty = -500
            red_obs_startx = random.randint(40,display_width - 30 - obstacle_width)
            ##CODE -> For increase in score
            int_score += 1
            score = str(int_score) #Score increases by 1 after a successful dodge of minor red obstacle

        ##This condition works if obstacle is left of the player (x - obs_startx <= obstacle_width and y - obs_starty <= obstacle_height)
        ##This condition works if obstacle is right of the player (obs_startx - x <= obstacle_width and obs_starty - y <= obstacle_height)
        if (x - obs_startx <= obstacle_width and y - obs_starty <= obstacle_height) and (obs_startx - x <= obstacle_width - 10 and obs_starty - y <= obstacle_height - 10):
            GameOver()
            score = 0 #Score is 0 until major obstacle is avoided

        if (x - red_obs_startx <= red_obstacle_width and y - red_obs_starty <= red_obstacle_height) and (red_obs_startx - x <= red_obstacle_width - 10 and red_obs_starty - y <= red_obstacle_height - 10):
            GameOver()
            score = 0 #Score is 0 until minor red obstacle is avoided
        pygame.display.update()
       
GameMenu()
pygame.quit()
