import pygame
from gameobject import GameObject
from pygame import *
from map import GameMap

WIN_WIDTH = 800 #Ширина создаваемого окна
WIN_HEIGHT = 600 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"
TILE_WIDTH = 32
TILE_HEIGHT = 32

level = {
    'grounds' : [
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
        "rrrrrrrrrrrrrrrrrrrrrrrrr",
        "rrrrrrrrrrrrrrrrrrrrrrrrr",
        "rrrrrrrrrrrrrrrrrrrrrrrrr",
        "rrrrrrrrrrrrrrrrrrrrrrrrr",
        "sssssssssssssssssssssssss",
        "sssssssssssssssssssssssss",
        "ggggggggggggggggggggggggg",
        "ggggggggggggggggggggggggg",
        "ggggggggggggggggggggggggg"
    ],
    'objects' : [
        "-------------------------",
        "-------------------------",
        "-------------------------",
        "-------------------------",
        "-------------------------",
        "-------------------------",
        "-------------------------",
        "-------------------------",
        "-------------------------",
        "-------------------------",
        "-------------------------",
        "------------------------C",
        "------------------------C",
        "c------------------------",
        "c------------------------",
        "-------------------------",
        "-------------------------",
        "-------------------------",
        "-------------------------",
        "-------------------------"
    ],
}

def main():
    pygame.init() # Инициация PyGame, обязательная строчка 
    screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
    pygame.display.set_caption("pyKitty") # Пишем в шапку
    bg = Surface((WIN_WIDTH,WIN_HEIGHT)) # Создание видимой поверхности
                                         # будем использовать как фон
    #bg.fill(Color(BACKGROUND_COLOR))     # Заливаем поверхность сплошным цветом
    clock = pygame.time.Clock()
    

    player =  Surface((TILE_WIDTH,TILE_HEIGHT))
    player_x = int((WIN_WIDTH/TILE_WIDTH)/2)
    player_y = WIN_HEIGHT - TILE_HEIGHT
    player.fill(Color("#ebe4e4"))
    player_speed = 10

    lvl1 = GameMap(screen, level)
    lvl1.load_ground_map()
    lvl1.load_object_map()
    
    while 1: # Основной цикл программы
        clock.tick(60)
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
        lvl1.update()
        lvl1.draw()
        screen.blit(player,(player_x,player_y))
        #pygame.display.update()     # обновление и вывод всех изменений на экран
        pygame.display.flip()
    

if __name__ == "__main__":
    main()