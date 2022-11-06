import pygame
from random import randint
from pygame.locals import*

troca_apple_pos = False
colidiu = False
pontuacao = 0

#   colocar Paredes (obstáculos para superar)
#   colocar níveis (velocidade e mais obstáculos)
#
def em_linha_randint():
    x = randint(10,580)
    y = randint(10,580)
    return (x//10 * 10, y//10 * 10)

def collision(objecto_1,objecto_2):
    return (objecto_1[0] == objecto_2[0] and (objecto_1[1] == objecto_2[1]))

def collision_wall(snake,apple_pos): #função interna para fazer a colisão com a parede
    global troca_apple_pos
    global colidiu

    for x in range(591):
        for y in range(591):
            if x == 0:
                if collision(snake[0],(x,y)):
                    if collision(snake[0],apple_pos):
                        apple_pos = em_linha_randint()
                        snake.append((x+10,y))
                        troca_apple_pos = True
                    snake[0] = (580,y)
            if y == 590:
                if collision(snake[0], (x, y)):
                    if collision(snake[0], (x, y)):
                        if collision(snake[0], (x, y)):
                            if collision(snake[0], apple_pos):
                                snake.append((x, y - 10))
                                troca_apple_pos = True
                    snake[0] = (x, y-590)
            if y == 0:
                if collision(snake[0],(x, y)):
                    if collision(snake[0], (x, y)):
                        if collision(snake[0], apple_pos):
                            snake.append((x, y+10))
                            troca_apple_pos = True
                    snake[0] = (x,580)
            if x == 590:
                if collision(snake[0], (x, y)):
                    if collision(snake[0],apple_pos):
                        apple_pos = em_linha_randint()
                        snake.append((x-10,y))
                        troca_apple_pos = True
                    snake[0] = (x - 590, y)
        i = 1
        """while i < len(snake):
            cabeca = snake[0]
            if i == 1:
                if collision(snake[0],snake[1]) and collision(snake[0],snake[i+1]):
                    aux = snake[len(snake)-1]
                    snake[len(snake)-1] = cabeca
                    snake[0] = aux"""
    return snake



pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')



UP  = 0
RIGHT = 1
DOWN = 2
LEFT = 3
# Criar a cobra
snake = [(200,200),(210,200),(220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((0,255,0))

# criar a maçã em_linha_randint()

apple_pos = em_linha_randint()
apple = pygame.Surface((10,10))
apple.fill((255,177,24))

# obstáculos
def obstaculo():
    global obst_pos
    obstaculo = pygame.Surface((100, 100))
    obstaculo.fill((250, 250, 200))
    return obstaculo

obst_pos = em_linha_randint()

my_direction = LEFT

#   variavel que controla o tempo para que o jogo não seja muito rápido
clock = pygame.time.Clock()
tempo = 15

while True:
    clock.tick(tempo)
    pygame.display.set_caption(f'Pontuação: {pontuacao}'.center(50))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if collision(snake[0],apple_pos):
        apple_pos = em_linha_randint()
        snake.append((0,0))
        pontuacao += 10
        tempo += 2.5

    for i in range(len(snake)-1,0,-1):
        snake[i] = (snake[i-1][0],snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    collision_wall(snake,apple_pos)
    if troca_apple_pos == True:
        apple_pos = em_linha_randint()


    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    
    #screen.blit(obstaculo(),obst_pos)

    for pos in snake:
        screen.blit(snake_skin, pos)

    if collision(snake[0],snake[len(snake)-1]):
        break

    troca_apple_pos = False
    pygame.display.update()