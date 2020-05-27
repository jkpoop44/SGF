# Image,Sound source copyright in Sunborn Network Technology Co., Ltd.

# Update 2020-05-27
# SGF Ver.4

# https://drive.google.com/file/d/1HxtinkQz_MVx3joWSzrbq4Yp8BmLMO7J/view?usp=sharing


import pygame as pg
import os
import random


# 기본값 설정
pg.init()
time_delay = 0
clock = pg.time.Clock()
FPS = 25
rotate = False
sop_x = 0
sop_y = 100
speed = 8
dx = 0
dy = 0
main_run = True
right = False
left = False
up = False
down = False
count = 0

bulletXY = []

starXY =[]
star_num = 0
dieXY = []
star_die_num = 0 

jaegerXY =[]
jaeger_num = 0
jaegerdieXY = []
jaeger_die_num = 0 

dragoonXY =[]
dragoon_num = 0
dragoondieXY = []
dragoon_die_num = 0 

grenadeXY = []
grenadeboomXY = []
cooltime = 0

score = 0
e_speed = 0
pause = False
life = 3
high_score = score
done = False

skill_done = 0

# 리셋
def reset():
    global sop_x,sop_y,speed,dx,main_run,save,bulletXY,starXY,star_num,dieXY,\
        star_die_num,jaegerXY,jaeger_num,jaegerdieXY,jaeger_die_num,score,e_speed,pause,life,\
            dragoonXY,dragoon_num,dragoondieXY,dragoon_die_num,grenadeXY,stard_rect,drd_rect,jd_rect,bullet
    sop_x = 0
    sop_y = 100
    speed = 8
    dx = 0
    dy = 0
    main_run = True
    save = []
    bulletXY = []
    starXY =[]
    star_num = 0
    dieXY = []
    star_die_num = 0 
    jaegerXY =[]
    jaeger_num = 0
    jaegerdieXY = []
    jaeger_die_num = 0 
    dragoonXY =[]
    dragoon_num = 0
    dragoondieXY = []
    dragoon_die_num = 0     
    score = 0
    e_speed = 3
    pause = False
    life = 3
    grenadeXY = []

    dragoon_die_png = dragoon_die_img[0]
    dragoon_die_ori = pg.image.load(os.path.join(dragoon_die_path,f'{dragoon_die_png}'))
    dragoon_die_rect = dragoon_die_ori.get_rect().size
    dragoon_die_i = pg.transform.scale(dragoon_die_ori,(int(screen_height*0.25*dragoon_die_rect[0]/dragoon_die_rect[1]) , int(screen_height*0.25)))
    drd_rect = dragoon_die_i.get_rect().size

    star_die_png = star_die_img[0]
    star_die_ori = pg.image.load(os.path.join(star_die_path,f'{star_die_png}'))
    star_die_rect = star_die_ori.get_rect().size
    star_die_i = pg.transform.scale(star_die_ori,(int(screen_height*0.25*star_die_rect[0]/star_die_rect[1]) , int(screen_height*0.25)))
    stard_rect = star_die_i.get_rect().size

    jaeger_die_png = jaeger_die_img[0]
    jaeger_die_ori = pg.image.load(os.path.join(jaeger_die_path,f'{jaeger_die_png}'))
    jaeger_die_rect = jaeger_die_ori.get_rect().size
    jaeger_die_i = pg.transform.scale(jaeger_die_ori,(int(screen_height*0.25*jaeger_die_rect[0]/jaeger_die_rect[1]) , int(screen_height*0.25)))
    jd_rect = jaeger_die_i.get_rect().size

    bullet = pg.transform.scale(bullet_ori,(int(screen_height*0.3/4),int((screen_height*0.3/4)*(bullet_rect.height/bullet_rect.width))))
    health = pg.transform.scale(health_ori,(int(screen_height*0.3/4),int((screen_height*0.3/4)*(health_rect.height/health_rect.width))))

#모니터 정보
monitor = pg.display.Info()


#기본 색상
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (220,20,20)
GREEN = (40,170,40)


# 기본 출력화면 설정
screen_width = 800
screen_height = int(screen_width*0.45)
screen = pg.display.set_mode((screen_width,screen_height))
resize = (screen_width,screen_height)
pg.display.set_caption('SGF')


# 폴더 경로 지정
current_path = os.path.dirname(__file__)
data_path = os.path.join(current_path, 'data')
font_path = os.path.join(current_path,'font')

sop_path = os.path.join(data_path, 'sop')
sop_run_path = os.path.join(sop_path,'sop_run')
sop_wait_path = os.path.join(sop_path,'sop_wait')
sop_shoot_path = os.path.join(sop_path,'sop_shoot')
sop_skill_path = os.path.join(sop_path,'sop_skill')

battle_path = os.path.join(data_path,'battle')

star_path = os.path.join(data_path,'star')
star_run_path = os.path.join(star_path,'star_run')
star_die_path = os.path.join(star_path,'star_die')

jaeger_path = os.path.join(data_path,'jaeger')
jaeger_run_path = os.path.join(jaeger_path,'jaeger_run')
jaeger_die_path = os.path.join(jaeger_path,'jaeger_die')

dragoon_path = os.path.join(data_path,'dragoon')
dragoon_run_path = os.path.join(dragoon_path,'dragoon_run')
dragoon_die_path = os.path.join(dragoon_path,'dragoon_die')

grenade_path = os.path.join(data_path,'grenade')


# 폴더별 이미지 리스트 작성
sop_run_img = os.listdir(os.path.join(sop_path,'sop_run'))
sop_shoot_img = os.listdir(os.path.join(sop_path,'sop_shoot'))
sop_wait_img = os.listdir(os.path.join(sop_path,'sop_wait'))
sop_skill_img = os.listdir(os.path.join(sop_path,'sop_skill'))

