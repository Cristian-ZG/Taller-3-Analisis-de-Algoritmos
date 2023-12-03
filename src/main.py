import random
import time
import sys

from src.ejercicio1.StoogeSort import sSort
from src.ejercicio3.InsertionSort import iSort
from src.ejercicio3.MergeSort import mSort
from src.ejercicio3.QuickSort3 import QuickSort3


class AlgoritmosTester:
    @staticmethod
    def main():

        # Se cambia el limite de recursion que viene por defecto.
        #sys.setrecursionlimit(20000)
        # Crea una arreglo aleatorio de tamaño 10.
        listn = [random.randint(1, 100) for _ in range(100)]
        print(f"Lista aleatoria de tamaño {len(listn)}: {listn}\n")

        #Ejercicio 1 - Test StoogeSort
        def ejr1():
            print("\nEjercicio 1 - Algoritmo StoogeSort")
            inicio1 = time.perf_counter()
            print(sSort.stoogeSort(listn))
            fin1 = time.perf_counter()
            print(f"El tiempo de ejecución de Ejr1(StoogeSort) fue: {fin1-inicio1:0.5f} segundos")

            print("\n")

        # Ejercicio 2
        def ejr2():
            inicio2 = time.time()
            print("Aqui va el llamado del segundo")
            fin2 = time.time()
            print(f"El tiempo de ejecución de Ejr2(Divide y venceras) fue: {fin2 - inicio22:0.5f} segundos")

        # Ejercicio 3}
        def ejr3():
            print("\nEjercicio 3 - Algoritmo InsertionSort")
            inicio3a = time.perf_counter()
            print(iSort.insertionSort(listn))
            fin3a = time.perf_counter()
            print(f"El tiempo de ejecución del Ejr3(InsertionSort) fue de :  {fin3a - inicio3a:0.5f} segundos \n")

            print("\nEjercicio 3 - Algoritmo MergeSort")
            inicio3b = time.perf_counter()
            print(mSort.mergeSort(listn))
            fin3b = time.perf_counter()
            print(f"El tiempo de ejecución del Ejr3(MergeSort) fue de : {fin3b - inicio3b:0.5f} segundos \n")

            print("\nEjercicio 3 - Algoritmo QuickSort")
            inicio3c = time.perf_counter()
            print(QuickSort3.quickSort(listn,0,len(listn)-1))
            fin3c = time.perf_counter()
            print(f"El tiempo de ejecución del Ejr3(QuickSort) fue de :  {fin3c - inicio3c:0.5f} segundos \n")
        def salir():
            print("¡Hasta luego!")
            sys.exit()

        while True:
            print("¿Qué desea hacer?")
            print("1. Ejecutar algortimo del ejercicio 1")
            print("2. Ejecutar algoritmo del ejercicio 2")
            print("3. Ejecutar algortimos del ejercicio3")
            print("4. Salir")

            opcion = input("Ingrese su opción: ")

            if opcion == "1":
                ejr1()
            elif opcion == "2":
                ejr2()
            elif opcion == "3":
                ejr3()
            elif opcion == "4":
                salir()



if __name__ == '__main__':
    AlgoritmosTester.main()

