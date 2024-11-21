import time
import threading
import random


class Bank(threading.Thread):
    lock = threading.Lock()

    def __init__(self, balance=0) -> None:
        threading.Thread.__init__(self)
        self.balance = balance

    def deposit(self) -> None:
        for _ in range(100):
            if (self.balance >= 500) and (self.lock.locked()):
                self.lock.release()
            else:
                pass
            amount = random.randint(50, 500)
            self.balance += amount
            time.sleep(0.001)
            print(f"Пополнение: {amount}. Баланс: {self.balance}")

    def take(self) -> None:
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            if amount <= self.balance:
                self.balance -= amount
                time.sleep(0.001)
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                time.sleep(0.001)
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")
