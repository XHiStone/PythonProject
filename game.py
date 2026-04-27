import pygame
import sys
import random

# 初始化 Pygame
pygame.init()

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
GRAY = (128, 128, 128)

# 屏幕设置
DIS_WIDTH = 600
DIS_HEIGHT = 400
BLOCK_SIZE = 20
SNAKE_SPEED = 5

dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('贪吃蛇游戏 - Pygame Demo')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont('stheitilight', 25)
score_font = pygame.font.SysFont('stheitilight', 35)


def your_score(score):
    value = score_font.render("得分: " + str(score), True, WHITE)
    dis.blit(value, [0, 0])


def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, GREEN, [x[0], x[1], block_size, block_size])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    # 居中显示
    text_rect = mesg.get_rect(center=(DIS_WIDTH / 2, DIS_HEIGHT / 2))
    dis.blit(mesg, text_rect)


def gameLoop():
    game_over = False
    game_close = False

    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, DIS_WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    foody = round(random.randrange(0, DIS_HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            dis.fill(BLACK)
            message("游戏结束! 按 Q-退出 或 C-重玩", RED)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(BLACK)

        # 绘制食物
        pygame.draw.rect(dis, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # 检查是否撞到自己
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(BLOCK_SIZE, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        # 吃到食物
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, DIS_WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            foody = round(random.randrange(0, DIS_HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()


if __name__ == "__main__":
    gameLoop()
