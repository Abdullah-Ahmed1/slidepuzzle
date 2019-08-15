import pygame
import time
pygame.init()

display_width=1000

display_height=500



gameDisplay=pygame.display.set_mode((display_width,display_height))
def score():
    
    black=(0,0,0)
    font=pygame.font.SysFont(None,40)
    text=font.render("score:"+str(score),True,black)
    gameDisplay.blit(text,(0,0)) 

def gameloop():
    
    
    x=300
    y=485
    circle_radius=15 
    
    
    rect1_ypos1=155
    rect1_xpos1=900
    rect_ypos=350
    rect2_ypos=350
    rect3_ypos=350
    rect4_ypos=350
    rect5_ypos=350
    rect_xpos=800
    rect2_xpos=1000
    rect3_xpos=1200
    rect4_xpos=1400
    count=13
    count1=30
    xychange1=0
    xychange=10

    white=(255,255,255)
    red=(255,0,0)
    black=(0,0,0)
    blue=(0,0,255)
    grey=(100,100,100)
    navyblue=(60,60,100)
    green=(0,255,0)
    yellow=(255,255,0)
    orange=(255,128, 0)
    purple=(255,0,255)
    light_purple=(255,150,255)
    cyan=(0,255,255)
    light_red=(250,100,100)
    grey=(100,100,100)
    black=(0,0,0)
    


    jump=False
    jumpcount=8


    gexit=True
       
    def text_objects(text,font):
            textSurface = font.render(text,True ,black)
            return textSurface, textSurface.get_rect()

    
    
    
   
     
    


 
    def message_display(text):
        pygame.font.get_fonts()
        LargeText=pygame.font.SysFont('copperplategothic',115)
        textSurf,TextRect = text_objects(text,LargeText)
        TextRect.center=((display_width/2),(display_height/2))
        gameDisplay.blit(textSurf, TextRect)
        
        pygame.display.update()
            
    def crash():
        message_display("GAME OVER")
        time.sleep(2)


             

    while gexit:
           
        
                
            
        
        
        pygame.time.delay(count1)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gexit=False
           # print(event)        
        
        keys=pygame.key.get_pressed()
                 
        if keys[pygame.K_RIGHT] and x<display_width-circle_radius:
            x =x+xychange
        if keys[pygame.K_RIGHT] and y>rect_ypos-10 and x+circle_radius< rect_xpos+20 and x-circle_radius> rect_xpos-20 :
            crash()
            break
        if keys[pygame.K_LEFT] and x>xychange+circle_radius :
            x =x-xychange
        if not(jump):    
            if keys[pygame.K_UP] and y>xychange+circle_radius:
                y =y-xychange1
            if keys[pygame.K_DOWN] and y<display_height-circle_radius:
                y =y+xychange1
            if keys[pygame.K_SPACE]:
                jump=True
        else:       
            if jumpcount >= -8:
                neg=1
                if jumpcount < 0:
                    neg= -1
                y -= (jumpcount**2)*1*neg
                jumpcount -=1
                
            else:
                jump=False
                jumpcount=8   
        

        
        
        rect_xpos-=count
        rect2_xpos-=count
        rect3_xpos-=count
        rect4_xpos-=count
        rect1_xpos1-=count
        
#=============================================================================        
        if rect_xpos < -10:
            rect_xpos=900
        if rect2_xpos < -10:
            rect2_xpos = 900
        if rect3_xpos < -10:
            rect3_xpos = 900
        if rect4_xpos < -10:
            rect4_xpos = 900    
        
        
        if rect1_xpos1 < -10:
            rect1_xpos1 = 900    
#==============================================================================       
        

        
        
        if y>rect_ypos-10:
            if x-circle_radius< rect_xpos+20 and x-circle_radius> rect_xpos-20 :
                pygame.draw.circle(gameDisplay,black,[x,y],30)
                crash()
                break

        if y>rect2_ypos:   
            if x-circle_radius< rect2_xpos+20 and x-circle_radius> rect2_xpos-20 :
                pygame.draw.rect(gameDisplay,cyan,[rect2_xpos-5,rect2_ypos-5,20+10,150+5])
                crash()
                break
        if y>rect3_ypos:   
            if x-circle_radius< rect3_xpos+20 and x-circle_radius> rect3_xpos-20 :
                crash()
                break
        if y>rect4_ypos:   
            if x-circle_radius< rect4_xpos+20 and x-circle_radius> rect4_xpos-20 :
                crash()
                break    
        
        
        
        
        
        if y<305:   
            if x-circle_radius< rect1_xpos1+20 and x-circle_radius> rect1_xpos1-20 :
                crash()
                break    
#=================================================================================        
        gameDisplay.fill(grey)
       
        pygame.draw.line(gameDisplay,white,(0,150),(1000,150),10)
        pygame.draw.rect(gameDisplay,yellow,[rect_xpos,rect_ypos,20,150])
        pygame.draw.rect(gameDisplay,cyan,[rect2_xpos,rect2_ypos,20,150])
        pygame.draw.rect(gameDisplay,red,[rect3_xpos,rect3_ypos,20,150])
        pygame.draw.rect(gameDisplay,navyblue,[rect4_xpos,rect4_ypos,20,150])
        pygame.draw.rect(gameDisplay,red,[rect1_xpos1,rect1_ypos1,20,150])
        
        pygame.draw.circle(gameDisplay,black,[x,y],circle_radius)
        pygame.display.update()
  
                
       
#___________________________________________________
def text_objects(text,font):
            black=(0,0,0)
            green=(0,255,0)
            textSurface = font.render(text,True,black)
            return textSurface, textSurface.get_rect()

def game_intro() :
    purple=(255,0,255)
    grey=(100,100,100)
    light_purple=(255,150,255)
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()  
                 
        gameDisplay.fill(grey)
        LargeText=pygame.font.SysFont('copperplategothic',115)
        textSurf,TextRect = text_objects("colour bounce",LargeText)
        TextRect.center=((display_width/2),(display_height/2))
        
        gameDisplay.blit(textSurf, TextRect)
    
        pygame.draw.rect(gameDisplay,light_purple,[150,400,100,50])
        pygame.draw.rect(gameDisplay,light_purple,[650,400,100,50]) 
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if 150<mouse[0]<150+100 and 400<mouse[1]<400+50:
            pygame.draw.rect(gameDisplay,purple,[150,400,100,50])
            if click[0]==1:
                gameloop()
        
        if 650<mouse[0]<650+100 and 400<mouse[1]<400+50:
            pygame.draw.rect(gameDisplay,purple,[650,400,100,50])
            if click[0]==1:
                pygame.quit
                quit() 
        
        
        LargeText=pygame.font.SysFont('copperplategothic',40)
        textSurf,TextRect = text_objects("play",LargeText)
        TextRect.center=((150+(100/2)),(400+(50/2)))
        gameDisplay.blit(textSurf, TextRect)        
        
        LargeText=pygame.font.SysFont('copperplategothic',40)
        textSurf,TextRect = text_objects("quit",LargeText)
        TextRect.center=((650+(100/2)),(400+(50/2)))
        gameDisplay.blit(textSurf, TextRect)    
        score=0
        black=(0,0,0)
        font=pygame.font.SysFont(None,40)
        text=font.render("score:"+str(score),True,black)
        gameDisplay.blit(text,(0,0))
        
        

        pygame.display.update()

        #print(mouse)

game_intro()
pygame.quit()
quit()
