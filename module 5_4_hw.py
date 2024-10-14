class House:
    houses_history = []


    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs.values())
        cls.houses_history.append(kwargs.get('name'))
        return object.__new__(cls)

    def __init__(self, number_of_floors, name):
        self.name = name
        self.number_of_floors = number_of_floors

    # def go_to(self, new_floor):
    #     floors_in_range = True
    #     for floors in range(1, (new_floor + 1)):
    #         if new_floor > self.number_of_floors or new_floor < 1:
    #             floors_in_range = False
    #             print('Такого этажа не существует')
    #             break
    #         else:
    #             print(floors)

    def __del__(self):
        print(f'{self.name} снесен, но останется в истории')

    # def __len__(self):
    #     return self.number_of_floors
    #
    # def __str__(self):
    #     return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    #
    # def __eq__(self, other):
    #     return self.number_of_floors == other.number_of_floors
    #
    # def __lt__(self, other):
    #     return self.number_of_floors <= other.number_of_floors
    #
    # def __gt__(self, other):
    #     return self.number_of_floors > other.number_of_floors
    #
    # def __ge__(self, other):
    #     return self.number_of_floors >= other.number_of_floors
    #
    # def __ne__(self, other):
    #     return self.number_of_floors != other.number_of_floors
    #
    # def __add__(self, value):
    #     self.number_of_floors = self.number_of_floors + value
    #     return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House(10, name ='ЖК Эльбрус') # name for kwargs
print(House.houses_history)
h2 = House(20, name = 'ЖК Акация')
print(House.houses_history)
h3 = House(20, name = 'ЖК Матрёшки')
print(House.houses_history)

del h2
del h3

print(House.houses_history)
print(House.houses_history[1])

# h1 = h1 + 10 # __add__
# print(h1)
# print(h1 == h2)
#
# h1 += 10 # __iadd__
# print(h1)
#
# h2 = 10 + h2 # __radd__
# print(h2)
#
# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__