star_run_img = os.listdir(os.path.join(star_path,'star_run'))
star_die_img = os.listdir(os.path.join(star_path,'star_die'))

jaeger_run_img = os.listdir(os.path.join(jaeger_path,'jaeger_run'))
jaeger_die_img = os.listdir(os.path.join(jaeger_path,'jaeger_die'))

dragoon_run_img = os.listdir(os.path.join(dragoon_path,'dragoon_run'))
dragoon_die_img = os.listdir(os.path.join(dragoon_path,'dragoon_die'))


# 개별 이미지 불러오기
bullet_ori = pg.image.load(os.path.join(data_path,'Bullet.png'))
bullet_rect = bullet_ori.get_rect() 
bullet = pg.transform.scale(bullet_ori,(int(screen_height*0.3/4),int((screen_height*0.3/4)*(bullet_rect.height/bullet_rect.width))))

health_ori = pg.image.load(os.path.join(data_path,'health.png'))
health_rect = health_ori.get_rect() 
health = pg.transform.scale(health_ori,(int(screen_height*0.3/4),int((screen_height*0.3/4)*(health_rect.height/health_rect.width))))

grenade_ori = pg.image.load(os.path.join(grenade_path,'grenade.png'))
grenade_rect =grenade_ori.get_rect()
grenade_img = pg.transform.scale(grenade_ori, (int(screen_width*0.3*0.1), int(screen_width*0.3*0.1*grenade_rect.height/grenade_rect.width)))

grenade_boom_ori = pg.image.load(os.path.join(grenade_path,'grenade_boom.png'))
grenade_boom_rect =grenade_boom_ori.get_rect()
grenade_boom_img = pg.transform.scale(grenade_boom_ori, ((int(screen_width*0.3), int(screen_width*0.3*grenade_boom_rect.height/grenade_boom_rect.width))))
grenade_boom_img_rect = grenade_boom_img.get_rect().size

# 배경화면 호출
fourth_original = pg.image.load(os.path.join(data_path,'4th login.png'))
expo_original = pg.image.load(os.path.join(data_path,'expo login.png'))
bridge_original = pg.image.load(os.path.join(battle_path,'Bridge.png'))

# 디폴트 폰트
default_font = pg.font.Font(os.path.join(font_path,'NanumGothic.ttf'),15)

# 이미지 가로,세로 크기 정보 불러오기
fourth_rect =fourth_original.get_rect() 
expo_rect = expo_original.get_rect()
bridge_rect = bridge_original.get_rect()


# 이미지 비율에 맞춰 확대 및 축소
fourth = pg.transform.scale(fourth_original, ((screen_width, int(screen_width*fourth_rect.height/fourth_rect.width))))
expo = pg.transform.scale(expo_original, ((screen_width,int(screen_width*expo_rect.height/expo_rect.width))))
bridge = pg.transform.scale(bridge_original, ((screen_width,int(screen_width*expo_rect.height/expo_rect.width))))


# 배경화면 지정
backgrounds = [fourth,expo]
background = fourth
battle = bridge


# 개별 이미지 그리기
def drawObject(obj,x,y):
    global screen
    screen.blit(obj,(int(x),int(y)))     

# 이미지 크기 재설정
def background_img():
    global screen_height,screen_width,fourth,expo,bridge

    fourth = pg.transform.scale(fourth_original, ((screen_width, int(screen_width*fourth_rect.height/fourth_rect.width))))
    expo = pg.transform.scale(expo_original, ((screen_width,int(screen_width*expo_rect.height/expo_rect.width))))
    bridge = pg.transform.scale(bridge_original, ((screen_width,int(screen_width*expo_rect.height/expo_rect.width))))   
    
# 전투 배경
def Battle_back():
    global screen_width,screen_height
    screen.fill([0,0,0])                  
    rotated = pg.transform.rotate(battle,0)
    rect = rotated.get_rect()
    rect.center = (screen_width/2,screen_height/2)
    screen.blit(rotated,rect)

# 일반 배경
def Background():
    global screen_width,screen_height,screen_width,screen_height
    screen.fill([0,0,0])                  
    rotated = pg.transform.rotate(background,0)
    rect = rotated.get_rect()
    rect.center = (screen_width/2,screen_height/2)
    screen.blit(rotated,rect)

# 도움말
def Help():
    h_font = pg.font.Font(os.path.join(font_path,'NanumGothic.ttf'),16)
    h_line_1 = h_font.render('인게임 // 조작 방향키 // S 공격 // A 스킬 // P 일시정지 // ESC 메인화면',True,WHITE)
    h_line_2 = h_font.render('돌아가기 H',True,WHITE)
    screen.blit(h_line_1,(screen_width*0.02,40))
    screen.blit(h_line_2,(screen_width*0.02,screen_height-40))

# 일시정지
def Pause():
    global pause
    
    pause_font = pg.font.Font(os.path.join(font_path,'NanumGothic.ttf'),30)
    pause_text = pause_font.render('press P to continue',True,WHITE)
    pause_rect = pause_text.get_rect()
    pause_rect.center = (screen_width/2,screen_height/2)
    while pause:
        screen.blit(pause_text,(pause_rect))
        pg.display.update()
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    pause = False

# 몹 이동 속도
def Speed():
    global e_speed
    if 100 >= score >= 25:
        if e_speed < 7:
            e_speed = 3+((score-25)/20)
        else:
            e_speed = 7
    if score > 100:
        if e_speed < 9:
            e_speed = 6+((score-100)/120)
        else:
            e_speed = 9
        
