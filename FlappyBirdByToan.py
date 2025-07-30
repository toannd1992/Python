import pygame
from random import randint
pygame.init()
pygame.mixer.init()
# load âm thanh
sound_score = pygame.mixer.Sound("ding.mp3")
sound_gameover = pygame.mixer.Sound("poof.mp3")

# màu
BG_COLOR = (100,220,255)
YELLOW = (213,222,128)
ORANGE = (232,97,1)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (34,139,34)
BIRD_X = 150
SPEED_BIRD = 0.5
SPACE = 170
# load ảnh và scale
gameover_image = pygame.image.load("gameover.png")
restart_image = pygame.image.load("restart.png")
restart_image = pygame.transform.scale(restart_image, (200,57))
bird0_image = pygame.image.load("bird0.png")
bird0_image = pygame.transform.scale(bird0_image,(45,45))
bird1_image = pygame.image.load("bird1.png")
bird1_image = pygame.transform.scale(bird1_image,(45,45))
bird2_image = pygame.image.load("bird2.png")
bird2_image = pygame.transform.scale(bird2_image,(45,45))
die_image = pygame.image.load("birddead.png")
die_image = pygame.transform.scale(die_image,(50,50))
dead_image = pygame.image.load("dead.png")
dead_image = pygame.transform.scale(dead_image,(450,60))
top_image = pygame.image.load("top.png")
top_image = pygame.transform.scale(top_image,(70,350))
bottom_image = pygame.image.load("bottom.png")
bottom_image = pygame.transform.scale(bottom_image,(70,350))
BG_IMAGE = pygame.image.load("background.png")
# set màn hình
display = pygame.display.set_mode((400,660))
pygame.display.set_caption("Flappy Bird Game")
hz = pygame.time.Clock()
# font chữ score
font = pygame.font.SysFont("VNI-Swiss-Condense", 50)
fontG = pygame.font.SysFont("Courier", 30)
# hàm restart game và biến cục bộ
def ReStart():
    global x1_up, x2_up,x3_up, x4, score, play_again, bird_y, drop_bird, speed, running, sound_play
    x1_up, x2_up, x3_up, x4 = 1000, 1250, 1500, 0
    score = 0
    play_again = False
    bird_y = 250
    drop_bird = 2
    speed = 2.5
    running = False
    sound_play = False

# biến
hight1_up = randint(250,450)
hight2_up = randint(250,450)
hight3_up = randint(250,450)
score_plus = False
fly = 0
angle_bird = 0 # góc của chim
angle_bird_down = 0
#running = False
ReStart()

warting = 0
run = True
# vòng lặp chính
while run:
    hz.tick(60)
    display.fill(BG_COLOR)
    display.blit(BG_IMAGE,(0,0))
# chim đung đưa đầu game
    if not running: # chờ game chạy
        warting += 1
        if warting <= 25:
            bird_y -= 0.5
            bird_rect = display.blit(bird0_image,(BIRD_X,bird_y))
        elif warting <= 50:
            bird_y += 0.5
            bird_rect = display.blit(bird0_image,(BIRD_X,bird_y))
            if warting == 50:
                warting = 0
        rect_dead = display.blit(dead_image,(x4,600))
        x4 -= speed
        if x4 < -20:
            x4 = 0
