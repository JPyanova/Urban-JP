class Animal:

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = True

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
            print(f'{self.name} насытился')
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
            print(f'{self.name} пошел охотиться')

class Mammal(Animal):
    pass

class Predator(Animal):
    pass


class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

predator = Predator('Волк')
mammal = Mammal('Капибара')
flower = Flower('Ромашка')
fruit = Fruit('Апельсин')

print(predator.name)
print(flower.name)

print(predator.alive)
print(mammal.fed)
predator.eat(flower)
mammal.eat(fruit)
print(predator.alive)
print(mammal.fed)