# 게임오버
def Game_over():
    global life, score,high_score
    
    GO_font = pg.font.Font(os.path.join(font_path,'NanumGothic.ttf'),25)

    GO_text = GO_font.render('press R to restart',True,RED)
    GO_rect = GO_text.get_rect()
    GO_rect.center = (screen_width/2,screen_height/2-50)

    GO_score_text = GO_font.render(f'처치수 : {score}',True,WHITE)
    GO_score_rect = GO_score_text.get_rect()
    GO_score_rect.center = (screen_width/2,(screen_height/2))

    GO_high_score_text = GO_font.render(f'최고 처치수 : {high_score}',True,WHITE)
    GO_high_score_rect = GO_high_score_text.get_rect()
    GO_high_score_rect.center = (screen_width/2,(screen_height/2)+50)

    restart = False
    if life <= 0:
        while not restart:
            screen.blit(GO_text,(GO_rect))
            screen.blit(GO_score_text,(GO_score_rect))
            screen.blit(GO_high_score_text,(GO_high_score_rect))
            pg.display.update()
            for event in pg.event.get(): 
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        restart = True    
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
        
        main_loop()
        
        
    else:
        if life == 3:
            screen.blit(health,(int(screen_width*0.4),int(screen_height*0.05)))
            screen.blit(health,(int(screen_width*0.36),int(screen_height*0.05)))
            screen.blit(health,(int(screen_width*0.32),int(screen_height*0.05)))
        if life == 2:
            screen.blit(health,(int(screen_width*0.36),int(screen_height*0.05)))
            screen.blit(health,(int(screen_width*0.32),int(screen_height*0.05)))
        if life == 1:
            screen.blit(health,(int(screen_width*0.32),int(screen_height*0.05)))
        
# STAR15 RUN
def star_def():
        global starXY,star_num,star_i,star_rect,e_speed,life
        
        if star_num < len(star_run_img):
            star_png = star_run_img[star_num]
            star_ori = pg.image.load(os.path.join(star_run_path,f'{star_png}'))
            star_i = pg.transform.scale(star_ori,(int(screen_height*0.25) , int(screen_height*0.25)))
            star_i = pg.transform.flip(star_i,True, False)
            star_rect = star_i.get_rect().size
        elif star_num >= len(star_run_img):
            star_num = 0

        if len(starXY) <= 1:
            starX = int(screen_width*1.1)
            starY = random.randint(int(int(screen_height*0.05)),screen_height-star_rect[1])
            starXY.append([starX,starY])

        if len(starXY) != 0:
            for sx,sy in starXY:
                drawObject(star_i, sx, sy)
                
        if len(starXY) != 0:
            for j,sxy in enumerate(starXY):
                sxy[0] -= int(e_speed*0.9)
                starXY[j][0] = sxy[0]

                if sxy[0] < 0-star_rect[0] :
                    try:
                        starXY.remove(sxy)
                        life -= 1
                    except:
                        print('err')
                        pass
        star_num += 1

# STAR15 DIE
def star_die_def():
    global dieXY

    if len(dieXY) != 0:
        for l,dxy in enumerate(dieXY):                
            dieXY[l][0] = dxy[0]
            dieXY[l][1] = dxy[1]
            

            if dxy[2] >= len(star_die_img)+5:               
                dieXY.remove(dxy)
            
            if dxy[2] < len(star_die_img):      
                star_die_num = dxy[2]
                star_die_png = star_die_img[star_die_num]
                star_die_ori = pg.image.load(os.path.join(star_die_path,f'{star_die_png}'))
                star_die_rect = star_die_ori.get_rect().size
                star_die_i = pg.transform.scale(star_die_ori,(int(screen_height*0.25*star_die_rect[0]/star_die_rect[1]) , int(screen_height*0.25)))
                star_die_i = pg.transform.flip(star_die_i,True, False)
                drawObject(star_die_i, dxy[0], dxy[1])
                dieXY[l][2] = dxy[2]+1

# Jaeger RUN
def jaeger_def():
        global jaegerXY,jaeger_num,jaeger_i,jaeger_rect,e_speed,life
        if jaeger_num < len(jaeger_run_img):
            jaeger_png = jaeger_run_img[jaeger_num]
            jaeger_ori = pg.image.load(os.path.join(jaeger_run_path,f'{jaeger_png}'))
            jaeger_ori_rect = jaeger_ori.get_rect().size
            jaeger_i = pg.transform.scale(jaeger_ori,(int(screen_height*0.25*jaeger_ori_rect[0]/jaeger_ori_rect[1]) , int(screen_height*0.25)))
            jaeger_i = pg.transform.flip(jaeger_i,False, False)
            jaeger_rect = jaeger_i.get_rect().size
        elif jaeger_num >= len(jaeger_run_img):
            jaeger_num = 0

        if len(jaegerXY)  <= 2:
            jaegerX = int(screen_width*1.1)
            jaegerY = random.randint(int(screen_height*0.05),screen_height-jaeger_rect[1])
            jaegerXY.append([jaegerX,jaegerY])

        if len(jaegerXY) != 0:
            for jx,jy in jaegerXY:
                drawObject(jaeger_i, jx, jy)
                
        if len(jaegerXY) != 0:
            for jae,jxy in enumerate(jaegerXY):
                jxy[0] -= int(e_speed*0.7)
                jaegerXY[jae][0] = jxy[0]

                if jxy[0] < 0-jaeger_rect[0] :
                    try:
                        jaegerXY.remove(jxy)
                        life -= 1
                    except:
                        print('err')
                        pass
        jaeger_num += 1

