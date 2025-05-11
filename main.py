import pygame as pygame
from sys import exit
from random import randint


def displayScore():
    currentTime = int(pygame.time.get_ticks()/1000) - startTime
    scoreSurface = scoreFont.render(f'Score: {currentTime}',False,(64,64,64))
    scoreRect = scoreSurface.get_rect(center=(850,50))
    screen.blit(scoreSurface,scoreRect)
    return currentTime

def obstacleMovement(obstacleList):
    if obstacleList:
        for obstacleRect in obstacleList:
            obstacleRect.x -= 5

            if obstacleRect.bottom == 565:
                screen.blit(enemySurface,obstacleRect)
            elif obstacleRect.bottom == 563:
                screen.blit(flySurface,obstacleRect)
            else:
                screen.blit(ghostSurface,obstacleRect)

        obstacleList = [obstacle for obstacle in obstacleList if obstacle.x > -100]
        return obstacleList
    else:
        return []
    
def collisions(player,obstacles, buffer=60):
    if obstacles:
        playerRectBuffered = playerRect.inflate(-buffer, -buffer)
        for obstacleRect in obstacles:
            obstacleRectBuffered = obstacleRect.inflate(-buffer, -buffer)
            if playerRectBuffered.colliderect(obstacleRectBuffered):
                return False
    return True

def standAnimation():
    global standIndex,playerStandSurface
    standIndex += 0.1
    if standIndex >= len(playerStand): standIndex = 0
    playerStandSurface = playerStand[int(standIndex)]

def playerAnimation():
    global jumpIndex,playerJumpSurface,runIndex,playerRunSurface
    if playerRect.bottom < 565:
        jumpIndex += 0.1
        if jumpIndex >= len(playerJump): jumpIndex = 0
        playerJumpSurface = playerJump[int(jumpIndex)]
    else:
        runIndex += 0.18
        if runIndex >= len(playerRun): runIndex = 0
        playerRunSurface = playerRun[int(runIndex)]


pygame.init()
pygame.mixer.init()
menu_music = pygame.mixer.Sound("assets/audio/menu_music.ogg")
game_music = pygame.mixer.Sound("assets/audio/game_loop.ogg")
death_sound = pygame.mixer.Sound("assets/audio/death_sound.ogg")

screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("Samurai Run by thisaru")
clock = pygame.time.Clock()
nameFont = pygame.font.Font("assets/fonts/alagard.ttf", 85)
scoreFont = pygame.font.Font("assets/fonts/bitmap.ttf", 50)
deadFont = pygame.font.Font("assets/fonts/bitmap.ttf", 90)
gameActive = False
startTime = 0
score = 0
death_sound_played = False
menu_music_playing = False
game_music_playing = False

startSurface = pygame.image.load("assets/images/start.jpg").convert_alpha()
deadSurface = pygame.image.load("assets/images/cemetery.jpg").convert_alpha()

skySurface = pygame.image.load("assets/images/sky1.jpeg").convert()
groundSurface = pygame.image.load("assets/images/background.jpg").convert()
nameSurface = nameFont.render("Samurai Run", False, (255, 215, 0))
nameRect = nameSurface.get_rect(center=(500,75))


creatorSurface = scoreFont.render("by Thisaru", False, (47, 47, 47))
creatorSurface = pygame.transform.scale(creatorSurface,(140,43))
creatorRect = creatorSurface.get_rect(center=(685,127))

ghost1 = pygame.image.load("assets/images/round_ghost/sprite_0.png").convert_alpha()
ghost1 = pygame.transform.scale(ghost1,(80,50))
ghost2 = pygame.image.load("assets/images/round_ghost/sprite_1.png").convert_alpha()
ghost2 = pygame.transform.scale(ghost2,(80,50))
ghost3 = pygame.image.load("assets/images/round_ghost/sprite_2.png").convert_alpha()
ghost3 = pygame.transform.scale(ghost3,(80,50))
ghost4 = pygame.image.load("assets/images/round_ghost/sprite_3.png").convert_alpha()
ghost4 = pygame.transform.scale(ghost4,(80,50))
ghost5 = pygame.image.load("assets/images/round_ghost/sprite_4.png").convert_alpha()
ghost5 = pygame.transform.scale(ghost5,(80,50))
ghost6 = pygame.image.load("assets/images/round_ghost/sprite_5.png").convert_alpha()
ghost6 = pygame.transform.scale(ghost6,(80,50))
ghostFrame = 0
ghostFrames =[ghost1,ghost2,ghost3,ghost4,ghost5,ghost6]
ghostSurface = ghostFrames[ghostFrame]


