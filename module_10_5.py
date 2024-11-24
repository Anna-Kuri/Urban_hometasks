import multiprocessing
import datetime


def read_info(name: str) -> None:
    all_data = []

    with open(name, "r", encoding="utf-8") as file:
        for _ in file:
            read_line = file.readline()
            all_data.append(read_line)

if __name__ == "__main__":

    filenames = [f"./file {number}.txt" for number in range(1, 5)]

    start = datetime.datetime.now()
    for file in filenames:
        read_info(file)
    end = datetime.datetime.now()
    print(f"Линейный вывод: {end - start}")

    start = datetime.datetime.now()
    with multiprocessing.Pool(4) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(f"Многопроцессный вывод: {end - start}")