# Jaeger DIE
def jaeger_die_def():
    global jaegerdieXY,jaeger_die_rect,jd_rect
    
    if len(jaegerdieXY) != 0:
        for jd,jdxy in enumerate(jaegerdieXY):                
            jaegerdieXY[jd][0] = jdxy[0]
            jaegerdieXY[jd][1] = jdxy[1]
            

            if jdxy[2] >= len(jaeger_die_img)+5:                
                    jaegerdieXY.remove(jdxy)
            
            if jdxy[2] < len(jaeger_die_img):      
                jaeger_die_num = jdxy[2]
                jaeger_die_png = jaeger_die_img[jaeger_die_num]
                jaeger_die_ori = pg.image.load(os.path.join(jaeger_die_path,f'{jaeger_die_png}'))
                jaeger_die_rect = jaeger_die_ori.get_rect().size
                jaeger_die_i = pg.transform.scale(jaeger_die_ori,(int(screen_height*0.25*jaeger_die_rect[0]/jaeger_die_rect[1]) , int(screen_height*0.25)))
                jd_rect = jaeger_die_i.get_rect().size
                drawObject(jaeger_die_i, jdxy[0], jdxy[1])
                jaegerdieXY[jd][2] = jdxy[2]+1

# dragoon RUN
def dragoon_def():
        global dragoonXY,dragoon_num,dragoon_i,dragoon_rect,e_speed,life
        if dragoon_num < len(dragoon_run_img):
            dragoon_png = dragoon_run_img[dragoon_num]
            dragoon_ori = pg.image.load(os.path.join(dragoon_run_path,f'{dragoon_png}'))
            dragoon_ori_rect = dragoon_ori.get_rect().size
            dragoon_i = pg.transform.scale(dragoon_ori,(int(screen_height*0.25*dragoon_ori_rect[0]/dragoon_ori_rect[1]) , int(screen_height*0.25)))
            dragoon_i = pg.transform.flip(dragoon_i,False, False)
            dragoon_rect = dragoon_i.get_rect().size
        elif dragoon_num >= len(dragoon_run_img):
            dragoon_num = 0

        if len(dragoonXY)  <= 0:
            dragoonX = int(screen_width*1.1)
            dragoonY = random.randint(int(screen_height*0.05),screen_height-dragoon_rect[1])
            dragoonXY.append([dragoonX,dragoonY])

        if len(dragoonXY) != 0:
            for drx,dry in dragoonXY:
                drawObject(dragoon_i, drx, dry)
                
        if len(dragoonXY) != 0:
            for dr,drxy in enumerate(dragoonXY):
                drxy[0] -= int(e_speed*1)
                dragoonXY[dr][0] = drxy[0]

                if drxy[0] < 0-dragoon_rect[0] :
                    try:
                        dragoonXY.remove(drxy)
                        life -= 1
                    except:
                        print('err')
                        pass
        dragoon_num += 1

# dragoon DIE
def dragoon_die_def():
    global dragoondieXY,dragoon_die_rect

    if len(dragoondieXY) != 0:
        for drd,drdxy in enumerate(dragoondieXY):                
            dragoondieXY[drd][0] = drdxy[0]
            dragoondieXY[drd][1] = drdxy[1]
            

            if drdxy[2] >= len(dragoon_die_img)+5:                
                    dragoondieXY.remove(drdxy)
            
            if drdxy[2] < len(dragoon_die_img):      
                dragoon_die_num = drdxy[2]
                dragoon_die_png = dragoon_die_img[dragoon_die_num]
                dragoon_die_ori = pg.image.load(os.path.join(dragoon_die_path,f'{dragoon_die_png}'))
                dragoon_die_rect = dragoon_die_ori.get_rect().size
                dragoon_die_i = pg.transform.scale(dragoon_die_ori,(int(screen_height*0.25*dragoon_die_rect[0]/dragoon_die_rect[1]) , int(screen_height*0.25)))
                drawObject(dragoon_die_i, drdxy[0], drdxy[1])
                dragoondieXY[drd][2] = drdxy[2]+1

# 탄환
def Bullet_def():
    global bulletXY,score
    if len(bulletXY) != 0:
        for k,bxy in enumerate(bulletXY):
            bxy[0] += 25
            bulletXY[k][0] = bxy[0]
            if bxy[0] > screen_width:
                try:
                    bulletXY.remove(bxy)
                except:
                    pass 

            for j,sxy in enumerate(starXY):
                starXY[j][0] = sxy[0]
                starXY[j][1] = sxy[1]
                if bxy[0] >= sxy[0] and bxy[0] <= sxy[0]+star_rect[0] and bxy[1] >= sxy[1] and bxy[1] <= sxy[1]+star_rect[1]:
                    try:                               
                        dieX = sxy[0]
                        dieY = sxy[1]
                        dieXY.append([dieX,dieY,0])

                                
                        bulletXY.remove(bxy)
                        starXY.remove(sxy)
                        score += 1
                    except:                               
                        pass

            for jae,jxy in enumerate(jaegerXY):
                jaegerXY[jae][0] = jxy[0]
                jaegerXY[jae][1] = jxy[1]
                if bxy[0] >= jxy[0] and bxy[0] <= jxy[0]+jaeger_rect[0] and bxy[1] >= jxy[1] and bxy[1] <= jxy[1]+jaeger_rect[1]:
                    try:                             
                        jaegerdieX = jxy[0]
                        jaegerdieY = jxy[1]
                        jaegerdieXY.append([jaegerdieX,jaegerdieY,0])
                        bulletXY.remove(bxy)
                        jaegerXY.remove(jxy)
                        score += 1
                    except:
                        print('err')                               
                        pass
                    
            for dr,drxy in enumerate(dragoonXY):
                dragoonXY[dr][0] = drxy[0]
                dragoonXY[dr][1] = drxy[1]
                if bxy[0] >= drxy[0] and bxy[0] <= drxy[0]+dragoon_rect[0] and bxy[1] >= drxy[1] and bxy[1] <= drxy[1]+dragoon_rect[1]:
                    try:                             
                        dragoondieX = drxy[0]
                        dragoondieY = drxy[1]
                        dragoondieXY.append([dragoondieX,dragoondieY,0])
                        bulletXY.remove(bxy)
                        dragoonXY.remove(drxy)
                        score += 1
                    except:
                        print('err')                               
                        pass

