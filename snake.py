import pygame
import random



pygame.init()

width = 800
height = 800
size = 40

snake_list = []
length_of_snake = 1

dis = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇游戏")
font = pygame.font.Font("font.ttf", 30)


min = 0
max_width = width - size
max_height = height - size


food_x = round(random.randrange(0, max_width)/ size) * size
food_y = round(random.randrange(0, max_height)/ size)* size

snake_x = width / 2
snake_y = height / 2

snake_change_x = 0

snake_change_y = 0


def score(score):
    value = font.render("得分: " + str(score), True, 'white')
    dis.blit(value, [100, 0])
def draw_food(color):
    pygame.draw.rect(dis, color, [food_x, food_y, size, size])
def draw_snake(color):
    for x in snake_list:
        pygame.draw.rect(dis, color, [x[0], x[1], size, size])



while True:
    dis.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_change_x = -size
                snake_change_y = 0
                print("left")

            elif event.key == pygame.K_RIGHT:
                snake_change_x = size
                snake_change_y = 0
                print("right")
                break
            elif event.key == pygame.K_UP:
                snake_change_x = 0
                snake_change_y = -size
                print("up")
                break
            elif event.key == pygame.K_DOWN:
                snake_change_x = 0
                snake_change_y = size
                print("done")
                break

    snake_x += snake_change_x
    snake_y += snake_change_y

    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)

    if len(snake_list)> length_of_snake:
        del snake_list[0]


    draw_food('red')
    draw_snake('green')
    score(length_of_snake - 1)


    pygame.display.update()

    if snake_y == food_y and snake_x == food_x:
        food_x = round(random.randrange(min, max_width)/ size)* size
        food_y = round(random.randrange(min, max_height)/ size)* size
        length_of_snake += 1

    pygame.time.Clock().tick(3)