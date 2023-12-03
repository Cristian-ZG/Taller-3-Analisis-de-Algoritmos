# Algoritmo QuickSort version de Hoare.
class QuickSort3:
    @staticmethod
    def divicion(lista, menor, mayor):
        pivote = lista[menor]
        izq = menor +1
        der = mayor

        while True:
            while izq <= der and lista[izq] <= pivote:
                izq += 1
            while izq <= der and lista[der] >= pivote:
                der -= 1
            if der < izq:
                break
            else:
                lista[izq], lista[der] = lista[der], lista[izq]
        lista[menor], lista[der] = lista[der], lista[menor]
        return der

    @staticmethod
    def quickSort(lista, menor, mayor):
        if menor < mayor:
            pivote = QuickSort3.divicion(lista, menor, mayor)
            QuickSort3.quickSort(lista, menor, pivote-1)
            QuickSort3.quickSort(lista, pivote+1, mayor)
            return lista