# 점수
def Score():
    global score,high_score
    white = (255,255,255)
    score_text = default_font.render(f'처치수 : {score}',True,white)
    high_score_text = default_font.render(f'최고 처치수 : {high_score}',True,white)
    screen.blit(score_text,(30,10))
    screen.blit(high_score_text,(30,30))
    if score >= high_score:
        high_score = score

# grenade
def Grenade():
    global cooltime, grenadeXY,grenadeboomXY,score,skill_done
    
    line_1 = default_font.render(f'유탄 : {skill_done}',True,WHITE)
    line_2 = default_font.render(f'쿨다운 : {round(cooltime,1)}',True,WHITE)
    if len(grenadeXY) != 0:
        for gre, grexy in enumerate(grenadeXY):
            grexy[0] += 50
            grenadeXY[gre][0] =grexy[0]
            if grexy[0] > screen_width:
                gredX = grexy[0] - grenade_boom_img_rect[0]*0.6
                gredY = grexy[1] - grenade_boom_img_rect[1]/2
                grenadeboomXY.append([gredX,gredY,0])
                grenadeXY.remove(grexy)
    
    if len(grenadeXY) != 0:
        for gre, grexy in enumerate(grenadeXY):
            
            for j,sxy in enumerate(starXY):
                        starXY[j][0] = sxy[0]
                        starXY[j][1] = sxy[1]
                        if grexy[0] >= sxy[0] and grexy[1] >= sxy[1] and grexy[0] <= sxy[0]+star_rect[0] and grexy[1] <= sxy[1]+star_rect[1]:
                            try:                               
                                dieX = sxy[0]
                                dieY = sxy[1]
                                dieXY.append([dieX,dieY,0])
                                gredX = grexy[0] - grenade_boom_img_rect[0]/3
                                gredY = grexy[1] - grenade_boom_img_rect[1]/2
                                grenadeboomXY.append([gredX,gredY,0])
                                grenadeXY.remove(grexy)
                                starXY.remove(sxy)
                                score += 1
                            except:                               
                                pass

            for jae,jxy in enumerate(jaegerXY):
                        jaegerXY[jae][0] = jxy[0]
                        jaegerXY[jae][1] = jxy[1]
                        if grexy[0] >= jxy[0] and grexy[0] <= jxy[0]+jaeger_rect[0] and grexy[1] >= jxy[1] and grexy[1] <= jxy[1]+jaeger_rect[1]:
                            try:                             
                                jaegerdieX = jxy[0]
                                jaegerdieY = jxy[1]
                                jaegerdieXY.append([jaegerdieX,jaegerdieY,0])
                                gredX = grexy[0] - grenade_boom_img_rect[0]/3
                                gredY = grexy[1] - grenade_boom_img_rect[1]/2
                                grenadeboomXY.append([gredX,gredY,0])
                                grenadeXY.remove(grexy)
                                jaegerXY.remove(jxy)
                                score += 1
                            except:
                                print('err')                               
                                pass
                    
            for dr,drxy in enumerate(dragoonXY):
                        dragoonXY[dr][0] = drxy[0]
                        dragoonXY[dr][1] = drxy[1]
                        if grexy[0] >= drxy[0] and grexy[1] >= drxy[1] and grexy[0] <= drxy[0]+dragoon_rect[0] and grexy[1] <= drxy[1]+dragoon_rect[1]:
                            try:                             
                                dragoondieX = drxy[0]
                                dragoondieY = drxy[1]
                                dragoondieXY.append([dragoondieX,dragoondieY,0])
                                gredX = grexy[0] - grenade_boom_img_rect[0]/3
                                gredY = grexy[1] - grenade_boom_img_rect[1]/2
                                grenadeboomXY.append([gredX,gredY,0])
                                grenadeXY.remove(grexy)
                                dragoonXY.remove(drxy)
                                score += 1
                            except:
                                print('err')                               
                                pass
    
            screen.blit(grenade_img,(grexy[0]-grenade_rect[0],grexy[1]-grenade_rect[1]))

    cooltime += 0.3
    if cooltime >= 100:
        cooltime -= 100
        skill_done += 1
    screen.blit(line_1,(screen_width*0.8,screen_height*0.83))
    screen.blit(line_2,(screen_width*0.8,screen_height*0.9))
    # print(grenadeboomXY)
    # print(cooltime)
    # print(grenadeXY)