fly1 = pygame.image.load("assets/images/sprite/02.png").convert_alpha()
fly1 = pygame.transform.flip(fly1, True, False)
fly2 = pygame.image.load("assets/images/sprite/03.png").convert_alpha()
fly2 = pygame.transform.flip(fly2, True, False)
fly3 = pygame.image.load("assets/images/sprite/04.png").convert_alpha()
fly3 = pygame.transform.flip(fly3, True, False)
fly4 = pygame.image.load("assets/images/sprite/05.png").convert_alpha()
fly4 = pygame.transform.flip(fly4, True, False)
fly5 = pygame.image.load("assets/images/sprite/06.png").convert_alpha()
fly5 = pygame.transform.flip(fly5, True, False)
fly6 = pygame.image.load("assets/images/sprite/07.png").convert_alpha()
fly6 = pygame.transform.flip(fly6, True, False)
fly7 = pygame.image.load("assets/images/sprite/08.png").convert_alpha()
fly7 = pygame.transform.flip(fly7, True, False)
fly8 = pygame.image.load("assets/images/sprite/09.png").convert_alpha()
fly8 = pygame.transform.flip(fly8, True, False)
fly9 = pygame.image.load("assets/images/sprite/10.png").convert_alpha()
fly9 = pygame.transform.flip(fly9, True, False)
flyFrame = 0
flyFrames = [fly1,fly2,fly3,fly4,fly5,fly6,fly7,fly8,fly9]
flySurface = flyFrames[flyFrame]

enemy1 = pygame.image.load("assets/images/Pirate/run_0.png").convert_alpha()
enemy1 = pygame.transform.scale(enemy1,(100,100))
enemy1 = pygame.transform.flip(enemy1, True, False)
enemy2 = pygame.image.load("assets/images/Pirate/run_1.png").convert_alpha()
enemy2 = pygame.transform.scale(enemy2,(100,100))
enemy2 = pygame.transform.flip(enemy2, True, False)
enemy3 = pygame.image.load("assets/images/Pirate/run_2.png").convert_alpha()
enemy3 = pygame.transform.scale(enemy3,(100,100))
enemy3 = pygame.transform.flip(enemy3, True, False)
enemy4 = pygame.image.load("assets/images/Pirate/run_3.png").convert_alpha()
enemy4 = pygame.transform.scale(enemy4,(100,100))
enemy4 = pygame.transform.flip(enemy4, True, False)
enemy5 = pygame.image.load("assets/images/Pirate/run_4.png").convert_alpha()
enemy5 = pygame.transform.scale(enemy5,(100,100))
enemy5 = pygame.transform.flip(enemy5, True, False)
enemy6 = pygame.image.load("assets/images/Pirate/run_5.png").convert_alpha()
enemy6 = pygame.transform.scale(enemy6,(100,100))
enemy6 = pygame.transform.flip(enemy6, True, False)
enemyFrame = 0
enemyFrames = [enemy1,enemy2,enemy3,enemy4,enemy5,enemy6]
enemySurface = enemyFrames[enemyFrame]


obstacleRectList = []


run1 = pygame.image.load("assets/images/Samurai/run_0.png").convert_alpha()
run1 = pygame.transform.scale(run1,(100,100))
run2 = pygame.image.load("assets/images/Samurai/run_1.png").convert_alpha()
run2 = pygame.transform.scale(run2,(100,100))
run3 = pygame.image.load("assets/images/Samurai/run_2.png").convert_alpha()
run3 = pygame.transform.scale(run3,(100,100))
run4 = pygame.image.load("assets/images/Samurai/run_3.png").convert_alpha()
run4 = pygame.transform.scale(run4,(100,100))
run5 = pygame.image.load("assets/images/Samurai/run_4.png").convert_alpha()
run5 = pygame.transform.scale(run5,(100,100))
run6 = pygame.image.load("assets/images/Samurai/run_5.png").convert_alpha()
run6 = pygame.transform.scale(run6,(100,100))
runIndex = 0
playerRun = [run1,run2,run3,run4,run5,run6]
playerRunSurface = playerRun[runIndex]
playerRect = playerRunSurface.get_rect(midbottom=(200,565))
playerGravity = 0

jump1 = pygame.image.load("assets/images/Samurai/idle_0.png").convert_alpha()
jump1 = pygame.transform.scale(jump1,(100,100))
jump2 = pygame.image.load("assets/images/Samurai/idle_0.png").convert_alpha()
jump2 = pygame.transform.scale(jump2,(100,100))
jump3 = pygame.image.load("assets/images/Samurai/idle_0.png").convert_alpha()
jump3 = pygame.transform.scale(jump3,(100,100))
jump4 = pygame.image.load("assets/images/Samurai/idle_0.png").convert_alpha()
jump4 = pygame.transform.scale(jump4,(100,100))
jumpIndex = 0
playerJump = [jump1,jump2,jump3,jump4]
playerJumpSurface = playerJump[jumpIndex]
playerRect = playerJumpSurface.get_rect(midbottom=(200,565))


