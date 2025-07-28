import pygame
import math
pygame.init()
pygame.mixer.init()

sound1 = pygame.mixer.Sound("alarm1.wav") # file âm thanh kết thúc
sound3 = pygame.mixer.Sound("tut3s.mp3") # âm thanh 3s

class Clock(): # Lớp đồng hồ
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s
        self.sum_new = 0
        self.sum_s = 0
    def tick(self): # giảm đi 1 s
        if self.s > 0:
            self.s -= 1
        else:
            if self.m > 0:
                self.m -= 1
                self.s = 59
            else:
                if self.h > 0:
                    self.h -= 1
                    self.m = 59
                    self.s = 59
        self.sum_new = (self.h * 3600) + (self.m * 60) + self.s
    def Sum_s(self):    # tính tổng số s
        self.sum_s = (self.h * 3600) + (self.m * 60) + self.s
    
BG_COLOR = (140, 140, 140) #    màu
WHITE = (255,255,255)
BACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

display = pygame.display.set_mode((500,600))    # Set màn hình, font, chữ
pygame.display.set_caption("Đồng Hồ Đếm Ngược")
font = pygame.font.SysFont("Courier", 25)
fontA = pygame.font.SysFont("Courier", 50)
start_txt = font.render("START",True, BACK)
pause_txt = font.render("PAUSE",True, BACK)
reset_txt = font.render("RESET",True, BACK)
hrs_txt = font.render("HRS", True,WHITE)
min_txt = font.render("MIN", True,WHITE)
sec_txt = font.render("SEC", True,WHITE)
plus = font.render("+",True, RED)
minus = font.render("-",True, RED)

total_second = Clock(0,0,0) # khởi tạo đồng hồ
hz = pygame.time.Clock()
last_time = pygame.time.get_ticks()

run = True
starting = False
pause = False
while run:      #Vòng lặp chính
    hz.tick(60)
    display.fill(BG_COLOR)
    h_text = fontA.render(f"{total_second.h:02}",True,BACK) # vẽ thời gian thực
    m_text = fontA.render(f"{total_second.m:02}",True,BACK)
    s_text = fontA.render(f"{total_second.s:02}",True,BACK)

    pygame.draw.rect(display, WHITE, (100,30, 110, 50),border_radius=10) # hcn Start
    display.blit(start_txt, (115, 40))
    pygame.draw.rect(display, WHITE, (300,30, 110, 50),border_radius=10) # hcn Reset
    display.blit(reset_txt, (317, 40))
    pygame.draw.rect(display, BACK, (113,118, 84, 54))
    pygame.draw.rect(display, WHITE, (115,120, 80, 50)) # vẽ hcn h
    display.blit(hrs_txt, (130, 170)) # hrs
    display.blit(h_text, (125, 120)) # h

    pygame.draw.rect(display, BACK, (213,118, 84, 54))
    pygame.draw.rect(display, WHITE, (215,120, 80, 50)) # vẽ m
    display.blit(min_txt, (230, 170)) # min
    display.blit(m_text, (225, 120)) # m
    
    pygame.draw.rect(display, BACK, (313,118, 84, 54))
    pygame.draw.rect(display, WHITE, (315,120, 80, 50)) # vẽ s
    display.blit(sec_txt, (330, 170)) # sec
    display.blit(s_text, (325, 120)) # s

    pygame.draw.rect(display, BACK, (50,530, 400, 50)) # timeline
    pygame.draw.rect(display, WHITE, (55,535, 390, 40))
    
    if not starting:
        display.blit(plus, (115, 130)) # + h
        display.blit(minus, (180, 130)) # - h
        display.blit(plus, (215, 130)) # + m
        display.blit(minus, (280, 130)) # - m
        display.blit(plus, (315, 130)) # + s
        display.blit(minus, (380, 130)) # - s
    else:
        if not pause:
            pygame.draw.rect(display, GREEN, (100,30, 110, 50),border_radius=10) # hcn pause
            display.blit(pause_txt, (115, 40)) # pause
        if total_second.sum_s > 0:
            pygame.draw.rect(display, GREEN, (55,535, 390 * (total_second.sum_new/total_second.sum_s), 40)) # timeline đếm


    pygame.draw.circle(display,BACK,(250,370), 120)  # đồng hồ
    pygame.draw.circle(display,WHITE,(250,370), 115) # hình tròn
    pygame.draw.circle(display,BACK,(250,370),3)
    
    x_sec = 250 + (100 * math.sin((total_second.s * 6 * math.pi)/180)) # tính s tọa độ x,y mới
    y_sec = 370 - (100 * math.cos((total_second.s * 6 * math.pi)/180))
    pygame.draw.line(display,BACK,(250,370),(x_sec, y_sec)) # vẽ kim s theo s hiện tại
    x_min = 250 + (60 * math.sin((total_second.m * 6 * math.pi)/180))# tính m tọa độ x,y mới
    y_min = 370 - (60 * math.cos((total_second.m * 6 * math.pi)/180))
    pygame.draw.line(display,RED,(250,370),(x_min, y_min)) # vẽ kim m theo m hiện tại
    x_hrs = 250 + (40 * math.sin((total_second.h * 15 * math.pi)/180))# tính h tọa độ x,y mới
    y_hrs = 370 - (40 * math.cos((total_second.h * 15 * math.pi)/180))
    pygame.draw.line(display,GREEN,(250,370),(x_hrs, y_hrs)) # vẽ kim m theo m hiện tại

    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get(): # sự kiện chuột
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # click left
                if not starting:
                    if 115 <= mouse_x <= 145 and 120 <= mouse_y <= 160: # + h
                        total_second.h += 1
                        if total_second.h == 25:
                            total_second.h = 0
                    elif 170 <= mouse_x <= 190 and 120 <= mouse_y <= 160: # - h
                        if total_second.h > 0:
                            total_second.h -= 1
                    elif 215 <= mouse_x <= 245 and 120 <= mouse_y <= 160: # + m
                        total_second.m += 1
                        if total_second.m == 59:
                            total_second.m = 0
                    elif 270 <= mouse_x <= 290 and 120 <= mouse_y <= 160: # - m
                        if total_second.m > 0:
                            total_second.m -= 1
                    elif 315 <= mouse_x <= 345 and 120 <= mouse_y <= 160: # + s
                        total_second.s += 1
                        if total_second.s == 59:
                            total_second.s = 0
                    elif 370 <= mouse_x <= 390 and 120 <= mouse_y <= 160: # - s
                        if total_second.s > 0:
                            total_second.s -= 1
                if 300 <= mouse_x <= 410 and 30 <= mouse_y <= 80: # Reset
                    total_second.h=total_second.m=total_second.s = 0
                elif 100 <= mouse_x <= 210 and 30 <= mouse_y <= 80: # Start
                    if not starting:
                        total_second.Sum_s()
                        starting = True
                        pause = False
                        last_time = pygame.time.get_ticks()
                    else:                                           # Pause
                        pause = not pause
    
    if starting and not pause:
        current_time = pygame.time.get_ticks()
        if current_time - last_time >= 1000:  # 1 s thời gian thực
            total_second.tick()
            last_time = current_time
            if total_second.h == 0 and total_second.m == 0:
                if total_second.s == 3:
                    pygame.mixer.Sound.play(sound3)
                elif total_second.s == 0:
                    starting = False
                    pygame.mixer.Sound.play(sound1)

    pygame.display.flip()

pygame.quit()