# Chim rơi
    else: # game chạy
        if bird_y < 570:
            bird_y += drop_bird
            drop_bird += SPEED_BIRD
            angle_bird_down += 1
        if angle_bird_down > 38: # góc chim hạ độ cao
            angle_bird = -20
    #Cột thứ nhất  
        rect1_up = display.blit(top_image,(x1_up,hight1_up - SPACE - 350)) # x1 top
        rect1_down = display.blit(bottom_image,(x1_up,hight1_up))           # x1 bottom
        x1_up -= speed
    # Cột thứ 2
        rect2_up = display.blit(top_image,(x2_up,hight2_up - SPACE - 350)) # x2 top
        rect2_down = display.blit(bottom_image,(x2_up,hight2_up))           # x2 bottom
        x2_up -= speed # cột 2 chạy
    # Cột thứ 3
        rect3_up = display.blit(top_image,(x3_up,hight3_up - SPACE - 350)) # x2 top
        rect3_down = display.blit(bottom_image,(x3_up,hight3_up))           # x2 bottom
        x3_up -= speed # cột 3 chạy
    # mặt đất
        rect_dead = display.blit(dead_image,(x4,600))
        x4 -= speed
    # góc của bird
        angle0_image = pygame.transform.rotate(bird0_image, angle_bird)
        angle1_image = pygame.transform.rotate(bird1_image, angle_bird)
        angle2_image = pygame.transform.rotate(bird2_image, angle_bird) 
        angle_die_image = pygame.transform.rotate(die_image, angle_bird)
    #game over
        if play_again:
            pygame.draw.rect(display,BLACK,(150,240, 100, 110),border_radius=10) # hcn SCORE
            pygame.draw.rect(display,YELLOW,(151,241, 98, 108),border_radius=10) # hcn SCORE
            game_over = fontG.render("GAME OVER", True, BLACK)
            display.blit(gameover_image,(80,150)) 
            score_txt = fontG.render(f"SCORE", True,ORANGE )
            display.blit(score_txt,(155,250)) # score text
            display.blit(score_text,(190,270)) # score
            restart_rect = display.blit(restart_image,(100,400)) # restart text
            bird_rect = display.blit(angle_die_image,(BIRD_X,bird_y)) # chim die
    #vẽ điểm
        else:
            score_text = font.render(f"{score}", True,WHITE)
            display.blit(score_text,(190,70))
            # chim bay
            fly += 1
            if fly < 10:
                bird_rect = display.blit(angle0_image,(BIRD_X,bird_y))
            elif 10 <= fly < 20:
                bird_rect = display.blit(angle1_image,(BIRD_X,bird_y))
            elif 20 <= fly <= 30:
                bird_rect = display.blit(angle2_image,(BIRD_X,bird_y))
                if fly == 30:
                    fly = 0
    # cột chuyển động
        if x1_up < -70:
            x1_up = 670
            hight1_up = randint(250,450)
            score_plus = False
        elif x2_up < -70:
            x2_up = 670
            hight2_up = randint(250,450)
            score_plus = False
        elif x3_up < -70:
            x3_up = 670
            hight3_up = randint(250,450)
            score_plus = False
        elif x4 < -20:
            x4 = 0
    # cộng điểm
        if x1_up < 77 and not score_plus:
            score += 1
            score_plus = True
            pygame.mixer.Sound.play(sound_score)
        if x2_up < 77 and not score_plus:
            score += 1
            score_plus = True
            pygame.mixer.Sound.play(sound_score)
        if x3_up < 77 and not score_plus:
            score += 1
            score_plus = True
            pygame.mixer.Sound.play(sound_score)
    # Phát hiện va chạm
        for rect in [rect1_up, rect1_down, rect2_up, rect2_down, rect3_up, rect3_down, rect_dead]: # va chạm cột và mặt đất
            if bird_rect.colliderect(rect):
                if not sound_play:
                    pygame.mixer.Sound.play(sound_gameover)
                    sound_play = True
                speed = 0
                drop_bird = 2
                play_again = True
                angle_bird = -90
                
    #bắt bàn phím và chuột
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE and not running: # bắt phím space
                running = True
            if event.key == pygame.K_SPACE: # bắt phím space
                if bird_rect[1] > 10 and not play_again:
                    drop_bird = 0
                    drop_bird -= 8
                    angle_bird = 20
                    angle_bird_down = 0
                elif play_again: # chơi tiếp
                    ReStart()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not running:
                running = True
            if event.button == 1:
                if bird_rect[1] > 10 and not play_again:
                    drop_bird = 0
                    drop_bird -= 8
                    angle_bird = 20
                    angle_bird_down = 0
                elif 100 <= mouse_x <= 300 and 400 <= mouse_y <= 457 and play_again: # chơi tiếp
                    ReStart()
    pygame.display.flip()
pygame.quit() 
 

