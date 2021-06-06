import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((1000, 700))

white = (255, 255, 255)
pygame.display.set_caption("Game Of Goose")

# bckground image
BOARD = pygame.image.load('BOARD2.png')
arrow = pygame.image.load('playnow.png')
arrow = pygame.transform.scale(arrow,(100,100))
logo = pygame.image.load('LOG.png')
logo= pygame.transform.scale(logo,(120,120))
title = pygame.image.load('TITLE.png')
title= pygame.transform.scale(title,(300,140))
player1 = pygame.image.load('player1.png')
player2 = pygame.image.load('player2.png')
player1= pygame.transform.scale(player1,(210,100))
player2= pygame.transform.scale(player2,(210,100))



# players
r1 = pygame.image.load('red.png')
b1 = pygame.image.load('blue.png')

rx=209
ry=259

bx=209
by=403

button = pygame.Rect(0, 30, 70,70)

score_font = pygame.font.SysFont("Arial Rounded MT Bold", 28)

clock = pygame.time.Clock()

def rollb():
    
    value= score_font.render("Your turn.....", True, (255, 255, 255))
    screen.blit(value, [12, 480])
    
def rollr():
    
    value= score_font.render("Your turn.....", True, (255, 255, 255))
    screen.blit(value, [12, 310])    
    


def bck():
    screen.blit(BOARD, (0,0))
    screen.blit(arrow, (0,30))
    screen.blit(logo, (875,537))
    screen.blit(title, (580,520))
    screen.blit(player1, (-5,230))
    screen.blit(player2, (-20,390))


def rplayer(x, y):
    screen.blit(r1, (x, y))

def bplayer(x, y):
    screen.blit(b1, (x, y))


def pickNumber():
    
    diceroll = random.randint(1, 6)
    if diceroll == 1:
        dice = pygame.image.load("1.png")
        dice = pygame.transform.scale(dice,(90,90))
    elif diceroll == 2:
        dice = pygame.image.load("2.png")
        dice = pygame.transform.scale(dice,(90,90))
    elif diceroll == 3:
        dice = pygame.image.load("3.png")
        dice = pygame.transform.scale(dice,(90,90))
    elif diceroll == 4:
        dice = pygame.image.load("4.png")
        dice = pygame.transform.scale(dice,(90,90))
    elif diceroll == 5:
        dice = pygame.image.load("5.png")
        dice = pygame.transform.scale(dice,(90,90))
    elif diceroll == 6:
        dice = pygame.image.load("6.png")
        dice = pygame.transform.scale(dice,(90,90))

    return (dice,diceroll)    
    
# game loop

running = True

turn = 'red'

