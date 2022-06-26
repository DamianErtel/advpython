import multiprocessing
import time

def licz(identyfikator, kolejka):
    suma = 0
    for i in range(10):
        print("id:", identyfikator, "i =", i)
        time.sleep(1)
        suma += i

    kolejka.put(suma)

def main():
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=licz, args=("P1", q) )
    p2 = multiprocessing.Process(target=licz, args=("P2", q) )

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    suma_wszystkich = 0
    while not q.empty():
        item = q.get()
        suma_wszystkich += item

    print('suma:', suma_wszystkich)

if __name__ == '__main__':
    main()