# grenade boom
def Grenadeboom():
    global grenadeboomXY,grenade_boom_num,grenade_boom_img_rect,score

    if len(grenadeboomXY) != 0:
        for greb, grebxy in enumerate(grenadeboomXY):
            if grebxy[2] <= 10:

                screen.blit(grenade_boom_img,(grebxy[0],grebxy[1]))
                grebxy[2] += 1   
                
            if grebxy[2] > 10:
                grenadeboomXY.remove(grebxy)
            
            for j,sxy in enumerate(starXY):
                        starXY[j][0] = sxy[0]
                        starXY[j][1] = sxy[1]
                        if grebxy[0] - stard_rect[0]/2 <= sxy[0] and grebxy[0] + grenade_boom_img_rect[0]- stard_rect[0]/2 >= sxy[0] \
                            and grebxy[1] - stard_rect[1]/2 <= sxy[1] and grebxy[1] + grenade_boom_img_rect[1] -stard_rect[1]/2 >= sxy[1]:
                            try:                               
                                dieX = sxy[0]
                                dieY = sxy[1]
                                starXY.remove(sxy)
                                dieXY.append([dieX,dieY,13])
                                score += 1
                            except:                               
                                pass

            for jae,jxy in enumerate(jaegerXY):
                        jaegerXY[jae][0] = jxy[0]
                        jaegerXY[jae][1] = jxy[1]
                        if grebxy[0] - jd_rect[0]/2 <= jxy[0] and grebxy[0] + grenade_boom_img_rect[0] - jd_rect[0]/2 >= jxy[0] \
                            and grebxy[1] - jd_rect[1]/2 <= jxy[1] and grebxy[1] + grenade_boom_img_rect[1] - jd_rect[1]/2 >= jxy[1]:
                            try:                             
                                jaegerdieX = jxy[0]
                                jaegerdieY = jxy[1]
                                jaegerdieXY.append([jaegerdieX,jaegerdieY,13])
                                jaegerXY.remove(jxy)
                                score += 1
                            except:
                                print('err')                               
                                pass
                    
            for dr,drxy in enumerate(dragoonXY):
                        dragoonXY[dr][0] = drxy[0]
                        dragoonXY[dr][1] = drxy[1]
                        if grebxy[0] - drd_rect[0]/2 <= drxy[0] and grebxy[0] + grenade_boom_img_rect[0] - drd_rect[0]/2 >= drxy[0] \
                            and grebxy[1] - drd_rect[1]/2 <= drxy[1] and grebxy[1] + grenade_boom_img_rect[1] - drd_rect[0]/2 >= drxy[1]:
                            try:                             
                                dragoondieX = drxy[0]
                                dragoondieY = drxy[1]
                                dragoondieXY.append([dragoondieX,dragoondieY,13])
                                dragoonXY.remove(drxy)
                                score += 1
                            except:
                                print('err')                               
                                pass

# Run mode
def sop_run_def():
    global sop_x, sop_y, dx, dy, sopshoot,soprun, sopwait, rotate,right,\
         left, up, down,speed,right,left,up,down,bulletXY
    
    while soprun:
        clock.tick(FPS)
        for i in sop_run_img:
            if not soprun:
                break
            Battle_back()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sopshoot = False
                    soprun = False
                    sopwait = False
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        sopshoot = False
                        soprun = False
                        sopwait = False
                        pg.quit()
                    if event.key == pg.K_s:
                        sopshoot = True
                        dx = 0
                        dy = 0
                        rotate = False
                        right = False
                        left = False
                        up = False
                        down = False
                        Shoot()
                        break
                    if event.key == pg.K_RIGHT:
                        rotate = False
                        dx = speed
                        right = True
                    if event.key == pg.K_LEFT:
                        rotate = True
                        dx = -speed
                        left = True
                    if event.key == pg.K_UP:
                        dy = -speed
                        up = True
                    if event.key == pg.K_DOWN:
                        dy = speed
                        down = True
                    if event.key == pg.K_p:
                        pause = True
                            

                if event.type == pg.KEYUP:   
                    if event.key == pg.K_RIGHT:
                        right = False
                        if not right:
                            if not left:
                                dx = 0
                                if not up:
                                    if not down:
                                        soprun = False
                                        sopwait = True

                    if event.key == pg.K_LEFT:
                        left = False
                        if not right:
                            if not left:
                                dx = 0
                                if not up:
                                    if not down:
                                        soprun = False
                                        sopwait = True
                    if event.key == pg.K_UP:
                        up = False
                        if not up:
                            if not down:
                                dy = 0
                                if not right:
                                    if not left:
                                        soprun = False
                                        sopwait = True                            
                    if event.key == pg.K_DOWN:
                        down = False
                        if not up:
                            if not down:
                                dy = 0
                                if not right:
                                    if not left:
                                        soprun = False
                                        sopwait = True
            
                if not up:
                    if not down: 
                        if not right:
                            if not left:
                                soprun = False
                                sopwait = True
                                break
                            else:
                                pass  
                        else:
                            pass
                    else:
                        pass
                else:
                    pass          
                
                            
            sop_x += dx
            sop_y += dy     

            
            ori = pg.image.load(os.path.join(sop_run_path,f'{i}'))
            i = pg.transform.scale(ori,(int(screen_height*0.3) , int(screen_height*0.3)))           
            i = pg.transform.flip(i,rotate, False)
            
            if len(bulletXY) != 0:
                for bx,by in bulletXY:
                    drawObject(bullet, bx, by)            
            
            screen.blit(i,(sop_x,sop_y))

            sop_rect = i.get_rect().size
            
            if sop_x <= -int(sop_rect[0]*0.25):
                    sop_x = -int(sop_rect[0]*0.25)
            if sop_y <= -int(sop_rect[0]*0.2):
                    sop_y = -int(sop_rect[1]*0.2)
            if sop_x >= screen_width - int(sop_rect[1]*0.8):
                    sop_x = screen_width - int(sop_rect[1]*0.8)
            if sop_y >= screen_height - int(sop_rect[1]*0.8):
                    sop_y = screen_height - int(sop_rect[1]*0.8)
            
            Score()
            Bullet_def()
            Grenade()
            Speed()
            star_def()
            star_die_def()
            jaeger_def()
            jaeger_die_def()
            dragoon_def()
            dragoon_die_def()
            Grenadeboom()
            Pause()
            Game_over()
            pg.display.update()
            pg.time.delay(time_delay)

