from exceptions import AuthorizationError, RegistrationError, ValidationError
from authenticator import Authenticator

def main():
    user1 = Authenticator()
    if user1.login is None:
        print('Пройдите регистрацию ')
    else:
        print('Введите логин(почта) и пароль для авторизации')
    while True:
        login = input('Введите логин:')
        password = input('Введите пароль:')

        try:
            if user1.login is None:
                user1.registrate(login,password)
                print('Регистрация прошла успешно!')
                break
            else:
                user1.authorize(login,password)
                print('Авторизация прошла успешно!')
                break
        except AuthorizationError as e:
            print(e)

        except RegistrationError as e:
            print(e)

        except ValidationError as e:
            print(e)

main()
