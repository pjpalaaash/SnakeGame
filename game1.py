import pygame
import random

pygame.init()
pygame.mixer.init()

white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
unknwn = (100,100,100)

gWindow = pygame.display.set_mode((700, 500))


pygame.display.set_caption("My GAME")


pygame.display.update()

Clock = pygame.time.Clock()


font = pygame.font.SysFont(None, 30)


def scoring(text, color, x, y):
    screen_text = font.render(text, True, color)
    gWindow.blit(screen_text, [x, y])


def plot_snake(gWindow, color, snake_list, s_size):
    for x, y in snake_list:
        pygame.draw.rect(gWindow, color, [x, y, s_size, s_size])



def Welcome():
    exit_game = False
    while not exit_game:
        gWindow.fill(black)
        scoring("Snakes Game bOOiii!!",red,215,200)
        scoring("PRESS SPACE TO PLAYY!!",green,200,230)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("bg.mp3")
                    pygame.mixer.music.play()
                    Gameloop()    
        pygame.display.update()
        Clock.tick(60)


def Gameloop():
    exit_game = False
    game_over = False
    X = 0
    Y = 0
    score = 0
    foodX = random.randint(25, 650)
    foodY = random.randint(25, 450)
    f_size = 10
    s_size = 12
    fps = 60
    velocity_x = 4
    velocity_y = 4
    snake_list = []
    snake_length = 1
    while not exit_game:
        

        if game_over:
            gWindow.fill(white)
            scoring("GAME OVER Bc Press Enter to Continue !!", red, 95, 250)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Welcome()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 4
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:

                        velocity_x = -4
                        velocity_y = 0
                    if event.key == pygame.K_UP:

                        velocity_y = -4
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = 4
                        velocity_x = 0

            X += velocity_x
            Y += velocity_y
            if abs(X - foodX) < 6 and abs(Y - foodY) < 6:
                score += 1
                foodX = random.randint(25, 650)
                foodY = random.randint(25, 450)
                snake_length += 5
            gWindow.fill(unknwn)
            scoring("Score is: " + str(score * 10), black, 5, 5)
            pygame.draw.rect(gWindow, red, [foodX, foodY, f_size, f_size])
            head = []
            head.append(X)
            head.append(Y)
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over = True
            if X < 0 or X > 700 or Y < 0 or Y > 500:
                game_over = True

            plot_snake(gWindow, green, snake_list, s_size)
        pygame.display.update()
        Clock.tick(fps)
    pygame.quit()
    quit()


Welcome()