while running:
    screen.fill((0, 255, 195))
    
    bck()
    if turn=='red':
        rollr()
    
    if turn=='blue':
        rollb()
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        


        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button.collidepoint(mouse_pos):
                  pickNumber()
                  dice,diceroll = pickNumber()
                
                  screen.blit(dice, (209, 55))
                  print(diceroll)

             #for player1
            if pickNumber() and turn=='red':
                turn='blue'
                if diceroll == 6 and rx==209 and ry==259:
                    rx=329
                    ry=403
                    
                    turn='red'
                elif diceroll == 6 and rx ==329 and ry==403:
                    rx=rx+(64*6)
                    ry=403
                    turn='red'
                elif diceroll == 6 and rx ==393 and ry==403:
                    rx=rx+(64*6)
                    ry=403
                    turn='red'
                elif diceroll == 6 and rx ==457 and ry==403:
                    rx=841
                    ry=403
                    if rx==841 and ry==403:
                         rx=905
                         ry=403
                    turn='red'
                elif diceroll == 6 and rx ==521 and ry==403:
                    rx=rx+(64*6)
                    ry=403
                    turn='red'
                elif  diceroll == 4 and rx == 329 and ry==403:
                    rx=585
                    ry=403
                    if rx==585 and ry==403:
                         rx=905
                         ry=403
                    
                elif  diceroll < 5 and diceroll != 4 and  rx == 329 and ry==403:
                    rx=rx+(64*diceroll)
                    ry=403
                elif  diceroll == 5 and rx == 329 and ry==403:
                    rx=649
                    ry=403
                    if rx==649 and ry==403:
                         rx=905
                         ry=263
                
                    

                elif  diceroll <= 5 and diceroll != 3 and diceroll != 4 and rx == 393 and ry==403:
                    rx=rx+(64*diceroll)
                    ry=403
                elif  diceroll == 3 and rx == 393 and ry==403:
                    rx=585
                    ry=403
                    if rx==585 and ry==403:
                         rx=905
                         ry=403
                elif  diceroll == 4 and rx == 393 and ry==403:
                    rx=649
                    ry=403
                    if rx==649 and ry==403:
                         rx=905
                         ry=263         
                elif  diceroll <= 5 and rx == 457 and diceroll !=2 and diceroll !=3  and ry==403:
                    rx=rx+(64*diceroll)
                    ry=403
                elif  diceroll == 2 and rx == 457 and ry==403:
                    rx=585
                    ry=403
                    if rx==585 and ry==403:
                         rx=905
                         ry=403
                elif  diceroll == 3 and rx == 457 and ry==403:
                    rx=649
                    ry=403
                    if rx==649 and ry==403:
                         rx=905
                         ry=263          
                elif  diceroll < 5 and diceroll !=1 and diceroll !=2 and rx == 521 and ry==403:
                    rx=rx+(64*diceroll)
                    ry=403
                elif  diceroll == 1 and rx == 521 and ry==403:
                    rx=585
                    ry=403
                    if rx==585 and ry==403:
                         rx=905
                         ry=403
                elif  diceroll == 2 and rx == 521 and ry==403:
                    rx=649
                    ry=403
                    if rx==649 and ry==403:
                         rx=905
                         ry=263  
                elif  diceroll == 5 and rx == 521 and ry==403:
                    rx=841
                    ry=403
                    if rx==841 and ry==403:
                         rx=905
                         ry=403     
                
                                
                     
                elif rx == 713 and diceroll == 6 and  ry==403:
                   rx=rx+(64*3)
                   ry=ry-(70*3)
                   turn='red'
                elif rx == 713 and diceroll <= 3 and diceroll != 2 and  ry==403:
                    rx=rx+(64*diceroll)
                    ry==403
                elif  diceroll == 2 and rx == 713 and ry==403:
                    rx=841
                    ry=403
                    if rx==841 and ry==403:
                         rx=905
                         ry=403    
                elif rx == 713 and diceroll == 4 and  ry==403:
                    rx=rx+(64*3)
                    ry=ry-(70*1)
                elif rx == 713 and diceroll == 5 and  ry==403:
                    rx=rx+(64*3)
                    ry=ry-(70*2)
                                      
                elif rx == 777 and diceroll == 3 and  ry==403:
                   rx=rx+(64*2)
                   ry=ry-(70*1)
                elif rx == 777 and diceroll == 4 and  ry==403:
                   rx=rx+(64*2)
                   ry=ry-(70*2)
                elif rx == 777 and diceroll ==5 and  ry==403:
                   rx=rx+(64*2)
                   ry=ry-(70*3)       
                elif rx == 777 and diceroll < 2 and  ry==403:
                    rx=rx+(64*diceroll)
                    ry=403
                elif  diceroll == 2 and rx == 777 and ry==403:
                    rx=841
                    ry=403
                    if rx==841 and ry==403:
                         rx=905
                         ry=403      
                elif rx == 777 and diceroll == 6 and  ry==403:
                    rx=905
                    ry=123
                    if rx==905 and ry==123:
                         rx=329
                         ry=193
                    turn='red'
                
                elif diceroll == 6 and ry==403 and rx==905:
                    ry=ry-(70*6)
                    rx=905
                    turn='red'
                elif diceroll <= 5 and diceroll !=4 and ry==403 and rx==905:
                    ry=ry-(70*diceroll)
                    rx=905
                elif rx == 905 and diceroll == 4 and  ry==403:
                    rx=905
                    ry=123
                    if rx==905 and ry==123:
                         rx=329
                         ry=193    
                elif diceroll == 6 and ry==333 and rx==905:
                    ry=ry-(70*5)
                    rx=rx-(64*1)
                    turn='red'
                elif diceroll <= 5 and diceroll != 3  and ry==333 and rx==905:
                    ry=ry-(70*diceroll)
                    rx=905
                elif rx == 905 and diceroll == 3 and  ry==333:
                    rx=905
                    ry=123
                    if rx==905 and ry==123:
                         rx=329
                         ry=193    

                elif diceroll == 6 and ry==263 and rx==905:
                    ry=-17
                    rx=777
                    if rx==777 and ry==-17:
                         rx=585
                         ry=333 
                    turn='red'
                elif diceroll ==5 and ry==263 and rx==905:
                    ry=ry-(70*4)
                    rx=rx-(64*1)
                elif diceroll <=4 and diceroll !=2 and ry==263 and rx==905:
                    ry=ry-(70*diceroll)
                    rx=905
                elif rx == 905 and diceroll == 2 and  ry==263:
                    rx=905
                    ry=123
                    if rx==905 and ry==123:
                         rx=329
                         ry=193     
                elif diceroll == 6 and ry==193 and rx==905:
                    ry=-17
                    rx=713
                    if rx==713 and ry==-17:
                         rx=777
                         ry=403 
                    turn='red'
                elif ry == 193 and diceroll == 5 and  rx==905:
                    ry=-17
                    rx=777
                    if rx==777 and ry==-17:
                         rx=585
                         ry=333 
                elif ry == 193 and diceroll == 4 and  rx==905:
                    ry=ry-(70*3)
                    rx=rx-(64*1)
                elif ry == 193 and diceroll <= 3 and diceroll !=1 and  rx==905:
                    ry=ry-(70*diceroll)
                    rx=905
                elif rx == 905 and diceroll == 1 and  ry==193:
                    rx=905
                    ry=123
                    if rx==905 and ry==123:
                         rx=329
                         ry=193    
                
                elif ry==53 and diceroll == 6 and rx==905:
                    ry=ry-(70*1)
                    rx=rx-(64*5)
                    turn='red'
                elif ry==53 and diceroll == 5 and rx==905:
                    ry=ry-(70*1)
                    rx=rx-(64*4)
                elif ry==53 and diceroll == 4 and rx==905:
                    ry=-17
                    rx=713
                    if rx==713 and ry==-17:
                         rx=777
                         ry=403 
                elif ry==53 and diceroll == 3 and rx==905:
                    ry=-17
                    rx=777
                    if rx==777 and ry==-17:
                         rx=585
                         ry=333 
                elif ry==53 and diceroll == 2 and rx==905:
                    ry=ry-(70*1)
                    rx=rx-(64*1)
                elif ry==53 and diceroll == 1 and rx==905:
                    ry=ry-(70*1)
                    rx=905
                elif ry==-17 and diceroll == 6 and rx ==905:
                    ry=-17
                    rx=rx-(64*6)
                    turn='red'
                elif ry==-17 and diceroll <=5 and diceroll !=2 and diceroll !=3   and rx ==905:
                    ry=-17
                    rx=rx-(64*diceroll)
                elif ry==-17 and diceroll == 2 and rx==905:
                    ry=-17
                    rx=713
                    if rx==713 and ry==-17:
                         rx=777
                         ry=403
                elif ry==-17 and diceroll == 3 and rx==905:
                    ry=-17
                    rx=777
                    if rx==777 and ry==-17:
                         rx=585
                         ry=333         
                elif ry==-17 and diceroll == 6 and rx ==841:
                    ry=-17
                    rx=457
                    if rx==457 and ry==-17:
                         rx=521
                         ry=333
                    turn='red'
                elif ry==-17 and diceroll <=5 and diceroll !=1 and diceroll !=2   and rx ==841:
                    ry=-17
                    rx=rx-(64*diceroll)    
                elif ry==-17 and diceroll == 1 and rx==841:
                    ry=-17
                    rx=777
                    if rx==777 and ry==-17:
                         rx=585
                         ry=333
                elif ry==-17 and diceroll == 2 and rx==841:
                    ry=-17
                    rx=713
                    if rx==713 and ry==-17:
                         rx=777
                         ry=403           
                elif ry==-17 and diceroll == 6 and rx==649:
                    ry=ry+(70*1)
                    rx=rx-(64*5)
                    turn='red'
                elif ry==-17 and diceroll <=5 and diceroll != 3 and rx ==649:
                    ry=-17
                    rx=rx-(64*diceroll)
                elif  ry==-17 and diceroll == 3 and rx ==649:
                    ry=-17
                    rx=457
                    if rx==457 and ry==-17:
                         rx=521
                         ry=333 

                elif ry==-17 and diceroll == 6 and rx==585:
                    ry=ry+(70*2)
                    rx=rx-(64*4)
                    turn='red'
                elif ry==-17 and diceroll == 5 and rx==585:
                    ry=ry+(70*1)
                    rx=rx-(64*4)
                elif ry==-17 and diceroll <= 4 and diceroll != 2 and rx==585:
                    ry=-17
                    rx=rx-(64*diceroll)
                elif  ry==-17 and diceroll == 2 and rx ==585:
                    ry=-17
                    rx=457
                    if rx==457 and ry==-17:
                         rx=521
                         ry=333     

                elif ry==-17 and diceroll == 6 and rx==521:
                    ry=ry+(70*3)
                    rx=rx-(64*3)
                    turn='red'
                elif ry==-17 and diceroll == 5 and rx==521:
                    ry=ry+(70*2)
                    rx=rx-(64*3)
                elif ry==-17 and diceroll == 4 and rx==521:
                    ry=ry+(70*1)
                    rx=rx-(64*3)
                elif ry==-17 and diceroll <= 3 and diceroll != 1 and rx==521:
                    ry=-17
                    rx=rx-(64*diceroll)
                elif  ry==-17 and diceroll == 2 and rx ==5218:
                    ry=-17
                    rx=457
                    if rx==457 and ry==-17:
                         rx=521
                         ry=333     

                elif ry==-17 and diceroll == 6 and rx==393:
                    ry=ry+(70*5)
                    rx=rx-(64*1)
                    turn='red'
                elif ry==-17 and diceroll == 5 and rx==393:
                    ry=ry+(70*4)
                    rx=rx-(64*1)
                elif ry==-17 and diceroll == 4 and rx==393:
                    ry=ry+(70*3)
                    rx=rx-(64*1)
                elif ry==-17 and diceroll == 3 and rx==393:
                    ry=ry+(70*2)
                    rx=rx-(64*1)
                elif ry==-17 and diceroll == 2 and rx==393:
                    ry=ry+(70*1)
                    rx=rx-(64*1)
                elif ry==-17 and diceroll == 1 and rx==393:
                    ry=-17
                    rx=rx-(64*1)
                elif ry==-17 and diceroll == 6 and rx==329:
                    ry=333
                    rx=393
                    if ry==333 and rx == 393:
                         rx =905
                         ry =403
                    turn='red'
                elif ry==-17 and diceroll <= 5 and rx==329:
                    ry=ry+(70*diceroll)
                    rx=329
                elif ry==53 and diceroll == 6 and rx==329:
                    ry=333
                    rx=457
                    if ry==333 and rx == 457:
                         rx =777
                         ry =53
                    turn='red'
                elif ry==53 and diceroll == 5 and rx==329:
                    ry=333
                    rx=393
                    if ry==333 and rx == 393:
                         rx =905
                         ry =403
                elif ry==53 and diceroll <= 4 and rx==329:
                    ry=ry+(70*diceroll)
                    rx=329
                elif ry==123 and diceroll == 6 and rx==329:
                    ry=ry+(70*3)
                    rx=rx+(64*3)
                    turn='red'
                elif ry==123 and diceroll == 5 and rx==329:
                    ry=333
                    rx=457
                    if ry ==333 and rx == 457:
                         rx =777
                         ry =53
                elif ry==123 and diceroll == 4 and rx==329:
                    ry=333
                    rx=393
                    if ry==333 and rx == 393:
                         rx =905
                         ry =403
                elif ry==123 and diceroll <= 3 and rx==329:
                    ry=ry+(70*diceroll)
                    rx=123
                elif ry==193 and diceroll == 6 and rx==329:
                    ry=ry+(70*2)
                    rx=rx+(64*4)
                    turn='red'
                elif ry==193 and diceroll == 5 and rx==329:
                    ry=ry+(70*2)
                    rx=rx+(64*3)
                elif ry==193 and diceroll == 4 and rx==329:
                    ry=333
                    rx=457
                    if ry ==333 and rx ==457:
                         rx =777
                         ry =53
                elif ry==193 and diceroll == 3 and rx==329:
                    ry=333
                    rx=393
                    if ry==333 and rx == 393:
                         rx =905
                         ry =403
                elif ry==193 and diceroll <= 2 and rx==329:
                    ry=ry+(70*diceroll)
                    rx=329
                elif ry==263 and diceroll == 6 and rx==329:
                    ry=333
                    rx=713
                    if ry==333 and rx==713:
                        ry=193
                        rx=777
                    turn='red'
                elif ry==263 and diceroll == 5 and rx==329:
                    ry=ry+(70*1)
                    rx=rx+(64*4)
                elif ry==263 and diceroll == 4 and rx==329:
                    ry=ry+(70*1)
                    rx=rx+(64*3)
                elif ry==263 and diceroll == 3 and rx==329:
                    ry=333
                    rx=457
                    if ry ==333 and rx == 457:
                         rx =777
                         ry =53
                elif ry==263 and diceroll == 2 and rx==329:
                    ry=333
                    rx=393
                    if ry==333 and rx == 393:
                         rx =905
                         ry =403
                elif ry==263 and diceroll == 1 and rx==329:
                    ry=ry+(70*1)
                    rx=329
                elif ry==333 and diceroll == 6 and rx == 329:
                    ry=333
                    rx=rx+(64*6)
                    turn='red'
                elif ry==333 and diceroll <= 5 and diceroll !=2 and diceroll != 1and rx ==329:
                    ry=333
                    rx=rx+(64*diceroll)
                elif ry==333 and diceroll ==2 and rx ==329:
                    ry=333
                    rx=457
                    if ry ==333 and rx == 457:
                         rx =777
                         ry =53
                elif ry==333 and diceroll ==1 and rx ==329:
                    ry=333
                    rx=393
                    if ry==333 and rx == 393:
                         rx =905
                         ry =403         
                 
                                    
                elif ry==333 and diceroll == 6 and rx ==521:
                    ry=ry-(70*1)
                    rx=rx+(64*5)
                    turn='red'
                elif ry==333 and diceroll <= 5 and diceroll != 3  and rx ==521:
                    ry=333
                    rx=rx+(64*diceroll)
                elif diceroll == 3 and ry ==333 and rx ==521:
                    ry=333
                    rx=713
                    if ry==333 and rx==713:
                        ry=193
                        rx=777
                    
                elif ry==333 and diceroll == 6 and rx ==585:
                    ry=ry-(70*2)
                    rx=rx+(64*4)
                    turn='red'
                elif ry==333 and diceroll == 5 and rx ==585:
                    ry=ry-(70*1)
                    rx=rx+(64*4)
                elif ry==333 and diceroll <= 4 and diceroll != 2 and rx ==585:
                    ry=333
                    rx=rx+(64*diceroll)
                elif diceroll == 2 and ry ==333 and rx ==585:
                    ry=333
                    rx=713
                    if ry==333 and rx==713:
                        ry=193
                        rx=777    
                elif ry==333 and diceroll == 6 and rx ==649:
                    ry=123
                    rx=841
                    if ry==123 and rx==841:
                        ry=53
                        rx=393 
                    turn='red'
                elif ry==333 and diceroll == 5 and rx ==649:
                    ry=ry-(70*2)
                    rx=rx+(64*3)
                elif ry==333 and diceroll == 4 and rx ==649:
                    ry=ry-(70*1)
                    rx=rx+(64*3)
                elif ry==333 and diceroll <= 3 and diceroll !=1 and rx ==649:
                    ry=333
                    rx=rx+(64*diceroll)
                elif diceroll == 1 and ry ==333 and rx ==649:
                    ry=333
                    rx=713
                    if ry==333 and rx==713:
                        ry=193
                        rx=777     

                
                elif ry==333 and diceroll == 6 and rx ==777:
                    ry=ry-(70*4)
                    rx=777
                    turn='red'
                elif ry==333 and diceroll == 5 and rx ==777:
                    ry=53
                    rx=841
                    if ry==53 and rx==841:
                        ry=263
                        rx=841
                elif ry==333 and diceroll == 4 and rx ==777:
                    ry=123
                    rx=841
                    if ry==123 and rx==841:
                        ry=53
                        rx=393
                elif ry==333 and diceroll == 3 and rx ==777:
                    ry=ry-(70*2)
                    rx=rx+(64*1)
                elif ry==333 and diceroll == 2 and rx ==777:
                    ry=ry-(70*1)
                    rx=rx+(64*1)
                elif ry==333 and diceroll == 1 and rx ==777:
                    ry=333
                    rx=rx+(64*1)

                elif diceroll == 6 and ry==333 and rx==841:
                    ry=ry-(70*4)
                    rx=rx-(64*2)
                    turn='red'
                elif diceroll == 5 and ry==333 and rx==841:
                    ry=ry-(70*4)
                    rx=rx-(64*1)
                elif diceroll < 4 and diceroll != 3 and ry==333 and rx==841:
                    ry=ry-(70*diceroll)
                    rx=841
                elif diceroll == 3 and ry ==333 and rx ==841:
                    ry=123
                    rx=841
                    if ry==123 and rx==841:
                        ry=53
                        rx=393
                elif diceroll == 4 and ry ==333 and rx ==841:
                    ry=53
                    rx=841
                    if ry==53 and rx==841:
                        ry=263
                        rx=841        
                elif diceroll == 6 and ry==263 and rx==841:
                    ry=ry-(70*3)
                    rx=rx-(64*3)
                    turn='red'
                elif diceroll ==5 and ry==263 and rx==841:
                    ry=ry-(70*3)
                    rx=rx-(64*2)
                elif diceroll ==4 and ry==263 and rx==841:
                    ry=ry-(70*3)
                    rx=rx-(64*1)
                elif diceroll < 3 and diceroll != 2 and ry==263 and rx==841:
                    ry=ry-(70*diceroll)
                    rx=841
                elif diceroll == 2 and ry ==263 and rx ==841:
                    ry=123
                    rx=841
                    if ry==123 and rx==841:
                        ry=53
                        rx=393
                elif diceroll == 2 and ry ==263 and rx ==841:
                    ry=53
                    rx=841
                    if ry==53 and rx==841:
                        ry=263
                        rx=841         
                    
                elif ry == 193 and diceroll == 6 and  rx==841:
                    ry=ry-(70*2)
                    rx=rx-(64*4)
                    turn='red'
                elif ry == 193 and diceroll == 5 and  rx==841:
                    ry=ry-(70*2)
                    rx=rx-(64*3)
                elif ry == 193 and diceroll == 4 and  rx==841:
                    ry=ry-(70*2)
                    rx=rx-(64*2)
                elif ry == 193 and diceroll == 3 and  rx==841:
                    ry=ry-(70*2)
                    rx=rx-(64*1)
                elif ry == 193 and diceroll == 2 and  rx==841:
                    ry=53
                    rx=841
                    if ry==53 and rx==841:
                        ry=263
                        rx=841
                elif ry == 193 and diceroll == 1 and  rx==841:
                    ry=123
                    rx=841
                    if ry==123 and rx==841:
                        ry=53
                        rx=393
                                                     
                                 
                elif ry==53 and diceroll == 6 and rx==777:
                    ry=53
                    rx=rx-(64*6)
                    turn='red'
                elif ry==53 and diceroll <= 5 and rx==777:
                    ry=53
                    rx=rx-(64*diceroll)
                elif ry==53 and diceroll == 6 and rx==713:
                    ry=123
                    rx=393
                    if ry==123 and rx==393:
                        ry=263
                        rx=393                      
                    turn='red'
                elif ry==53 and diceroll <= 5 and rx==713:
                    ry=53
                    rx=rx-(64*diceroll)
                elif ry==53 and diceroll == 1 and rx==393:
                    ry=53
                    rx=rx-(64*1)
                elif ry==53 and diceroll == 6 and rx==649:
                    ry=ry+(70*2)
                    rx=rx-(64*4)
                    turn='red'
                elif ry==53 and diceroll == 5 and rx==649:
                   ry=123
                   rx=393
                   if ry==123 and rx==393:
                        ry=263
                        rx=393   
                elif ry==53 and diceroll <= 4 and rx==649:
                    ry=53
                    rx=rx-(64*diceroll)

                elif ry==53 and diceroll == 6 and rx==585:
                    ry=263
                    rx=393
                    if ry==263 and rx==393:
                        ry=-17
                        rx=649 
                    turn='red'
                elif ry==53 and diceroll == 5 and rx==585:
                    ry=ry+(70*2)
                    rx=rx-(64*3)
                elif ry==53 and diceroll == 4 and rx==585:
                    ry=123
                    rx=393
                    if ry==123 and rx==393:
                        ry=263
                        rx=393   
                elif ry==53 and diceroll <= 3 and rx==585:
                    ry=53
                    rx=rx-(64*diceroll)

                elif ry==53 and diceroll == 6 and rx==521:
                    ry=ry+(70*3)
                    rx=rx-(64*1)
                    turn='red'
                elif ry==53 and diceroll == 5 and rx==521:
                    ry=263
                    rx=393
                    if ry==263 and rx==393:
                        ry=-17
                        rx=649 
                elif ry==53 and diceroll == 4 and rx==521:
                    ry=ry+(70*2)
                    rx=rx-(64*2)
                elif ry==53 and diceroll == 3 and rx==521:
                    ry=123
                    rx=393
                    if ry==123 and rx==393:
                        ry=263
                        rx=393   
                elif ry==53 and diceroll <= 2 and rx==521:
                    ry=53
                    rx=rx-(64*diceroll)

                elif ry==53 and diceroll == 6 and rx==457:
                    ry=263
                    rx=521
                    if ry==263 and rx==521:
                        ry=193
                        rx=777
                    turn='red'
                elif ry==53 and diceroll == 5 and rx==457:
                    ry=ry+(70*3)
                    rx=457
                elif ry==53 and diceroll == 4 and rx==457:
                    ry=263
                    rx=393
                    if ry==263 and rx==393:
                        ry=-17
                        rx=649 
                elif ry==53 and diceroll == 3 and rx==457:
                    ry=ry+(70*2)
                    rx=rx-(64*1)
                elif ry==53 and diceroll == 2 and rx==457:
                    ry=123
                    rx=393
                    if ry==123 and rx==393:
                        ry=263
                        rx=393   
                elif ry==53 and diceroll == 1 and rx==457:
                    ry=53
                    rx=rx-(64*1)

                elif ry==53 and diceroll == 6 and rx==393:
                    ry=ry+(70*3)
                    rx=rx+(64*3)
                    turn='red'
                elif ry==53 and diceroll == 5 and rx==393:
                    ry=263
                    rx=521
                    if ry==263 and rx==521:
                        ry=193
                        rx=777
                elif ry==53 and diceroll == 4 and rx==393:
                    ry=ry+(70*3)
                    rx=rx+(64*1)
                elif ry==53 and diceroll < 3 and diceroll !=1 and rx==393:
                    ry=ry+(70*diceroll)
                    rx=393
                elif  ry==53 and diceroll ==3 and rx==393:
                    ry=263
                    rx=393
                    if ry==263 and rx==393:
                        ry=-17
                        rx=649 
                elif  ry==53 and diceroll ==1 and rx==393:
                    ry=123
                    rx=393
                    if ry==123 and rx==393:
                        ry=263
                        rx=393   

                
                elif ry==193 and diceroll == 6 and rx==393:
                    ry=ry+(70*1)
                    rx=rx+(64*5)
                    turn='red'
                elif ry==193 and diceroll == 5 and rx==393:
                    ry=ry+(70*1)
                    rx=rx+(64*4)
                elif ry==193 and diceroll == 4 and rx==393:
                    ry=ry+(70*1)
                    rx=rx+(64*3)
                elif ry==193 and diceroll ==3  and rx==393:
                    ry=263
                    rx=521
                    if ry==263 and rx==521:
                        ry=193
                        rx=777
                elif ry==193 and diceroll ==2  and rx==393:
                    ry=ry+(70*1)
                    rx=rx+(64*1)
                elif ry==193 and diceroll == 1 and rx==393:
                    ry=263
                    rx=393
                    if ry==263 and rx==393:
                        ry=-17
                        rx=649 

                elif ry==263 and diceroll == 6 and rx==393:
                    ry=263
                    rx=rx+(64*6)
                    turn='red'
                elif ry==263 and diceroll <= 5 and rx==393:
                    ry=263
                    rx=rx+(64*diceroll)
                                    
                
                elif ry==263 and diceroll == 6 and rx==585:
                    ry=ry-(70*2)
                    rx=rx+(64*2)
                    turn='red'
                elif ry==263 and diceroll ==5  and rx==585:
                    ry=ry-(70*2)
                    rx=rx+(64*3)
                elif ry==263 and diceroll ==4  and rx==585:
                    ry=ry-(70*1)
                    rx=rx+(64*3)
                elif ry==263 and diceroll <3  and rx==585:
                    ry=263
                    rx=rx+(64*diceroll)
                elif ry==263  and diceroll ==3  and rx==585:
                    ry=263
                    rx=777
                    if ry==263 and rx==777:
                        ry=403
                        rx=329        
     

                elif ry==263 and diceroll == 6 and rx==457:
                    ry=ry-(70*1)
                    rx=rx+(64*5)
                    turn='red'
                elif ry==263 and diceroll < 5 and diceroll !=1  and rx==457:
                    ry=263
                    rx=rx+(64*diceroll)
                elif ry==263  and diceroll ==1  and rx==457:
                    ry=263
                    rx=521
                    if ry==263 and rx==521:
                        ry=193
                        rx=777
                elif ry==263  and diceroll ==5  and rx==457:
                    ry=263
                    rx=777
                    if ry==263 and rx==777:
                        ry=403
                        rx=329        

                elif ry==263 and diceroll == 6 and rx==649:
                    ry=ry-(70*2)
                    rx=649
                    turn='red'
                elif ry==263 and diceroll ==5  and rx==649:
                    ry=123
                    rx=777
                    if ry==123 and rx==777:
                        ry=158
                        rx=521

                elif ry==263 and diceroll ==4  and rx==649:
                    ry=123
                    rx=777
                    if ry==123 and rx==777:
                        ry=158
                        rx=521

                elif ry==263 and diceroll ==3  and rx==649:
                    ry=ry=ry-(70*1)
                    rx=rx+(64*2)  
                elif ry==263 and diceroll < 2  and rx==649:
                    ry=263
                    rx=rx+(64*diceroll)
                elif ry==263  and diceroll ==2  and rx==649:
                    ry=263
                    rx=777
                    if ry==263 and rx==777:
                        ry=403
                        rx=329        
    

                elif ry==263 and diceroll == 6 and rx==713:  #win
                    ry=158
                    rx=521
                    turn='red'
                elif ry==263 and diceroll ==5  and rx==713:
                    ry=ry-(70*2)
                    rx=rx-(64*1)
                elif ry==263 and diceroll ==4  and rx==713:
                    ry=ry-(70*2)
                    rx=713
                elif ry==263 and diceroll ==3  and rx==713:
                    ry=123
                    rx=777
                    if ry==123 and rx==777:
                        ry=158
                        rx=521
                elif ry==263 and diceroll ==2  and rx==713:
                    ry=ry-(70*1)
                    rx=rx+(64*1)  
                elif ry==263 and diceroll ==1  and rx==713:
                    ry=263
                    rx=777
                    if ry==263 and rx==777:
                        ry=403
                        rx=329
                        
                elif ry==263 and diceroll == 5 and rx==777:  #win
                    ry=158
                    rx=521
                elif ry==263 and diceroll ==4  and rx==777:
                    ry=ry-(70*2)
                    rx=rx-(64*2)
                elif ry==263 and diceroll ==3  and rx==777:
                    ry=ry-(70*1)
                    rx=rx-(64*2)  
                elif ry==263 and diceroll <=2  and rx==777:
                    ry=ry-(70*diceroll)
                    rx=777
                              

                elif ry==193 and diceroll ==4  and rx==777:  #win
                    ry=158
                    rx=521
                elif ry==193 and diceroll ==3  and rx==777:
                    ry=ry-(70*1)
                    rx=rx-(64*2)  
                elif ry==193 and diceroll ==2  and rx==777:
                    ry=ry-(70*1)
                    rx=rx-(64*1) 
                elif ry==193 and diceroll ==1  and rx==777:
                    ry=123
                    rx=777
                    if ry==123 and rx==777:
                        ry=158
                        rx=521
       

                elif ry==123 and diceroll ==3  and rx==777:  #win
                    ry=158
                    rx=521  
                elif ry==123 and diceroll <=2  and rx==777:
                    ry=123
                    rx=rx-(64*diceroll) 

                elif ry==123 and diceroll ==2  and rx==713:  #win
                    ry=158
                    rx=521
                elif ry==123 and diceroll ==1  and rx==713:
                    ry=123
                    rx=rx=rx-(64*1)

                elif ry==123 and diceroll ==1  and rx==649:  #win
                    ry=158
                    rx=521  

                else:
                    pass
            
                 
             #for player2
            elif pickNumber() and turn=='blue':
                turn='red'
                if diceroll == 6 and bx==209 and by==403:
                    bx=329
                    by=403
                    
                    turn='blue'
                elif diceroll == 6 and bx ==329 and by==403:
                    bx=bx+(64*6)
                    by=403
                    turn='blue'
                elif diceroll == 6 and bx ==393 and by==403:
                    bx=bx+(64*6)
                    by=403
                    turn='blue'
                elif diceroll == 6 and bx ==457 and by==403:
                    bx=841
                    by=403
                    if bx==841 and by==403:
                         bx=905
                         by=403
                    turn='blue'
                elif diceroll == 6 and bx ==521 and by==403:
                    bx=bx+(64*6)
                    by=403
                    turn='blue'
                elif  diceroll == 4 and bx == 329 and by==403:
                    bx=585
                    by=403
                    if bx==585 and by==403:
                         bx=905
                         by=403
                    
                elif  diceroll < 5 and diceroll != 4 and  bx == 329 and by==403:
                    bx=bx+(64*diceroll)
                    by=403
                elif  diceroll == 5 and bx == 329 and by==403:
                    bx=649
                    by=403
                    if bx==649 and by==403:
                         bx=905
                         by=263
                
                    

                elif  diceroll <= 5 and diceroll != 3 and diceroll != 4 and bx == 393 and by==403:
                    bx=bx+(64*diceroll)
                    by=403
                elif  diceroll == 3 and bx == 393 and by==403:
                    bx=585
                    by=403
                    if bx==585 and by==403:
                         bx=905
                         by=403
                elif  diceroll == 4 and bx == 393 and by==403:
                    bx=649
                    by=403
                    if bx==649 and by==403:
                         bx=905
                         by=263         
                elif  diceroll <= 5 and bx == 457 and diceroll !=2 and diceroll !=3  and by==403:
                    bx=bx+(64*diceroll)
                    by=403
                elif  diceroll == 2 and bx == 457 and by==403:
                    bx=585
                    by=403
                    if bx==585 and by==403:
                         bx=905
                         by=403
                elif  diceroll == 3 and bx == 457 and by==403:
                    bx=649
                    by=403
                    if bx==649 and by==403:
                         bx=905
                         by=263          
                elif  diceroll < 5 and diceroll !=1 and diceroll !=2 and bx == 521 and by==403:
                    bx=bx+(64*diceroll)
                    by=403
                elif  diceroll == 1 and bx == 521 and by==403:
                    bx=585
                    by=403
                    if bx==585 and by==403:
                         bx=905
                         by=403
                elif  diceroll == 2 and bx == 521 and by==403:
                    bx=649
                    by=403
                    if bx==649 and by==403:
                         bx=905
                         by=263  
                elif  diceroll == 5 and bx == 521 and by==403:
                    bx=841
                    by=403
                    if bx==841 and by==403:
                         bx=905
                         by=403     
                
                                
                     
                elif bx == 713 and diceroll == 6 and  by==403:
                   bx=bx+(64*3)
                   by=by-(70*3)
                   turn='blue'
                elif bx == 713 and diceroll <= 3 and diceroll != 2 and  by==403:
                    bx=bx+(64*diceroll)
                    by==403
                elif  diceroll == 2 and bx == 713 and by==403:
                    bx=841
                    by=403
                    if bx==841 and by==403:
                         bx=905
                         by=403    
                elif bx == 713 and diceroll == 4 and  by==403:
                    bx=bx+(64*3)
                    by=by-(70*1)
                elif bx == 713 and diceroll == 5 and  by==403:
                    bx=bx+(64*3)
                    by=by-(70*2)
                                      
                elif bx == 777 and diceroll == 3 and  by==403:
                   bx=bx+(64*2)
                   by=by-(70*1)
                elif bx == 777 and diceroll == 4 and  by==403:
                   bx=bx+(64*2)
                   by=by-(70*2)
                elif bx == 777 and diceroll ==5 and  by==403:
                   bx=bx+(64*2)
                   by=by-(70*3)       
                elif bx == 777 and diceroll < 2 and  by==403:
                    bx=bx+(64*diceroll)
                    by=403
                elif  diceroll == 2 and bx == 777 and by==403:
                    bx=841
                    by=403
                    if bx==841 and by==403:
                         bx=905
                         by=403      
                elif bx == 777 and diceroll == 6 and  by==403:
                    bx=905
                    by=123
                    if bx==905 and by==123:
                         bx=329
                         by=193
                    turn='blue'
                
                elif diceroll == 6 and by==403 and bx==905:
                    by=by-(70*6)
                    bx=905
                    turn='blue'
                elif diceroll <= 5 and diceroll !=4 and by==403 and bx==905:
                    by=by-(70*diceroll)
                    bx=905
                elif bx == 905 and diceroll == 4 and  by==403:
                    bx=905
                    by=123
                    if bx==905 and by==123:
                         bx=329
                         by=193    
                elif diceroll == 6 and by==333 and bx==905:
                    by=by-(70*5)
                    bx=bx-(64*1)
                    turn='blue'
                elif diceroll <= 5 and diceroll != 3  and by==333 and bx==905:
                    by=by-(70*diceroll)
                    bx=905
                elif bx == 905 and diceroll == 3 and  by==333:
                    bx=905
                    by=123
                    if bx==905 and by==123:
                         bx=329
                         by=193    
                elif diceroll == 6 and by==263 and bx==905:
                    by=-17
                    bx=777
                    if bx==777 and by==-17:
                         bx=585
                         by=333 
                    turn='blue'
                elif diceroll ==5 and by==263 and bx==905:
                    by=by-(70*4)
                    bx=bx-(64*1)
                elif diceroll <=4 and diceroll !=2 and by==263 and bx==905:
                    by=by-(70*diceroll)
                    bx=905
                elif bx == 905 and diceroll == 2 and  by==263:
                    bx=905
                    by=123
                    if bx==905 and by==123:
                         bx=329
                         by=193     
                elif diceroll == 6 and by==193 and bx==905:
                    by=-17
                    bx=713
                    if bx==713 and by==-17:
                         bx=777
                         by=403 
                    turn='blue'
                elif by == 193 and diceroll == 5 and  bx==905:
                    by=-17
                    bx=777
                    if bx==777 and by==-17:
                         bx=585
                         by=333 
                elif by == 193 and diceroll == 4 and  bx==905:
                    by=by-(70*3)
                    bx=bx-(64*1)
                elif by == 193 and diceroll <= 3 and diceroll !=1 and  bx==905:
                    by=by-(70*diceroll)
                    bx=905
                elif bx == 905 and diceroll == 1 and  by==193:
                    bx=905
                    by=123
                    if bx==905 and by==123:
                         bx=329
                         by=193    
                
                elif by==53 and diceroll == 6 and bx==905:
                    by=by-(70*1)
                    bx=bx-(64*5)
                    turn='blue'
                elif by==53 and diceroll == 5 and bx==905:
                    by=by-(70*1)
                    bx=bx-(64*4)
                elif by==53 and diceroll == 4 and bx==905:
                    by=-17
                    bx=713
                    if bx==713 and by==-17:
                         bx=777
                         by=403 
                elif by==53 and diceroll == 3 and bx==905:
                    by=-17
                    bx=777
                    if bx==777 and by==-17:
                         bx=585
                         by=333 
                elif by==53 and diceroll == 2 and bx==905:
                    by=by-(70*1)
                    bx=bx-(64*1)
                elif by==53 and diceroll == 1 and bx==905:
                    by=by-(70*1)
                    bx=905
                elif by==-17 and diceroll == 6 and bx ==905:
                    by=-17
                    bx=bx-(64*6)
                    turn='blue'
                elif by==-17 and diceroll <=5 and diceroll !=2 and diceroll !=3   and bx ==905:
                    by=-17
                    bx=bx-(64*diceroll)
                elif by==-17 and diceroll == 2 and bx==905:
                    by=-17
                    bx=713
                    if bx==713 and by==-17:
                         bx=777
                         by=403
                elif by==-17 and diceroll == 3 and bx==905:
                    by=-17
                    bx=777
                    if bx==777 and by==-17:
                         bx=585
                         by=333         
                elif by==-17 and diceroll == 6 and bx ==841:
                    by=-17
                    bx=457
                    if bx==457 and by==-17:
                         bx=521
                         by=333
                    turn='blue'
                elif by==-17 and diceroll <=5 and diceroll !=1 and diceroll !=2   and bx ==841:
                    by=-17
                    bx=bx-(64*diceroll)    
                elif by==-17 and diceroll == 1 and bx==841:
                    by=-17
                    bx=777
                    if bx==777 and by==-17:
                         bx=585
                         by=333
                elif by==-17 and diceroll == 2 and bx==841:
                    by=-17
                    bx=713
                    if bx==713 and by==-17:
                         bx=777
                         by=403           
                elif by==-17 and diceroll == 6 and bx==649:
                    by=by+(70*1)
                    bx=bx-(64*5)
                    turn='blue'
                elif by==-17 and diceroll <=5 and diceroll != 3 and bx ==649:
                    by=-17
                    bx=bx-(64*diceroll)
                elif  by==-17 and diceroll == 3 and bx ==649:
                    by=-17
                    bx=457
                    if bx==457 and by==-17:
                         bx=521
                         by=333 

                elif by==-17 and diceroll == 6 and bx==585:
                    by=by+(70*2)
                    bx=bx-(64*4)
                    turn='blue'
                elif by==-17 and diceroll == 5 and bx==585:
                    by=by+(70*1)
                    bx=bx-(64*4)
                elif by==-17 and diceroll <= 4 and diceroll != 2 and bx==585:
                    by=-17
                    bx=bx-(64*diceroll)
                elif  by==-17 and diceroll == 2 and bx ==585:
                    by=-17
                    bx=457
                    if bx==457 and by==-17:
                         bx=521
                         by=333     

                elif by==-17 and diceroll == 6 and bx==521:
                    by=by+(70*3)
                    bx=bx-(64*3)
                    turn='blue'
                elif by==-17 and diceroll == 5 and bx==521:
                    by=by+(70*2)
                    bx=bx-(64*3)
                elif by==-17 and diceroll == 4 and bx==521:
                    by=by+(70*1)
                    bx=bx-(64*3)
                elif by==-17 and diceroll <= 3 and diceroll != 1 and bx==521:
                    by=-17
                    bx=bx-(64*diceroll)
                elif  by==-17 and diceroll == 2 and bx ==5218:
                    by=-17
                    bx=457
                    if bx==457 and by==-17:
                         bx=521
                         by=333     

                elif by==-17 and diceroll == 6 and bx==393:
                    by=by+(70*5)
                    bx=bx-(64*1)
                    turn='blue'
                elif by==-17 and diceroll == 5 and bx==393:
                    by=by+(70*4)
                    bx=bx-(64*1)
                elif by==-17 and diceroll == 4 and bx==393:
                    by=by+(70*3)
                    bx=bx-(64*1)
                elif by==-17 and diceroll == 3 and bx==393:
                    by=by+(70*2)
                    bx=bx-(64*1)
                elif by==-17 and diceroll == 2 and bx==393:
                    by=by+(70*1)
                    bx=bx-(64*1)
                elif by==-17 and diceroll == 1 and bx==393:
                    by=-17
                    bx=bx-(64*1)
                elif by==-17 and diceroll == 6 and bx==329:
                    by=333
                    bx=393
                    if by==333 and bx == 393:
                         bx =905
                         by =403
                    turn='blue'
                elif by==-17 and diceroll <= 5 and bx==329:
                    by=by+(70*diceroll)
                    bx=329
                elif by==53 and diceroll == 6 and bx==329:
                    by=333
                    bx=457
                    if by==333 and bx == 457:
                         bx =777
                         by =53
                    turn='blue'
                elif by==53 and diceroll == 5 and bx==329:
                    by=333
                    bx=393
                    if by==333 and bx == 393:
                         bx =905
                         by =403
                elif by==53 and diceroll <= 4 and bx==329:
                    by=by+(70*diceroll)
                    bx=329
                elif by==123 and diceroll == 6 and bx==329:
                    by=by+(70*3)
                    bx=bx+(64*3)
                    turn='blue'
                elif by==123 and diceroll == 5 and bx==329:
                    by=333
                    bx=457
                    if by ==333 and bx == 457:
                         bx =777
                         by =53
                elif by==123 and diceroll == 4 and bx==329:
                    by=333
                    bx=393
                    if by==333 and bx == 393:
                         bx =905
                         by =403
                elif by==123 and diceroll <= 3 and bx==329:
                    by=by+(70*diceroll)
                    bx=123
                elif by==193 and diceroll == 6 and bx==329:
                    by=by+(70*2)
                    bx=bx+(64*4)
                    turn='blue'
                elif by==193 and diceroll == 5 and bx==329:
                    by=by+(70*2)
                    bx=bx+(64*3)
                elif by==193 and diceroll == 4 and bx==329:
                    by=333
                    bx=457
                    if by ==333 and bx ==457:
                         bx =777
                         by =53
                elif by==193 and diceroll == 3 and bx==329:
                    by=333
                    bx=393
                    if by==333 and bx == 393:
                         bx =905
                         by =403
                elif by==193 and diceroll <= 2 and bx==329:
                    by=by+(70*diceroll)
                    bx=329
                elif by==263 and diceroll == 6 and bx==329:
                    by=333
                    bx=713
                    if by==333 and bx==713:
                        by=193
                        bx=777
                    turn='blue'
                elif by==263 and diceroll == 5 and bx==329:
                    by=by+(70*1)
                    bx=bx+(64*4)
                elif by==263 and diceroll == 4 and bx==329:
                    by=by+(70*1)
                    bx=bx+(64*3)
                elif by==263 and diceroll == 3 and bx==329:
                    by=333
                    bx=457
                    if by ==333 and bx == 457:
                         bx =777
                         by =53
                elif by==263 and diceroll == 2 and bx==329:
                    by=333
                    bx=393
                    if by==333 and bx == 393:
                         bx =905
                         by =403
                elif by==263 and diceroll == 1 and bx==329:
                    by=by+(70*1)
                    bx=329
                elif by==333 and diceroll == 6 and bx == 329:
                    by=333
                    bx=bx+(64*6)
                    turn='blue'
                elif by==333 and diceroll <= 5 and diceroll !=2 and diceroll != 1and bx ==329:
                    by=333
                    bx=bx+(64*diceroll)
                elif by==333 and diceroll ==2 and bx ==329:
                    by=333
                    bx=457
                    if by ==333 and bx == 457:
                         bx =777
                         by =53
                elif by==333 and diceroll ==1 and bx ==329:
                    by=333
                    bx=393
                    if by==333 and bx == 393:
                         bx =905
                         by =403         
                 
                                    
                elif by==333 and diceroll == 6 and bx ==521:
                    by=by-(70*1)
                    bx=bx+(64*5)
                    turn='blue'
                elif by==333 and diceroll <= 5 and diceroll != 3  and bx ==521:
                    by=333
                    bx=bx+(64*diceroll)
                elif diceroll == 3 and by ==333 and bx ==521:
                    by=333
                    bx=713
                    if by==333 and bx==713:
                        by=193
                        bx=777
                    
                elif by==333 and diceroll == 6 and bx ==585:
                    by=by-(70*2)
                    bx=bx+(64*4)
                    turn='blue'
                elif by==333 and diceroll == 5 and bx ==585:
                    by=by-(70*1)
                    bx=bx+(64*4)
                elif by==333 and diceroll <= 4 and diceroll != 2 and bx ==585:
                    by=333
                    bx=bx+(64*diceroll)
                elif diceroll == 2 and by ==333 and bx ==585:
                    by=333
                    bx=713
                    if by==333 and bx==713:
                        by=193
                        bx=777    
                elif by==333 and diceroll == 6 and bx ==649:
                    by=123
                    bx=841
                    if by==123 and bx==841:
                        by=53
                        bx=393 
                    turn='blue'
                elif by==333 and diceroll == 5 and bx ==649:
                    by=by-(70*2)
                    bx=bx+(64*3)
                elif by==333 and diceroll == 4 and bx ==649:
                    by=by-(70*1)
                    bx=bx+(64*3)
                elif by==333 and diceroll <= 3 and diceroll !=1 and bx ==649:
                    by=333
                    bx=bx+(64*diceroll)
                elif diceroll == 1 and by ==333 and bx ==649:
                    by=333
                    bx=713
                    if by==333 and bx==713:
                        by=193
                        bx=777     

                
                elif by==333 and diceroll == 6 and bx ==777:
                    by=by-(70*4)
                    bx=777
                    turn='blue'
                elif by==333 and diceroll == 5 and bx ==777:
                    by=53
                    bx=841
                    if by==53 and bx==841:
                        by=263
                        bx=841
                elif by==333 and diceroll == 4 and bx ==777:
                    by=123
                    bx=841
                    if by==123 and bx==841:
                        by=53
                        bx=393
                elif by==333 and diceroll == 3 and bx ==777:
                    by=by-(70*2)
                    bx=bx+(64*1)
                elif by==333 and diceroll == 2 and bx ==777:
                    by=by-(70*1)
                    bx=bx+(64*1)
                elif by==333 and diceroll == 1 and bx ==777:
                    by=333
                    bx=bx+(64*1)

                elif diceroll == 6 and by==333 and bx==841:
                    by=by-(70*4)
                    bx=bx-(64*2)
                    turn='blue'
                elif diceroll == 5 and by==333 and bx==841:
                    by=by-(70*4)
                    bx=bx-(64*1)
                elif diceroll < 4 and diceroll != 3 and by==333 and bx==841:
                    by=by-(70*diceroll)
                    bx=841
                elif diceroll == 3 and by ==333 and bx ==841:
                    by=123
                    bx=841
                    if by==123 and bx==841:
                        by=53
                        bx=393
                elif diceroll == 4 and by ==333 and bx ==841:
                    by=53
                    bx=841
                    if by==53 and bx==841:
                        by=263
                        bx=841        
                elif diceroll == 6 and by==263 and bx==841:
                    by=by-(70*3)
                    bx=bx-(64*3)
                    turn='blue'
                elif diceroll ==5 and by==263 and bx==841:
                    by=by-(70*3)
                    bx=bx-(64*2)
                elif diceroll ==4 and by==263 and bx==841:
                    by=by-(70*3)
                    bx=bx-(64*1)
                elif diceroll < 3 and diceroll != 2 and by==263 and bx==841:
                    by=by-(70*diceroll)
                    bx=841
                elif diceroll == 2 and by ==263 and bx ==841:
                    by=123
                    bx=841
                    if by==123 and bx==841:
                        by=53
                        bx=393
                elif diceroll == 2 and by ==263 and bx ==841:
                    by=53
                    bx=841
                    if by==53 and bx==841:
                        by=263
                        bx=841         
                    
                elif by == 193 and diceroll == 6 and  bx==841:
                    by=by-(70*2)
                    bx=bx-(64*4)
                    turn='blue'
                elif by == 193 and diceroll == 5 and  bx==841:
                    by=by-(70*2)
                    bx=bx-(64*3)
                elif by == 193 and diceroll == 4 and  bx==841:
                    by=by-(70*2)
                    bx=bx-(64*2)
                elif by == 193 and diceroll == 3 and  bx==841:
                    by=by-(70*2)
                    bx=bx-(64*1)
                elif by == 193 and diceroll == 2 and  bx==841:
                    by=53
                    bx=841
                    if by==53 and bx==841:
                        by=263
                        bx=841
                elif by == 193 and diceroll == 1 and  bx==841:
                    by=123
                    bx=841
                    if by==123 and bx==841:
                        by=53
                        bx=393
                                                     
                                 
                elif by==53 and diceroll == 6 and bx==777:
                    by=53
                    bx=bx-(64*6)
                    turn='blue'
                elif by==53 and diceroll <= 5 and bx==777:
                    by=53
                    bx=bx-(64*diceroll)
                elif by==53 and diceroll == 6 and bx==713:
                    by=123
                    bx=393
                    if by==123 and bx==393:
                        by=263
                        bx=393                      
                    turn='blue'
                elif by==53 and diceroll <= 5 and bx==713:
                    by=53
                    bx=bx-(64*diceroll)
                elif by==53 and diceroll == 1 and bx==393:
                    by=53
                    bx=bx-(64*1)
                elif by==53 and diceroll == 6 and bx==649:
                    by=by+(70*2)
                    bx=bx-(64*4)
                    turn='blue'
                elif by==53 and diceroll == 5 and bx==649:
                   by=123
                   bx=393
                   if by==123 and bx==393:
                        by=263
                        bx=393   
                elif by==53 and diceroll <= 4 and bx==649:
                    by=53
                    bx=bx-(64*diceroll)

                elif by==53 and diceroll == 6 and bx==585:
                    by=263
                    bx=393
                    if by==263 and bx==393:
                        by=-17
                        bx=649 
                    turn='blue'
                elif by==53 and diceroll == 5 and bx==585:
                    by=by+(70*2)
                    bx=bx-(64*3)
                elif by==53 and diceroll == 4 and bx==585:
                    by=123
                    bx=393
                    if by==123 and bx==393:
                        by=263
                        bx=393   
                elif by==53 and diceroll <= 3 and bx==585:
                    by=53
                    bx=bx-(64*diceroll)

                elif by==53 and diceroll == 6 and bx==521:
                    by=by+(70*3)
                    bx=bx-(64*1)
                    turn='blue'
                elif by==53 and diceroll == 5 and bx==521:
                    by=263
                    bx=393
                    if by==263 and bx==393:
                        by=-17
                        bx=649 
                elif by==53 and diceroll == 4 and bx==521:
                    by=by+(70*2)
                    bx=bx-(64*2)
                elif by==53 and diceroll == 3 and bx==521:
                    by=123
                    bx=393
                    if by==123 and bx==393:
                        by=263
                        bx=393   
                elif by==53 and diceroll <= 2 and bx==521:
                    by=53
                    bx=bx-(64*diceroll)

                elif by==53 and diceroll == 6 and bx==457:
                    by=263
                    bx=521
                    if by==263 and bx==521:
                        by=193
                        bx=777
                    turn='blue'
                elif by==53 and diceroll == 5 and bx==457:
                    by=by+(70*3)
                    bx=457
                elif by==53 and diceroll == 4 and bx==457:
                    by=263
                    bx=393
                    if by==263 and bx==393:
                        by=-17
                        bx=649 
                elif by==53 and diceroll == 3 and bx==457:
                    by=by+(70*2)
                    bx=bx-(64*1)
                elif by==53 and diceroll == 2 and bx==457:
                    by=123
                    bx=393
                    if by==123 and bx==393:
                        by=263
                        bx=393   
                elif by==53 and diceroll == 1 and bx==457:
                    by=53
                    bx=bx-(64*1)

                elif by==53 and diceroll == 6 and bx==393:
                    by=by+(70*3)
                    bx=bx+(64*3)
                    turn='blue'
                elif by==53 and diceroll == 5 and bx==393:
                    by=263
                    bx=521
                    if by==263 and bx==521:
                        by=193
                        bx=777
                elif by==53 and diceroll == 4 and bx==393:
                    by=by+(70*3)
                    bx=bx+(64*1)
                elif by==53 and diceroll < 3 and diceroll !=1 and bx==393:
                    by=by+(70*diceroll)
                    bx=393
                elif  by==53 and diceroll ==3 and bx==393:
                    by=263
                    bx=393
                    if by==263 and bx==393:
                        by=-17
                        bx=649 
                elif  by==53 and diceroll ==1 and bx==393:
                    by=123
                    bx=393
                    if by==123 and bx==393:
                        by=263
                        bx=393   

                
                elif by==193 and diceroll == 6 and bx==393:
                    by=by+(70*1)
                    bx=bx+(64*5)
                    turn='blue'
                elif by==193 and diceroll == 5 and bx==393:
                    by=by+(70*1)
                    bx=bx+(64*4)
                elif by==193 and diceroll == 4 and bx==393:
                    by=by+(70*1)
                    bx=bx+(64*3)
                elif by==193 and diceroll ==3  and bx==393:
                    by=263
                    bx=521
                    if by==263 and bx==521:
                        by=193
                        bx=777
                elif by==193 and diceroll ==2  and bx==393:
                    by=by+(70*1)
                    bx=bx+(64*1)
                elif by==193 and diceroll == 1 and bx==393:
                    by=263
                    bx=393
                    if by==263 and bx==393:
                        by=-17
                        bx=649 

                elif by==263 and diceroll == 6 and bx==393:
                    by=263
                    bx=bx+(64*6)
                    turn='blue'
                elif by==263 and diceroll <= 5 and bx==393:
                    by=263
                    bx=bx+(64*diceroll)
                                    
                
                elif by==263 and diceroll == 6 and bx==585:
                    by=by-(70*2)
                    bx=bx+(64*2)
                    turn='blue'
                elif by==263 and diceroll ==5  and bx==585:
                    by=by-(70*2)
                    bx=bx+(64*3)
                elif by==263 and diceroll ==4  and bx==585:
                    by=by-(70*1)
                    bx=bx+(64*3)
                elif by==263 and diceroll <3  and bx==585:
                    by=263
                    bx=bx+(64*diceroll)
                elif by==263  and diceroll ==3  and bx==585:
                    by=263
                    bx=777
                    if by==263 and bx==777:
                        by=403
                        bx=329        
     

                elif by==263 and diceroll == 6 and bx==457:
                    by=by-(70*1)
                    bx=bx+(64*5)
                    turn='blue'
                elif by==263 and diceroll < 5 and diceroll !=1  and bx==457:
                    by=263
                    bx=bx+(64*diceroll)
                elif by==263  and diceroll ==1  and bx==457:
                    by=263
                    bx=521
                    if by==263 and bx==521:
                        by=193
                        bx=777
                elif by==263  and diceroll ==5  and bx==457:
                    by=263
                    bx=777
                    if by==263 and bx==777:
                        by=403
                        bx=329        

                elif by==263 and diceroll == 6 and bx==649:
                    by=by-(70*2)
                    bx=649
                    turn='blue'
                elif by==263 and diceroll ==5  and bx==649:
                    by=123
                    bx=777
                    if by==123 and bx==777:
                        by=158
                        bx=521

                elif by==263 and diceroll ==4  and bx==649:
                    by=123
                    bx=777
                    if by==123 and bx==777:
                        by=158
                        bx=521

                elif by==263 and diceroll ==3  and bx==649:
                    by=by=by-(70*1)
                    bx=bx+(64*2)  
                elif by==263 and diceroll < 2  and bx==649:
                    by=263
                    bx=bx+(64*diceroll)
                elif by==263  and diceroll ==2  and bx==649:
                    by=263
                    bx=777
                    if by==263 and bx==777:
                        by=403
                        bx=329        
    

                elif by==263 and diceroll == 6 and bx==713:  #win
                    by=158
                    bx=521
                    turn='blue'
                elif by==263 and diceroll ==5  and bx==713:
                    by=by-(70*2)
                    bx=bx-(64*1)
                elif by==263 and diceroll ==4  and bx==713:
                    by=by-(70*2)
                    bx=713
                elif by==263 and diceroll ==3  and bx==713:
                    by=123
                    bx=777
                    if by==123 and bx==777:
                        by=158
                        bx=521
                elif by==263 and diceroll ==2  and bx==713:
                    by=by-(70*1)
                    bx=bx+(64*1)  
                elif by==263 and diceroll ==1  and bx==713:
                    by=263
                    bx=777
                    if by==263 and bx==777:
                        by=403
                        bx=329
                        
                elif by==263 and diceroll == 5 and bx==777:  #win
                    by=158
                    bx=521
                elif by==263 and diceroll ==4  and bx==777:
                    by=by-(70*2)
                    bx=bx-(64*2)
                elif by==263 and diceroll ==3  and bx==777:
                    by=by-(70*1)
                    bx=bx-(64*2)  
                elif by==263 and diceroll <=2  and bx==777:
                    by=by-(70*diceroll)
                    bx=777
                              

                elif by==193 and diceroll ==4  and bx==777:  #win
                    by=158
                    bx=521
                elif by==193 and diceroll ==3  and bx==777:
                    by=by-(70*1)
                    bx=bx-(64*2)  
                elif by==193 and diceroll ==2  and bx==777:
                    by=by-(70*1)
                    bx=bx-(64*1) 
                elif by==193 and diceroll ==1  and bx==777:
                    by=123
                    bx=777
                    if by==123 and bx==777:
                        by=158
                        bx=521
       

                elif by==123 and diceroll ==3  and bx==777:  #win
                    by=158
                    bx=521  
                elif by==123 and diceroll <=2  and bx==777:
                    by=123
                    bx=bx-(64*diceroll) 

                elif by==123 and diceroll ==2  and bx==713:  #win
                    by=158
                    bx=521
                elif by==123 and diceroll ==1  and bx==713:
                    by=123
                    bx=bx=bx-(64*1)

                elif by==123 and diceroll ==1  and bx==649:  #win
                    by=158
                    bx=521  


                else:
                    pass
            
                
            else:
                pass                 
                    


    rplayer(rx, ry)   
    bplayer(bx, by) 
    pygame.display.update()

    if rx==521 and ry==158 :
        screen.fill((50, 153, 213))
        value = score_font.render(" CONGRATULATIONS....Red won !", True, (255, 255, 102))
        
        screen.blit(value, [250, 200])
        
        
        running = False
        
    if bx==521 and by==158 :
        screen.fill((50, 153, 213))
        value = score_font.render("CONGRATULATIONS....Blue won !", True, (255, 255, 102))
        
        screen.blit(value, [250, 200])
        
        running = False
        
    time.sleep(1.3)

    
pygame.display.update()
clock.tick(40)    
pygame.quit()
quit()




