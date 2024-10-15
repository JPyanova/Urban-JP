class Vehicle:

    __COLOR_VARIANTS = ['black', 'red', 'blue', 'dark blue', 'maroon']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print (self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, wished_color):
        wished_color = str(wished_color)
        for color_variant in self.__COLOR_VARIANTS:
            if wished_color.lower == str(color_variant).lower:
                self.__color = wished_color
                break
            else:
                print(f'Нельзя сменить цвет на {wished_color}')
                break

class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info()
vehicle1.set_color('black')
vehicle1.print_info()
