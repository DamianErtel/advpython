import platform
import sys
import os
import concurrent.futures
import time
import timeit
from data import numbers_data
from html_builder import build_html

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

def add_sys_vars(arr):
    # html_args = map(lambda x: "<p>" + str(x) + "</p>", args)
    # print(sum(html_args))
    html_base = '<section class="sysvars">'
    for i in arr:
        html_base += '<p>' + str(i) + '</p>'
    html_base += "</section>"
    return html_base


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
        executor.map(count, identifiers, split_numbers)
        time_result = (time.time() - start_time)
        print("MP", time_result)
    return time_result


def multi_process_max():
    numbers = numbers_data.numbers
    identifiers = []
    for i in range(processor_count):
        identifiers.append("P" + str(i + 1))

    split_numbers = list(split(numbers, processor_count))
    with concurrent.futures.ProcessPoolExecutor() as executor:
        start_time = time.time()
        executor.map(count, identifiers, split_numbers)
        time_result = (time.time() - start_time)
        print("MP MAX", time_result)
    return time_result


def multi_thread():
    identifiers = ["T1", "T2", "T3", "T4"]
    numbers = numbers_data.numbers
    split_numbers = list(split(numbers, 4))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        start_time = time.time()
        executor.map(count, identifiers, split_numbers)
        time_result = (time.time() - start_time)
        print("MT", time_result)
    return time_result


def single_thread():
    identifiers = ["T1"]
    numbers = numbers_data.numbers
    split_numbers = list(split(numbers, 1))
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        start_time = time.time()
        executor.map(count, identifiers, split_numbers)
        time_result = (time.time() - start_time)
        print("ST", time_result)
    return time_result


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

    nameplate_list = ["4 processes (s)", "processes based on number of CPUs (s)", "4 threads (s)", "1 thread (s)"]

    result_dict = dict(zip(nameplate_list, result_list))

    sys_vars = add_sys_vars([python_v, python_interpreter, system_type, system_v, processor_type, processor_count])

    build_html(result_dict, sys_vars)

    # print(result_dict)


if __name__ == '__main__':
    main()
