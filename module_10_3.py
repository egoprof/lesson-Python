import threading
from random import randint
from threading import Lock
from time import sleep

class Bank:
    def init(self):
        self.balance: int = 0
        self.lock = Lock()

    def deposit(self):
        for trackup in range(100):
            if self.balance >=500 and self.lock.locked():
                self.lock.release()
            random_number = randint(50, 500)
            self.balance += random_number
            print(f'Пополнение: {random_number}. Баланс: {self.balance}')
            sleep(0.001)
    def take(self):
        for trackout in range(100):
            random_number1 = randint(50, 500)
            print(f"Запрос на {random_number1}")
            if self.balance >= random_number1:
                self.balance -= random_number1
                print(f'Снятие: {random_number1}. Баланс: {self.balance}')
            else:
                self.lock.acquire()
                print(f'Запрос отклонён, не достаточно средств.')
            sleep(0.001)

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
