import pygame
from pygame.locals import *

pygame.init()

# Screen size (pixels)
screen_width = 600
screen_height = 500

# Font
font = pygame.font.SysFont("Constantia",30)

# Parameters
margin=50
player_score=0
cpu_score=0
score = 0
best_score = 41
fps=64
winner = 0
live_ball = False
acceleration = 0

# Attributes
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Colours
bg_color= (50,25,50)
white=(250,250,250)

# Functions
def draw_board():
    screen.fill(bg_color)
    pygame.draw.line(screen, white, (0,margin),(screen_width,margin))
    
def draw_text(txt, font, col, x, y):
    img=font.render(txt, True, col)
    screen.blit(img,(x,y))

# Classes    
class paddle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = Rect(self.x , self.y , 20, 100)
        self.speed = 12
        
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and (self.rect.top > margin) ==  True:
            self.rect.move_ip(0,-1 * self.speed)
        if key[pygame.K_DOWN] and (self.rect.bottom < screen_height)==  True:
            self.rect.move_ip(0,self.speed)
    
    def ai(self):
        if self.rect.centery < pong.rect.top and self.rect.bottom < screen_height:
            self.rect.move_ip(0, self.speed)
        if self.rect.centery > pong.rect.bottom and self.rect.top > margin:
            self.rect.move_ip(0,-1 * self.speed)    
            
    def draw(self):
        pygame.draw.rect(screen, white, self.rect)
        
class ball():
    def __init__(self, x, y, r):
        self.reset(x,y,r)
    
    def move(self):
        # Collisions
        if self.rect.top < margin:
            self.speed_y *= -1
        if self.rect.bottom > screen_height:
            self.speed_y *= -1    
        if self.rect.left <0:
            self.winner =  1
            live_ball=False
        if self.rect.right > screen_width:
            self.winner = -1
            live_ball=False
        if self.rect.colliderect(player_paddle): 
            self.speed_x *= -1
        if self.rect.colliderect(cpu_paddle):
            self.speed_x *= -1
            self.rebound += 1
        # Update
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        return(self.winner)
    
    def draw(self):
        pygame.draw.circle(screen, white, (self.rect.x + self.radius,self.rect.y + self.radius ) , self.radius )
    
    def reset(self, x, y,r):
        self.x = x
        self.y = y
        self.rebound=r
        self.radius = 8
        self.rect = Rect(self.x , self.y , self.radius * 2, self.radius * 2)
        self.speed_x = -4
        self.speed_y = 4
        self.winner = 0 # 1 Player 1 has won, 0 CPU has won
    
# Players
player_paddle = paddle(screen_width - 40, screen_height // 2)
cpu_paddle = paddle(20, screen_height // 2)
pong = ball(screen_width -60 , screen_height // 2 +50, 0 )

#Game loop
run=True
while run:
    
    fpsClock.tick(fps)
    draw_board()
    draw_text("Level: "+ str(abs(pong.speed_x)-4) , font, white, 20 , 15) 
    draw_text("Score: "+str(score),font, white, screen_width // 2 -60, 15 )
    draw_text("Best score: "+str(best_score),font, white, screen_width-200,15 )
    
    player_paddle.draw()
    cpu_paddle.draw()
     
    if live_ball == True:
        acceleration += 1
        winner = pong.move()
        if winner == 0:
            if pong.rect.colliderect(cpu_paddle):
                score+=1
            player_paddle.move()
            cpu_paddle.ai()
            pong.draw()
        else:
            live_ball = False
            if winner == -1:
                player_score +=1
                if best_score < score :
                    best_score = score
            elif winner == 1:
                cpu_score += 1
            score=0    
                
    if live_ball == False:
        if winner == 0:
            draw_text("Click anywhere to start", font, white ,140, screen_height // 2- 100)
        if winner == 1:
            draw_text("You cheated", font, white ,220, screen_height // 2- 100)
            draw_text("Click anywhere to continue", font, white ,120, screen_height // 2- 50)
        if winner == -1:
            draw_text("You loose!", font, white ,220, screen_height // 2- 100)
            draw_text("Click anywhere to continue", font, white ,120, screen_height // 2- 50)    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and live_ball ==  False:
            live_ball = True
            pong.reset(screen_width -60 , screen_height // 2 +50, 0 )
    
    if acceleration > 500:
        acceleration = 0
        if pong.speed_x <0:
            pong.speed_x -= 1
        if pong.speed_x >0:
            pong.speed_x += 1
        if pong.speed_y <0:
            pong.speed_y -= 1
        if pong.speed_y >0:
            pong.speed_y += 1    
    
    pygame.display.update()        

pygame.quit()            