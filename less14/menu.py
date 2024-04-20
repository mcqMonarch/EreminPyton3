import pygame_menu
import pygame


class Menu:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 840))
        pygame.display.set_caption('Менюшка')
        self.menu = pygame_menu.Menu('Welcome', 600, 840,
                                     theme=pygame_menu.themes.THEME_BLUE)
        self.menu.add.text_input('Login: ')
        self.menu.add.text_input('Password: ')
        self.menu.add.text_input('Retry Password: ')
        self.menu.add.text_input('Email: ')
        self.menu.add.button('Registration', self.registration)
    def registration(self):
        print('Успешно')


if __name__ == '__main__':
    menu = Menu()
    menu.menu.mainloop(menu.screen)
