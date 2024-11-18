import time
import threading


class Knight(threading.Thread):
    number_of_enemies = 100
    days = 0
    DELAY = 1  
    def __init__(self, name: str, power: int) -> None:
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self) -> None:
        print(f"{self.name}, на нас напали!")

        while self.number_of_enemies:
            time.sleep(self.DELAY)

            self.days += 1
            self.number_of_enemies -= self.power

            print(
                f"{self.name} сражается {self.days} день(дня)..., осталось {self.number_of_enemies} воинов."
            )

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
