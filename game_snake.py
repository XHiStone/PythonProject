import random

import pygame

pygame.init()
clock = pygame.time.Clock()

#颜色
WHITE = "white"
BLACK = "black"
RED = "red"
GREEN = "green"
BLUE = "blue"
YELLOW = "yellow"
GRAY = "gray"

#屏幕
DIS_WIDTH = 800
DIS_HEIGHT = 600
SIZE = 20
SNAKE_SPEED = 5

dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption("贪吃蛇游戏")
font = pygame.font.SysFont("stheitilight", 30)
snake_x = DIS_WIDTH/2
snake_y = DIS_HEIGHT/2
snake_change_x = 0
snake_change_y = 0
game_over = False
snake_List = []
Length_of_snake = 1


def score(score):
    value = font.render("得分: " + str(score), True, WHITE)
    dis.blit(value, [0, 0])
def message(msg, color):
    value = font.render(msg, True, color)
    position = value.get_rect(center=(DIS_WIDTH / 2, DIS_HEIGHT / 2))
    dis.blit(value, position)

# 绘制食物
def draw_food(color):
    pygame.draw.rect(dis, color, [foodX, foodY, SIZE, SIZE])
def draw_snake(color):
    for x in snake_List:
        pygame.draw.rect(dis, color, [x[0], x[1], SIZE, SIZE])


foodX = round(random.randrange(0, DIS_WIDTH - SIZE) / SIZE) * SIZE
foodY = round(random.randrange(0, DIS_HEIGHT - SIZE) / SIZE) * SIZE

while True:

    while game_over:
        dis.fill(BLACK)
        message("游戏结束!", RED)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    dis.fill(BLACK)
                    snake_x = DIS_WIDTH/2
                    snake_y = DIS_HEIGHT/2
                    snake_List = []
                    Length_of_snake = 1
                    snake_change_x =0
                    snake_change_y =0
                    game_over = False



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_change_x = -SIZE
                snake_change_y = 0
            elif event.key == pygame.K_RIGHT:
                snake_change_x = SIZE
                snake_change_y = 0
            elif event.key == pygame.K_UP:
                snake_change_x = 0
                snake_change_y = -SIZE
            elif event.key == pygame.K_DOWN:
                snake_change_x = 0
                snake_change_y = SIZE

    if snake_x >= DIS_WIDTH or snake_x < 0 or snake_y >= DIS_HEIGHT or snake_y < 0:
        game_over = True

    snake_x += snake_change_x
    snake_y += snake_change_y
    dis.fill(BLACK)

    draw_food(RED)

    snake_Head = []
    snake_Head.append(snake_x)
    snake_Head.append(snake_y)
    snake_List.append(snake_Head)

    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    draw_snake(GREEN)
    score(Length_of_snake - 1)
    pygame.display.update()


    if snake_x == foodX and snake_y == foodY:
        foodX = round(random.randrange(0, DIS_WIDTH - SIZE) / SIZE) *SIZE
        foodY = round(random.randrange(0, DIS_HEIGHT - SIZE) / SIZE) * SIZE
        Length_of_snake += 1

    clock.tick(SNAKE_SPEED)