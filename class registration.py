class Database:
    """
    База данных, содержащий словарь и метод добавления данных в словарь
    """
    def __init__(self):
        self.data = {}

    def __add_user__(self, username, password):
        self.data[username] = password

class User:
    """
    Класс пользователя, содержащий аттрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            character_in_password = True
            for character in password:
                upper = 0
                lower = 0
                number = 0

                if character.isupper():
                    upper += 1
                elif character.islower():
                    lower += 1
                elif character.isalpha():
                    number += 1
                    continue

                if upper <= 0 or lower <= 0 or number <= 0 or len(password) < 7:
                    print('Password is not strong enough!')
                    break
            self.password = password # если данное условие не выполнится, аттрибут password не создастся
            # AttributeError: 'User' object has no attribute 'password'
        else:
            pass
            # предотвращаем переход программы на строчку добавления пользователя database.__add_user__

if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input(f'''Greetings! Choose the action:
        1 - Sign in
        2 - Sign up
        '''))
        if choice == 1:
            login = input('Enter login: ')
            password = input('Enter password: ')

            if login in database.data:
                if password == database.data[login]:
                    print(f'You entered the system, {login}!')
                    break
                else:
                    print('Wrong password!')
            else:
                print('No user with this login!')

        if choice == 2:
            user = User(input('Enter login: '), password := input('Enter password: '),
                    password_confirm := input('Confirm password: '))
            # := моржовый оператор: позволяет одновременно вычислить выражение, присвоить результат переменной
            # и вернуть это значение.
            if password != password_confirm:
                print('Passwords do not match! Try one more time!')
                continue
            database.__add_user__(user.username, user.password) #добавляем в словарь имя пользователя и пароль
            print(database.data)


