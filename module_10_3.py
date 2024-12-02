import threading
import random
import time

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            random_deposit = random.randint(50, 500)
            self.balance += random_deposit
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            else:
                print(f'"Пополнение: {random_deposit}. Баланс: {self.balance}".')
            time.sleep(0.001)

    def take(self):
        random_deposit = random.randint(50, 500)
        print(f'Запрос на {random_deposit}')
        for i in range(100):
            if random_deposit <= self.balance:
                self.balance -= random_deposit
                print(f'"Снятие: {random_deposit}. Баланс: {self.balance}".')
            if random_deposit > self.balance:
                print(f'Запрос отклонен, недостаточно средств.')
                self.lock.acquire()

bk = Bank()

th1 = threading.Thread(target = Bank.deposit, args = (bk,))
th2 = threading.Thread(target = Bank.take, args = (bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')




