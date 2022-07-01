import os
import concurrent.futures
import timeit
from split import split
from data import numbers_data
from html_builder import build_html


processor_count = os.cpu_count()


def add_sys_vars(arr):
    html_base = '<section class="sysvars">'
    for i in arr:
        html_base += '<p>' + str(i) + '</p>'
    html_base += "</section>"
    return html_base


def count(numbers):
    suma = 0
    for i in numbers:
        suma += i
    return suma

def multi_process():
    identifiers = ["P1", "P2", "P3", "P4"]
    numbers = numbers_data.numbers
    split_numbers = list(split(numbers, 4))

    def test():
        with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
            executor.map(count, identifiers, split_numbers)

    timeit_result = timeit.timeit(test, number=1)
    return "%.3f" % round(timeit_result, 3)


def multi_process_max():
    numbers = numbers_data.numbers
    identifiers = []
    for i in range(processor_count):
        identifiers.append("P" + str(i + 1))

    split_numbers = list(split(numbers, processor_count))

    def test():
        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(count, identifiers, split_numbers)

    timeit_result = timeit.timeit(test, number=1)
    return "%.3f" % round(timeit_result, 3)


def multi_thread():
    identifiers = ["T1", "T2", "T3", "T4"]
    numbers = numbers_data.numbers
    split_numbers = list(split(numbers, 4))

    def test():
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            executor.map(count, identifiers, split_numbers)

    timeit_result = timeit.timeit(test, number=1)
    return "%.3f" % round(timeit_result, 3)


def single_thread():
    identifiers = ["T1"]
    numbers = numbers_data.numbers
    split_numbers = list(split(numbers, 1))

    def test():
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            executor.map(count, identifiers, split_numbers)

    timeit_result = timeit.timeit(test, number=1)
    return "%.3f" % round(timeit_result, 3)


def fill_result_array(arr, func, times):
    for i in range(times):
        arr.append(func())


def main():
    multi_process_result = []
    multi_process_max_result = []
    multi_thread_max_result = []
    single_thread_result = []

    result_list = [multi_process_result, multi_process_max_result, multi_thread_max_result, single_thread_result]
    func_list = [multi_process, multi_process_max, multi_thread, single_thread]

    for i in result_list:
        func = func_list[result_list.index(i)]
        fill_result_array(i, func, 5)

    median_list = []

    for i in result_list:
        x = [*i]
        x.sort()
        print(x)
        median = x[2]
        median_list.append(median)

    nameplate_list = ["4 processes (s)", "processes based on number of CPUs (s)", "4 threads (s)", "1 thread (s)"]

    result_dict = dict(zip(nameplate_list, result_list))

    build_html(result_dict, median_list, nameplate_list)

    return


if __name__ == '__main__':
    main()
