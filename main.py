import pygame
from gameobject import GameObject
from player import Player
from pygame import *
from map import GameMap
from hud import Hud

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

    pl = Player(Color("#ebe4e4"), 3, int((WIN_WIDTH/2) - (TILE_WIDTH/2)), WIN_HEIGHT - TILE_HEIGHT)
    pl_grp = pygame.sprite.Group()
    pl_grp.add(pl)
    hud = Hud(screen, pl)

    lvl1 = GameMap(screen, level)
    lvl1.load_ground_map()
    lvl1.load_object_map()
    
    while 1: # Основной цикл программы
        clock.tick(60)
        for e in pygame.event.get(): # Обрабатываем события
            if e.type == QUIT:
                raise(SystemExit, "QUIT")
            elif e.type == pygame.KEYDOWN:
                if e.key == K_DOWN:
                    pl.set_move_down()
                if e.key == K_LEFT:
                    pl.set_move_left()
                if e.key == K_RIGHT:
                    pl.set_move_right()
                if e.key == K_UP:
                    pl.set_move_up()

            elif e.type == pygame.KEYUP:
                if e.key == K_DOWN:
                    pl.unset_move_down()
                if  e.key == K_LEFT:
                    pl.unset_move_left()
                if  e.key == K_RIGHT:
                    pl.unset_move_right()
                if e.key == K_UP:
                    pl.unset_move_up()

        screen.blit(bg, (0,0))      # Каждую итерацию необходимо всё перерисовывать 
        lvl1.update()
        lvl1.draw()
        hits = pygame.sprite.groupcollide(sp_asteroids, self.sp_bullets, False, True)
        pl.update()
        pl_grp.draw(screen)
        hud.draw()
        #screen.blit(pl.image,(pl.rect.left,pl.rect.top))
        pygame.display.update()     # обновление и вывод всех изменений на экран
        pygame.display.flip()
    

if __name__ == "__main__":
    main()
