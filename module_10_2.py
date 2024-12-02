import threading
import time

class Knight(threading.Thread):

    def __init__(self, name, power, enemies = 100):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = enemies

    def enemies_counter(self, name, enemies, power):
        enemies = 100
        days = 0
        while enemies:
            time.sleep(1)
            days += 1
            enemies -= self.power
            print(f'{self.name} сражается {days} дней(дня), осталось {enemies} воинов.')
            if enemies <= 0:
                print(f'{self.name} одержал победу спустя {days} дней(дня')
                break


    def run(self):
        print(f'{self.name}, на нас напали!')
        self.enemies_counter(self.name, self.enemies, self.power)
        print(f'Все сражения закончены.')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

