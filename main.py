import pygame
from gameobject import GameObject
from pygame import *

WIN_WIDTH = 800 #Ширина создаваемого окна
WIN_HEIGHT = 600 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"
TILE_WIDTH = 32
TILE_HEIGHT = 32


level = [
       "ggggggggggggggggggggggggg",
       "bbbbbbbbbbbbbbbbbbbbbbbbb",
       "GGGGGGGGGGGGGGGGGGGGGGGGG",
       "gggggggssssssssgggggggggg",
       "gggggggssssssssgggggggggg",
       "gggggggssssssssgggggggggg",
       "ggggggggggggggggggggggggg",
       "ggggggggggggggggggggggggg",
       "rrrrrrrrrrrrrrrrrrrrrrrrr",
       "sssssssssssssssssssssssss",
       "sssssssssssssssssssssssss",
       "rrrrrrrrrrrrrrrrrrrrrrrrc",
       "rrrrrrrrrrrrrrrrrrrrrrrrc",
       "crrrrrrrrrrrrrrrrrrrrrrrr",
       "crrrrrrrrrrrrrrrrrrrrrrrr",
       "sssssssssssssssssssssssss",
       "sssssssssssssssssssssssss",
       "ggggggggggggggggggggggggg",
       "ggggggggggggggggggggggggg",
       "ggggggggggggggggggggggggg"]


def create_map(grass_gp, ground_gp, sand_gp, athphalt_gp, border_gp, level):
    x=y=0 # координаты
    for row in level: # вся строка
        for col in row: # каждый символ
            # grass
            if col == "g":
                #создаем блок, заливаем его цветом и рисеум его
                pf = GameObject(grass_gp, 0, 0, x, y, TILE_WIDTH, TILE_HEIGHT)
                pf.set_color("#39c936")
                grass_gp.add(pf) 
            # sand
            if col == "s":
                #создаем блок, заливаем его цветом и рисеум его
                pf = GameObject(sand_gp, 0, 0, x, y, TILE_WIDTH, TILE_HEIGHT)
                pf.set_color("#e2f511")
                sand_gp.add(pf) 
            # asphalt
            if col == "a":
                #создаем блок, заливаем его цветом и рисеум его
                pf = GameObject(athphalt_gp, 0, 0, x, y, TILE_WIDTH, TILE_HEIGHT)
                pf.set_color("#575352")
                athphalt_gp.add(pf) 
            # ground
            if col == "G":
                #создаем блок, заливаем его цветом и рисеум его
                pf = GameObject(ground_gp, 0, 0, x, y, TILE_WIDTH, TILE_HEIGHT)
                pf.set_color("#26100a")
                ground_gp.add(pf) 
            # border
            if col == "b":
                #создаем блок, заливаем его цветом и рисеум его
                pf = GameObject(border_gp, 0, 0, x, y, TILE_WIDTH, TILE_HEIGHT)
                pf.set_color("#290505")
                border_gp.add(pf)

            x += TILE_WIDTH #блоки платформы ставятся на ширине блоков
        y += TILE_HEIGHT    #то же самое и с высотой
        x = 0                   #на каждой новой строчке начинаем с нуля

def draw_map(screen, grass_gp, ground_gp, sand_gp, athphalt_gp, border_gp):
   grass_gp.draw(screen)
   ground_gp.draw(screen)
   sand_gp.draw(screen)
   athphalt_gp.draw(screen)
   border_gp.draw(screen)

def main():
    pygame.init() # Инициация PyGame, обязательная строчка 
    screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
    pygame.display.set_caption("pyKitty") # Пишем в шапку
    bg = Surface((WIN_WIDTH,WIN_HEIGHT)) # Создание видимой поверхности
                                         # будем использовать как фон
    #bg.fill(Color(BACKGROUND_COLOR))     # Заливаем поверхность сплошным цветом
    timer = pygame.time.Clock()
    

    player =  Surface((TILE_WIDTH,TILE_HEIGHT))
    player_x = int((WIN_WIDTH/TILE_WIDTH)/2)
    player_y = WIN_HEIGHT - TILE_HEIGHT
    player.fill(Color("#ebe4e4"))
    player_speed = 10

    # Группы для спрайтов
    sg_grass = pygame.sprite.Group()
    sg_sand = pygame.sprite.Group()
    sg_athphalt = pygame.sprite.Group()
    sg_ground = pygame.sprite.Group()
    sg_border = pygame.sprite.Group()

    create_map(sg_grass, sg_ground, sg_sand, sg_athphalt, sg_border, level)

    while 1: # Основной цикл программы
        for e in pygame.event.get(): # Обрабатываем события
            if e.type == QUIT:
                raise(SystemExit, "QUIT")
            if e.type == KEYDOWN and e.key == K_UP:
                player_y = player_y - player_speed
            if e.type == KEYDOWN and e.key == K_DOWN:
                player_y = player_y + player_speed
            if e.type == KEYDOWN and e.key == K_LEFT:
                player_x = player_x - player_speed
            if e.type == KEYDOWN and e.key == K_RIGHT:
                player_x = player_x + player_speed

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
        screen.blit(bg, (0,0))      # Каждую итерацию необходимо всё перерисовывать 
        draw_map(screen, sg_grass, sg_ground, sg_sand, sg_athphalt, sg_border)
        screen.blit(player,(player_x,player_y))
        #pygame.display.update()     # обновление и вывод всех изменений на экран
        pygame.display.flip()
    

if __name__ == "__main__":
    main()