class QuickSort2:
    @staticmethod
    def dividir(lista):
        pivote = lista[0]
        menores = []
        mayores = []

        for i in range(1, len(lista)):
            if lista[i] < pivote:
                menores.append(lista[i])
            else:
                mayores.append(lista[i])
        return menores, pivote, mayores

    @staticmethod
    def quickSort(lista):
        if len(lista) < 2:
            return lista

        menores, pivote, mayores = QuickSort2.dividir(lista)
        return QuickSort2.quickSort(menores) + [pivote] + QuickSort2.quickSort(mayores)
