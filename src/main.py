import random
import time
import sys

from src.ejercicio1.StoogeSort import sSort
from src.ejercicio3.InsertionSort import iSort
from src.ejercicio3.MergeSort import mSort
from src.ejercicio3.QuickSort import qSort


class AlgoritmosTester:
    @staticmethod
    def main():
        # Se cambia el limite de recursion que viene por defecto.
        sys.setrecursionlimit(2500)
        # Crea una arreglo aleatorio de tamaño 10.
        list10 = [random.randint(1, 100) for _ in range(2000)]
        print(f"Lista aleatoria de tamaño {len(list10)}: {list10}")

        # Ejercicio 1 - Test StoogeSort
        print("\nEjercicio 1 - Algoritmo StoogeSort")
        inicio1 = time.time()
        print(sSort.stoogeSort(list10))
        fin1 = time.time()
        print(f"El tiempo de ejecución de Ejr1(StoogeSort) fue: {fin1-inicio1:0.5f} segundos")

        print("\n")

        # Ejercicio 2

        inicio2 = time.time()
        #Aqui va el llamado al algoritmo
        fin2 = time.time()
        print(f"El tiempo de ejecución de Ejr2(Divide y venceras) fue: {fin1 - inicio1:0.5f} segundos")

        # Ejercicio 3
        print("\nEjercicio 3 - Algoritmo InsertionSort")
        inicio3a = time.time()
        print(iSort.insertionSort(list10))
        fin3a = time.time()
        print(f"El tiempo de ejecución del Ejr3(InsertionSort) fue de :  {fin3a - inicio3a:0.5f} segundos \n")

        print("4\nEjercicio 3 - Algoritmo MergeSort")
        inicio3b = time.time()
        print(mSort.mergeSort(list10))
        fin3b = time.time()
        print(f"El tiempo de ejecución del Ejr3(MergeSort) fue de : {fin3b - inicio3b:0.5f} segundos \n")

        print("\nEjercicio 3 - Algoritmo QuickSort")
        inicio3c = time.time()
        print(qSort.quickSort(list10, 0, len(list10)-1))
        fin3c = time.time()
        print(f"El tiempo de ejecución del Ejr3(QuickSort) fue de :  {fin3c - inicio3c:0.5f} segundos")


if __name__ == '__main__':
    AlgoritmosTester.main()