# wait mode
def sop_wait():
    global sop_x, sop_y, dx, dy, sopshoot, soprun, sopwait, rotate, bulletXY,pause,skill_done

    
    star_num = 0
    
    while sopwait:
        clock.tick(FPS)
        for i in sop_wait_img:
            if not sopwait:
                break
            
            Battle_back()
            ori = pg.image.load(os.path.join(sop_wait_path,f'{i}'))
            i = pg.transform.scale(ori,(int(screen_height*0.3) , int(screen_height*0.3)))
            i = pg.transform.flip(i,rotate, False)
            sop_rect = i.get_rect().size
            if len(bulletXY) != 0:
                for bx,by in bulletXY:
                    drawObject(bullet, bx, by)
                      
            screen.blit(i,(sop_x,sop_y))
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sopshoot = False
                    soprun = False
                    sopwait = False
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        sopshoot = False
                        soprun = False                        
                        sopwait = False
                    if event.key == pg.K_RIGHT:
                        dx = speed
                        right = True
                        rotate = False
                        soprun = True
                        sop_run_def()
                    if event.key == pg.K_LEFT:
                        dx = -speed
                        left = True
                        soprun = True
                        rotate = True
                        sop_run_def()
                    if event.key == pg.K_UP:
                        soprun = True
                        dy = -speed
                        up = True
                        sop_run_def()
                    if event.key == pg.K_DOWN:
                        soprun = True
                        dy = speed
                        down = True
                        sop_run_def()
                    if event.key == pg.K_s:
                        rotate = False
                        sopshoot = True
                        Shoot()
                    if event.key == pg.K_p:
                        pause = True
                    if event.key == pg.K_a:
                        if  skill_done >= 1:
                            Skill()
                if event.type == pg.KEYUP:
                        if event.key == pg.K_RIGHT:
                            dx = 0
                            right = False
                            soprun = False
                            sopwait = True
                        if event.key == pg.K_LEFT:
                            dx = 0
                            left = False
                            soprun = False
                            sopwait = True
                        if event.key == pg.K_UP:
                            dy = 0
                            up = False
                            soprun = False
                            sopwait = True
                        if event.key == pg.K_DOWN:
                            dy = 0
                            down = False
                            soprun = False
                            sopwait = True
                sop_x += dx
                sop_y += dy
            
            if sop_x <= -int(sop_rect[0]*0.25):
                    sop_x = -int(sop_rect[0]*0.25)
            if sop_y <= -int(sop_rect[0]*0.2):
                    sop_y = -int(sop_rect[1]*0.2)
            if sop_x >= screen_width - int(sop_rect[1]*0.8):
                    sop_x = screen_width - int(sop_rect[1]*0.8)
            if sop_y >= screen_height - int(sop_rect[1]*0.8):
                    sop_y = screen_height - int(sop_rect[1]*0.8)


            Score()
            Bullet_def()
            Grenade()
            Speed()
            star_def()
            star_die_def()
            jaeger_def()
            jaeger_die_def()
            dragoon_def()
            dragoon_die_def()
            Grenadeboom()
            Game_over()
            Pause()   
            pg.display.update()
            pg.time.delay(time_delay)
                    
# Shoot mode
def Shoot():
    global soprun, sopshoot, sopwait,bulletXY,sop_x,sop_y,dieXY,score,sop_rect,dx,dy
    
    gun_sound = pg.mixer.Sound(os.path.join(data_path,'gun_sound.wav'))
    

    while sopshoot:
        stop = False
        clock.tick(FPS)
        fps_count = 0
        gun_sound.play()
        gun_sound.set_volume(0.3)
        for i in sop_shoot_img:
            if stop:
                break
            Battle_back()
            ori = pg.image.load(os.path.join(sop_shoot_path,f'{i}'))
            i = pg.transform.scale(ori,(int(screen_height*0.3) , int(screen_height*0.3)))
           
            sop_rect = i.get_rect().size

            if len(bulletXY) != 0:
                for bx,by in bulletXY:
                    drawObject(bullet, bx, by)            
            
            screen.blit(i,(sop_x,sop_y))
                       
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sopshoot = False
                    soprun = False
                    sopwait = False
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        sopshoot = False
                        soprun = False  
                    
                    if event.key == pg.K_p:
                        pause = True
                    if event.key == pg.K_RIGHT:
                        dx = speed
                        right = True
                        rotate = False
                        soprun = True
                        sop_run_def()
                    if event.key == pg.K_LEFT:
                        dx = -speed
                        left = True
                        soprun = True
                        rotate = True
                        sop_run_def()
                    if event.key == pg.K_UP:
                        soprun = True
                        dy = -speed
                        up = True
                        sop_run_def()
                    if event.key == pg.K_DOWN:
                        soprun = True
                        dy = speed
                        down = True
                        sop_run_def()
                    if not sopshoot:
                        stop = True

                if event.type == pg.KEYUP:
                    if event.key == pg.K_s:
                        sopshoot = False
                        sopwait = True
                sop_x += dx
                sop_y += dy
            
            fps_count += 1
            if fps_count == 3:
                
                bulletX = sop_x + sop_rect[0]/2
                bulletY = sop_y + sop_rect[1]/1.855
                bulletXY.append([bulletX,bulletY])

            if fps_count == 15:
                
                bulletX = sop_x + sop_rect[0]/2
                bulletY = sop_y + sop_rect[1]/1.855
                bulletXY.append([bulletX,bulletY])

            if fps_count == 9:
                
                bulletX = sop_x + sop_rect[0]/2
                bulletY = sop_y + sop_rect[1]/1.855
                bulletXY.append([bulletX,bulletY])
            
            Score()
            Bullet_def()
            Grenade()
            Speed()
            star_def()
            star_die_def()
            jaeger_def()
            jaeger_die_def()
            dragoon_def()
            dragoon_die_def()
            Grenadeboom()
            Pause()
            Game_over()
            pg.display.update()           
            pg.time.delay(time_delay)

