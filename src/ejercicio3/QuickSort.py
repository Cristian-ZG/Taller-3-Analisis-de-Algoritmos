class qSort:
    @staticmethod
    def quickSort(arr, low, high):
        if low < high:
            #Dividir y acomodar pivote.
            pi = qSort.partition(arr, low, high)

            qSort.quickSort(arr, low, pi - 1)
            qSort.quickSort(arr, pi + 1, high)
            return arr

    @staticmethod
    def partition(arr, low, high):
        #Pivote a la derecha
        pivot = arr[high]

        #Appuntador del ultimo elemento mas pequeño
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                #Avanzar apuntador.
                i = i + 1
                #Intercambiar los elementos.
                (arr[i], arr[j]) = (arr[j], arr[i])

        #Al final intercambia el pivote
        (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

        #Regresa la posición final del pivote.
        return i + 1

