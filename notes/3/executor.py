import concurrent.futures
import time

def licz(identyfikator):
    suma = 0
    for i in range(10):
        print("id:", identyfikator, "i =", i)
        time.sleep(1)
        suma += i

    return suma

def main():
    identyfikatory = ["P1", "P2", "P3", "P4"]
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        wyniki_czastkowe = executor.map(licz, identyfikatory)
        suma_wszystkich = sum(wyniki_czastkowe)

    print('suma:', suma_wszystkich)

if __name__ == '__main__':
    main()
