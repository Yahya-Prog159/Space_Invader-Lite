import random
import pygame
import sys



pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((750, 500))


over_sound = pygame.mixer.Sound('Assets/over.wav')
laser_sound = pygame.mixer.Sound('Assets/laser_shot.wav')


# A Variable to hold the score
Score = 0

# Font Styling
font = pygame.font.Font('Assets/Pixeltype.ttf', 50)
font_style = pygame.font.Font('Assets/Pixeltype.ttf', 50)
text = font_style.render('Game Over', False, 'red')


# Spaceship
space_ship = pygame.image.load('Assets/spaceship_e.png')
space_ship = pygame.transform.scale(space_ship, (125, 125))
space_ship_X = 475
space_ship_Y = 350


# Background
background = pygame.image.load('Assets/background.jpg')
background = pygame.transform.scale(background, (850, 500))


# Enemies
enemy = pygame.image.load('Assets/enemy.png')
enemy = pygame.transform.scale(enemy, (35, 35))
enemy_Y = 25
enemy_X = random.randint(20, 730)

# enemy_2 = pygame.image.load('Assets/e_orange.png')
# enemy_2 = pygame.transform.scale(enemy_2, (100, 100))
# enemy_2_Y = 25
# enemy_2_X = random.randint(100, 730)



# Bullets
bullet = pygame.image.load('Assets/bullet.png')
bullet = pygame.transform.scale(bullet, (15, 17))
enemy_bullet = pygame.image.load('Assets/bullet.png')
enemy_bullet = pygame.transform.scale(bullet, (17, 19))
bullet_X = space_ship_X
# bx = enemy_2_X
# by = 0
bullet_Y = 350
bullet_fired = False

# enemy_2_B = pygame.image.load('Assets/bullet.png')
# enemy_2_B = pygame.transform.scale(bullet, (15, 17))
# enemy_2_B_X = enemy_2_X
# enemy_2_B_Y = enemy_2_Y
# damage = 3
# dead = False
# bf = False



# Create rectangles for the spaceship and enemy and the bullet
space_ship_rect = pygame.Rect(500, 370, 75, 75)
enemy_rect = pygame.Rect(enemy_X, enemy_Y, 30, 30)
# enemy_2_rect = pygame.Rect(enemy_2_X, enemy_2_Y, 90, 90)
bullet_rect = pygame.Rect(bullet_X, bullet_Y, 15, 17)




# Main game loop
while True:
    # Enemy's movement
    if enemy_Y <= 475:
        enemy_Y += 1

    # if enemy_2_Y <= 475:
    #     enemy_2_Y += .4
    # Check if the enemy touches the ground >> Game over
    if enemy_Y == 475:
        print('Game over')
        over_sound.play()
        screen.blit(text, (300, 200))
        pygame.display.update()
        pygame.time.delay(1000)
        sys.exit()

    # if enemy_2_Y == 475:
    #     print('Game over')
    #     over_sound.play()
    #     screen.blit(text, (300, 200))
    #     pygame.display.update()
    #     pygame.time.delay(1000)
    #     sys.exit()

    


    # Main Events: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Check if the keyboard is pressed
        if event.type == pygame.KEYDOWN:
            # Check if the Right key is pressed
            if event.key == pygame.K_RIGHT:
                space_ship_X += 25
                space_ship_rect.right  += 25
            # Check if the Left key is pressed
            elif event.key == pygame.K_LEFT:
                space_ship_X -= 25
                space_ship_rect.left  -= 25
            # Check if the space key is pressed
            elif event.key == pygame.K_SPACE:
                # Check if the bullet_fired = False, then bullet_fired will be true 
                if not bullet_fired:
                    bullet_X = space_ship_X + 55
                    bullet_Y = 350
                    bullet_fired = True

    # if not bf:
    #     bx = enemy_2_B_X + 55
    #     by = 350
    #     bf = True        

    # reposition the objects rectangles
    # space_ship_rect.x = space_ship_X 

    enemy_rect.y = enemy_Y
    # enemy_2_rect.y = enemy_2_Y
    bullet_rect.x = bullet_X
    bullet_rect.y = bullet_Y

    # Check if bullet_fire
    if bullet_fired:
        laser_sound.play()
        bullet_Y -= 10  
        # Check if bullet_Y < 0, Stop the bullet's movement
        if bullet_Y < 0:
            bullet_fired = False

        # if by < 350:
        #     bf = False

        # Check if the bullet collides with enemy
        if bullet_rect.colliderect(enemy_rect):
            Score += 1
            print("Collision!")
            bullet_fired = False
            enemy_Y = 25
            enemy_X = random.randint(35, 730)
            enemy_rect.x = enemy_X
            enemy_rect.y = enemy_Y

        # if bullet_rect.colliderect(enemy_2_rect):
        #     Score += 2
        #     print("hit!")
        #     bullet_fired = False
        #     enemy_2_Y = 25
        #     enemy_2_X = random.randint(35, 730)
        #     enemy_2_rect.x = enemy_2_X
        #     enemy_2_rect.y = enemy_2_Y


    # check if the spaceship collides with enemy
    if space_ship_rect.colliderect(enemy_rect):
        print('Game Over')
        over_sound.play()
        screen.blit(text, (300, 200))
        pygame.display.update()
        pygame.time.delay(1000)
        sys.exit()

    # if space_ship_rect.colliderect(enemy_2_rect):
    #     print('Game Over')
    #     over_sound.play()
    #     screen.blit(text, (300, 200))
    #     pygame.display.update()
    #     pygame.time.delay(1000)
    #     sys.exit()

    txt = font.render(f'Score: {Score}', False, 'green')

    # Puts all of the objects on the screen
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(space_ship, (space_ship_X, space_ship_Y))
    pygame.draw.rect(screen, (255, 0, 0), space_ship_rect, 2)
    # pygame.draw.rect(screen, (255, 0, 0), enemy_2_rect, 2)
    # pygame.draw.rect(screen, (255, 0, 0), enemy_rect, 2)
    screen.blit(enemy, (enemy_X, enemy_Y))
    screen.blit(txt, (10, 10))
    # screen.blit(enemy_2, (enemy_2_X, enemy_2_Y))

    # Checks if the bullet is fired
    if bullet_fired:
        screen.blit(bullet, (bullet_X, bullet_Y))

    # if bf:
    #     screen.blit(bullet, (bullet_X, bullet_Y))

    # Updates the display
    pygame.display.update()
    
    # Fixed FPS(60) 
    clock.tick(60)