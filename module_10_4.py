import threading
import time
import random
import queue


class Table:
    def __init__(self, number: int) -> None:
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name: str) -> None:
        threading.Thread.__init__(self)
        self.name = name

    def run(self) -> None:
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables: Table) -> None:
        self.tables = tables
        self.queue = queue.Queue()

    def guest_arrival(self, *guests: Guest) -> None:
        for guest in guests:
            for table in self.tables:
                if table.guest == None:
                    table.guest = guest
                    guest.start()
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            if not guest.is_alive():
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self) -> None:
        while not self.queue.empty() or self.occupied_tables():
            occupied_tables = [table for table in self.tables if table.guest != None]
            for table in occupied_tables:
                if not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    table.guest = None
                    print(f"Стол номер {table.number} свободен")
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        table.guest.start()
                        print(
                            f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}"
                        )
            free_tables = [table for table in self.tables if table.guest == None]
            for table in free_tables:
                if not self.queue.empty():
                    table.guest = self.queue.get()
                    table.guest.start()
                    print(
                        f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}"
                    )

    def occupied_tables(self) -> None:
        occupied = False
        for table in self.tables:
            if not table.guest == None:
                occupied = True
                break
        return occupied


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    "Maria",
    "Oleg",
    "Vakhtang",
    "Sergey",
    "Darya",
    "Arman",
    "Vitoria",
    "Nikita",
    "Galina",
    "Pavel",
    "Ilya",
    "Alexandra",
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()