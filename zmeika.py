import pygame
import random

SCREEN_WIDTH = 500 # Ширина экрана
SCREEN_HEIGHT = 500 # Высота экрана
BLOCK_SIZE = SCREEN_HEIGHT//25

ITEM_WIDTH = SCREEN_WIDTH // 40
ITEM_HEIGHT = SCREEN_HEIGHT // 40

BLACK = (0, 100, 100)
WHITE = (150, 150, 0)
RED = (255, 0, 0)

LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("S.N.A.K.E")


#ЕДА
items = []
for i in range(1):
    item_x = random.randint(ITEM_WIDTH, SCREEN_WIDTH - ITEM_WIDTH)
    item_y = random.randint(ITEM_HEIGHT, SCREEN_HEIGHT - ITEM_HEIGHT)
    items.append((item_x, item_y))

def draw_items(items):
    for item in items:
        pygame.draw.ellipse(screen, RED, [item[0], item[1], ITEM_WIDTH, ITEM_HEIGHT])



#ЗМЕЯ
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, BLACK, [block[0], block[1],BLOCK_SIZE, BLOCK_SIZE])

#КОЛЛИЗИЯ ЕДЫ
def check_collision(items,snake_x,snake_y):
    eat = 0
    for item in items:
        if snake_x < item[0] + ITEM_WIDTH and snake_x + BLOCK_SIZE > item[0] \
        and snake_y < item[1] + ITEM_HEIGHT and snake_y + BLOCK_SIZE > item[1]:
            items.remove(item)
        if len(items)==0:
            eat = 1
            item_x = random.randint(ITEM_WIDTH, SCREEN_WIDTH - ITEM_WIDTH)
            item_y = random.randint(ITEM_HEIGHT, SCREEN_HEIGHT - ITEM_HEIGHT)
            items.append((item_x, item_y))
    return eat

#КОЛЛИЗИЯ ЗМЕИ
def check_collisionSNAKE(snake_list,snake_head):
    head = snake_list[0]
    for i in snake_list:
        if i != head:
            if i[0] < head[0] + BLOCK_SIZE and i[0] + BLOCK_SIZE > head[0] and\
                    i[1] < head[1] + BLOCK_SIZE and i[1] + BLOCK_SIZE > head[1]:
                    print(f"xh{snake_list[0][0]} yh{snake_list[0][1]}")
                    pygame.quit()
                    exit()


def main_loop():
    snake_x = SCREEN_WIDTH // 2
    snake_y = SCREEN_HEIGHT // 2

    snake_list= [[snake_x,snake_y]]
    snake_len = 1
    snake_dir = LEFT


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_LEFT]:
                    snake_dir = LEFT
                if pressed[pygame.K_RIGHT]:
                    snake_dir = RIGHT
                if pressed[pygame.K_UP]:
                    snake_dir = UP
                if pressed[pygame.K_DOWN]:
                    snake_dir = DOWN
        if snake_dir == LEFT:
            if snake_x < 0:
                pygame.quit()
                exit()
            snake_x -= BLOCK_SIZE
        if snake_dir == RIGHT:
            if snake_x > 490:
                pygame.quit()
                exit()
            snake_x += BLOCK_SIZE
        if snake_dir == UP:
            if snake_y < 0:
                pygame.quit()
                exit()
            snake_y -= BLOCK_SIZE
        if snake_dir == DOWN:
            if snake_y > 490:
                pygame.quit()
                exit()
            snake_y += BLOCK_SIZE

        snake_head = [snake_x, snake_y]
        check_collisionSNAKE(snake_list, snake_head)
        snake_list.insert(0, snake_head)

        if len(snake_list) > snake_len:
            del snake_list[-1]

        screen.fill(WHITE)
        snake_len += check_collision(items,snake_x,snake_y)
        draw_snake(snake_list)
        draw_items(items)
        pygame.display.update()
        pygame.time.Clock().tick(10)

if __name__ == '__main__':
    main_loop()