class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floors_in_range = True
        for floors in range(1, (new_floor + 1)):
            if new_floor > self.number_of_floors or new_floor < 1:
                floors_in_range = False
                print('Такого этажа не существует')
                break
            else:
                print(floors)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)