# skill mode
def Skill():
    global cooltime,e_speed,skill_done
    sop_skill = True
    count = 0
    while sop_skill:
        
        for skill_i in sop_skill_img:
            Battle_back()       
            sop_skill_ori = pg.image.load(os.path.join(sop_skill_path,f'{skill_i}'))
            sop_skill_rect = sop_skill_ori.get_rect().size
            sop_skill_i = pg.transform.scale(sop_skill_ori,(int(screen_height*0.3),int(screen_height*0.3)))
            sop_rect = sop_skill_i.get_rect().size
            screen.blit(sop_skill_i,(sop_x,sop_y))
            grenadeX = sop_x + sop_rect[0]*0.2
            grenadeY = sop_y + sop_rect[1]*0.49
            # print(count)
            if count == 44:
                grenadeXY.append([grenadeX,grenadeY])
                skill_done -= 1
                count = -300
            
            count += 1
            e_speed = 0
            Grenade()
            Grenadeboom()
            Score()
            star_def()
            star_die_def()
            jaeger_def()
            jaeger_die_def()
            dragoon_def()
            dragoon_die_def()
            Game_over() 
            pg.display.update()

            
            
              
        break
    
    count = 0
    e_speed = 3
    Speed()     

# mian loop
def main_loop():
    global background, sop_x, sop_y,sopwait,screen_width,screen_height, fourth,expo,battle,time_delay,screen
    
    main_font = pg.font.Font(os.path.join(font_path,'NanumGothic.ttf'),15)
    main_text = main_font.render(f'현재 창 크기 : {screen_width} // (M키 +100,N키 -100)',True,WHITE)
    main_delay_text = main_font.render(f'현재 게임 속도 : {time_delay} // 높을수록 느림 기본값 0 , 최대 15 추천 (K키 +5, J키 -5)',True,WHITE)
    main_2 = main_font.render('완료 : L키',True,WHITE)

    line_1 = main_font.render('시작 : S',True,BLACK)
    back_1 = pg.Surface(line_1.get_size())
    back_1.fill(WHITE)
    back_1.blit(line_1,(0,0))

    line_2 = main_font.render('설정 : L',True,BLACK)
    back_2 = pg.Surface(line_2.get_size())
    back_2.fill(WHITE)
    back_2.blit(line_2,(0,0)) 

    line_3 = main_font.render('도움 : H',True,BLACK)
    back_3 = pg.Surface(line_3.get_size())
    back_3.fill(WHITE)
    back_3.blit(line_3,(0,0))

    

    pg.mixer.music.load(os.path.join(data_path,'BGM.wav'))
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.6)
    main_run = True
    reset()
    
    while main_run:
        clock.tick(3) 
        reset()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                main_run = False
                pg.quit()   
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_e:
                    background = expo
                if event.key == pg.K_f:
                    background = fourth
                if event.key == pg.K_s:
                    sopwait = True
                    sop_wait()
                    sop_x = 0
                    sop_y = 100
                if event.key == pg.K_ESCAPE:
                    pg.quit()       
                if event.key == pg.K_h:
                    HELP = True
                    while HELP:
                        
                        screen.fill([0,0,0])
                        for event in pg.event.get():
                            
                            if event.type == pg.QUIT:
                                pg.quit()
                            if event.type == pg.KEYDOWN:
                                if event.key == pg.K_h:
                                    HELP = False
                        Help()
                        pg.display.update()
                
                if event.key == pg.K_l:
                    done = False
                    while not done:
                        screen.fill([0,0,0])
                        
                        for event in pg.event.get():
                            main_text = main_font.render(f'현재 창 크기 : {screen_width} // (M키 +100,N키 -100)',True,WHITE)
                            main_delay_text = main_font.render(f'현재 게임 속도 : {time_delay} // 높을수록 느림 기본값 0 , 최대 15 추천 (K키 +5, J키 -5)',True,WHITE)
                            if event.type == pg.QUIT:
                                pg.quit()
                            if event.type == pg.KEYDOWN:
                                if event.key == pg.K_m:
                                    screen_width += 100
                                if event.key == pg.K_n:
                                    if screen_width != 400:
                                        screen_width -= 100
                                if event.key == pg.K_k:
                                    time_delay += 5
                                if event.key == pg.K_j:
                                    if time_delay != 0:
                                        time_delay -= 5
                                    
                                if event.key == pg.K_l:
                                    done = True
                                if event.key == pg.K_ESCAPE:
                                    pg.quit()
                        screen_height = int(screen_width*0.45)
                        screen = pg.display.set_mode((screen_width,screen_height))
                        screen.blit(main_text,(20,20))
                        screen.blit(main_delay_text,(20,100))
                        screen.blit(main_2,(20,screen_height-40))
                        pg.display.update()
                        reset()


                    screen_height = int(screen_width*0.45)
                    background_img()
                    
                        
                    background = fourth
                    battle = bridge
                    pg.display.update()
                    Background()
                

            if event.type == pg.MOUSEBUTTONDOWN:
                background = random.choice(backgrounds) 
        

        Background()
        screen.blit(back_3,(screen_width-100,screen_height-40))
        screen.blit(back_2,(screen_width-100,screen_height-65))
        screen.blit(back_1,(screen_width-100,screen_height-90))
        pg.display.update()

    pg.quit()

main_loop()