import pygame_menu
import pygame
import db


class Menu:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 840))
        pygame.display.set_caption('Менюшка')
        self.menu = pygame_menu.Menu('Welcome', 600, 840,
                                     theme=pygame_menu.themes.THEME_BLUE)

        def get_login(text):
            self.login = text

        def get_password(text):
            self.password = text

        def get_rt_password(text):
            self.rt_password = text

        def get_email(text):
            self.email = text

        self.menu.add.text_input('Login: ', onchange=get_login)
        self.menu.add.text_input('Password: ', onchange=get_password)
        self.menu.add.text_input('Retry Password: ', onchange=get_rt_password)
        self.menu.add.text_input('Email: ', onchange=get_email)
        self.menu.add.button('Registration', self.registration)

    def registration(self):
        print('Регистрация.')
        print('Регистрация..')
        print('Регистрация...')
        print('Регистрация..')
        print('Регистрация.')
        bd = db.MySQL()
        if bd.add_user(self.login, self.password, self.rt_password, self.email):
            raise SystemExit(123)


if __name__ == '__main__':
    menu = Menu()
    menu.menu.mainloop(menu.screen)
