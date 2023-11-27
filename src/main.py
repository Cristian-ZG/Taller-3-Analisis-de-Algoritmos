import random

from src.ejercicio1.StoogeSort import sSort
from src.ejercicio3.InsertionSort import iSort
from src.ejercicio3.MergeSort import mSort
from src.ejercicio3.QuickSort import qSort


class AlgoritmosTester:
    @staticmethod
    def main():
        # Crea una arreglo aleatorio de tamaño 10.
        list10 = [random.randint(1, 100) for _ in range(10)]
        print(f"Lista aleatoria de tamaño 10: {list10}")

        # Ejercicio 1 - Test StoogeSort
        print("\nEjercicio 1 - Algoritmo StoogeSort")
        print(sSort.stoogeSort(list10))

        print("\n")

        # Ejercicio 3
        print("\nEjercicio 3 - Algoritmo InsertionSort")
        print(iSort.insertionSort(list10))

        print("\nEjercicio 3 - Algoritmo MergeSort")
        print(mSort.mergeSort(list10))

        print("\nEjercicio 3 - Algoritmo QuickSort")
        print(qSort.quickSort(list10, 0, len(list10)-1))



if __name__ == '__main__':
    AlgoritmosTester.main()