playerStand1 = pygame.image.load("assets/images/Samurai/idle_0.png").convert_alpha()
playerStand1 = pygame.transform.scale(playerStand1,(350,350))
playerStand2 = pygame.image.load("assets/images/Samurai/idle_1.png").convert_alpha()
playerStand2 = pygame.transform.scale(playerStand2,(350,350))
playerStand3 = pygame.image.load("assets/images/Samurai/idle_2.png").convert_alpha()
playerStand3 = pygame.transform.scale(playerStand3,(350,350))
playerStand4 = pygame.image.load("assets/images/Samurai/idle_3.png").convert_alpha()
playerStand4 = pygame.transform.scale(playerStand4,(350,350))
standIndex = 0
playerStand = [playerStand1,playerStand3,playerStand3,playerStand4]
playerStandSurface = playerStand[standIndex]
playerStandRect = playerStandSurface.get_rect(center=(540,390))

playerDeadSurface = pygame.image.load("assets/images/Samurai/x_1.png").convert_alpha()
playerDeadSurface = pygame.transform.scale(playerDeadSurface,(360,360))
playerDeadRect = playerDeadSurface.get_rect(center=(540,370))

gameMessage = scoreFont.render("Press SPACE to start",False,(0,0,0))
gameMessageRect = gameMessage.get_rect(center=(500,570))

deadMessage = deadFont.render("YOU DIED!!",False,(178, 34, 34))
deadMessageRect = deadMessage.get_rect(center=(500,90))


obstacleTimer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacleTimer,1200)

enemyAnimationTimer = pygame.USEREVENT + 2
pygame.time.set_timer(enemyAnimationTimer,90)

flyAnimationTimer = pygame.USEREVENT + 3
pygame.time.set_timer(flyAnimationTimer,90)

ghostAnimationTimer = pygame.USEREVENT + 4
pygame.time.set_timer(ghostAnimationTimer,230)


while True:
    pygame.display.update()
    clock.tick(60)

    if gameActive:
        screen.blit(skySurface,(0,-50))
        screen.blit(groundSurface,(0,550))
        score = displayScore()
        menu_music.stop()
        death_sound.stop()

        if not game_music_playing:
            game_music.play(loops=-1)
            game_music_playing = True


        playerGravity += 1
        playerRect.y += playerGravity
        if playerRect.bottom >= 565:
            playerRect.bottom = 565
        screen.blit(playerRunSurface,playerRect)
        playerAnimation()

        gameActive = collisions(playerRect,obstacleRectList, buffer=60)

        obstacleRectList = obstacleMovement(obstacleRectList)

    else:
        screen.fill((100,100,100))
        scoreMessage = scoreFont.render(f'Your score: {score}',False,(0,0,0))
        scoreMessageRect = scoreMessage.get_rect(center = (500,570))
        obstacleRectList.clear()
        playerRect.midbottom = (200,565)
        playerGravity = 0

        if score == 0:
            if not menu_music_playing:
                menu_music.play(loops=1)
                menu_music_playing = True
            screen.blit(startSurface,(0,-80))
            standAnimation()
            screen.blit(playerStandSurface,playerStandRect)
            pygame.draw.rect(screen,(139, 69, 19),nameRect)
            pygame.draw.rect(screen,(139, 69, 19),nameRect,1000)
            screen.blit(nameSurface,nameRect)
            screen.blit(creatorSurface,creatorRect)
            screen.blit(gameMessage,gameMessageRect)
            
        else:
            menu_music.stop()
            game_music.stop()
            game_music_playing = False
            menu_music_playing = False
            if not death_sound_played:
                death_sound.play()
                death_sound_played = True
            screen.blit(deadSurface,(-150,0))
            screen.blit(playerDeadSurface,playerDeadRect)
            screen.blit(scoreMessage,scoreMessageRect)
            screen.blit(deadMessage,deadMessageRect)
            


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            menu_music.stop()
            death_sound.stop()
            game_music.stop()
            pygame.quit()
            exit()
            

        if gameActive:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if playerRect.bottom > 350 :
                        playerGravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameActive = True
                startTime = int(pygame.time.get_ticks()/1000)
                death_sound_played = False
                menu_music_playing = False
                game_music.stop()
                menu_music.stop()
                death_sound.stop()
 
        if gameActive:
            menu_music.stop()
            death_sound.stop()
            if not game_music_playing:
                game_music.play(loops=-1)
                game_music_playing = True
            if event.type == obstacleTimer:
                if randint(0,2):
                    if randint(0,2):
                        obstacleRectList.append(enemySurface.get_rect(midbottom=(randint(1000,1300),565)))
                    else:
                        obstacleRectList.append(flySurface.get_rect(midbottom=(randint(1000,1300),563)))
                else:
                    obstacleRectList.append(ghostSurface.get_rect(midbottom=(randint(1000,1300),randint(150,365))))

            if event.type == enemyAnimationTimer:
                enemyFrame = (enemyFrame + 1) % len(enemyFrames)
                enemySurface = enemyFrames[enemyFrame]

            if event.type == flyAnimationTimer:
                flyFrame = (flyFrame + 1) % len(flyFrames)
                flySurface = flyFrames[flyFrame]

            if event.type == ghostAnimationTimer:
                ghostFrame = (ghostFrame + 1) % len(ghostFrames)
                ghostSurface = ghostFrames[ghostFrame]
