import timeit


def licz():
    suma = 0
    for i in range(0, 60000):
        suma += i


czas_wykonania = timeit.timeit(licz, number=1)
print('czas wykonania:', czas_wykonania)
