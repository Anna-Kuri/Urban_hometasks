import threading
import time
import datetime


def write_words(word_count: int, file_name: str) -> None:
   
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}" + "\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


start_time = time.time()

func1 = write_words(10, "example1.txt")
func2 = write_words(30, "example2.txt")
func3 = write_words(200, "example3.txt")
func4 = write_words(100, "example4.txt")

end_time = time.time()

elapsed_time = end_time - start_time

print(f"Время работы функций {datetime.timedelta(seconds=elapsed_time)}")

start_time_2 = time.time()
thread1 = threading.Thread(target=write_words, args=(10, "example5.txt"))
thread2 = threading.Thread(target=write_words, args=(30, "example6.txt"))
thread3 = threading.Thread(target=write_words, args=(200, "example7.txt"))
thread4 = threading.Thread(target=write_words, args=(100, "example8.txt"))


thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

end_time_2 = time.time()

elapsed_time_2 = end_time_2 - start_time_2

print(f"Время работы потоков {datetime.timedelta(seconds=elapsed_time_2)}")