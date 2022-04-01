import pygame
from const import *
from statemanager import StateMananger

def main():
    pygame.init() # Инициация PyGame, обязательная строчка 
    screen = pygame.display.set_mode(DISPLAY, pygame.RESIZABLE|pygame.SCALED|pygame.DOUBLEBUF|pygame.HWSURFACE) # Создаем окошко
    pygame.display.set_caption("pyKitty") # Пишем в шапку
                                         # будем использовать как фон
    #bg.fill(Color(BACKGROUND_COLOR))     # Заливаем поверхность сплошным цветом
    clock = pygame.time.Clock()
    stm = StateMananger(screen)
    stm.go_to('title', 'init')

    while True: # Основной цикл программы
        clock.tick(60)
        stm.cur_scene.handle_events(pygame.event.get())
        stm.cur_scene.update()
        stm.cur_scene.draw()

if __name__ == "__main__":
    main()
