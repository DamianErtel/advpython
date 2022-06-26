import platform
import sys
import os
import concurrent.futures
import time
import timeit
from data import numbers_data

# define system variables

python_v = platform.python_version()
python_interpreter = sys.version
system_type = platform.system()
system_v = platform.release()
processor_type = platform.processor()
processor_count = os.cpu_count()


# check system variables

# print(python_v)
# print(python_interpreter)
# print(system_type)
# print(system_v)
# print(processor_type)
# print(processor_count)


# execute code

# numbers = numbers_data.numbers
# result = 0
# for num in numbers:
#     result += num
#
# print("\nresult1: ", result)

def count(identifier, numbers):
    suma = 0
    for i in numbers:
        # print("id:", identifier, "i =", i)
        # time.sleep(1)
        suma += i
    return suma


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


def multi_process():
    identifiers = ["P1", "P2", "P3", "P4"]
    numbers = numbers_data.numbers
    split_numbers = list(split(numbers, 4))
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        start_time = time.time()
        wyniki_czastkowe = executor.map(count, identifiers, split_numbers)
        suma_wszystkich = sum(wyniki_czastkowe)
        print("EXEC TIME - 4 PROCESS: ", (time.time() - start_time))

    # print('suma:', suma_wszystkich)


def multi_process_max():
    numbers = numbers_data.numbers
    identifiers = []
    for i in range(processor_count):
        identifiers.append("P" + str(i + 1))

    split_numbers = list(split(numbers, processor_count))
    with concurrent.futures.ProcessPoolExecutor() as executor:
        start_time = time.time()
        wyniki_czastkowe = executor.map(count, identifiers, split_numbers)
        suma_wszystkich = sum(wyniki_czastkowe)
        print("EXEC TIME - MAX PROCESS: ", (time.time() - start_time))

    # print('suma2:', suma_wszystkich)


def multi_thread():
    identifiers = ["T1", "T2", "T3", "T4"]
    numbers = numbers_data.numbers
    split_numbers = list(split(numbers, 4))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        start_time = time.time()
        wyniki_czastkowe = executor.map(count, identifiers, split_numbers)
        suma_wszystkich = sum(wyniki_czastkowe)
        print("EXEC TIME - 4 THREADS: ", (time.time() - start_time))

    # print('suma:', suma_wszystkich)


def single_thread():
    identifiers = ["T1"]
    numbers = numbers_data.numbers
    split_numbers = list(split(numbers, 1))
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        start_time = time.time()
        wyniki_czastkowe = executor.map(count, identifiers, split_numbers)
        suma_wszystkich = sum(wyniki_czastkowe)
        print("EXEC TIME - ONE THREAD: ", (time.time() - start_time))

    # print('suma:', suma_wszystkich)


def main():
    multi_process()
    multi_process_max()
    multi_thread()
    single_thread()


if __name__ == '__main__':
    main()
