class mSort:
    @staticmethod
    def mergeSort(arr):
        if len(arr) == 1:
            return arr

        mitad = len(arr) // 2
        arrIzq = arr[:mitad]
        arrDer = arr[mitad:]

        ordenarIzq = mSort.mergeSort(arrIzq)
        ordenarDer = mSort.mergeSort(arrDer)

        return mSort.merge(ordenarIzq, ordenarDer)

    @staticmethod
    def merge(arrIzq, arrDer):
        arrSol = []
        while len(arrIzq) > 0 and len(arrDer) > 0:
            if arrIzq[0] > arrDer[0]:
                arrSol.append(arrDer[0])
                arrDer.pop(0)
            else:
                arrSol.append(arrIzq[0])
                arrIzq.pop(0)

        while len(arrIzq) > 0:
            arrSol.append(arrIzq[0])
            arrIzq.pop(0)

        while len(arrDer) > 0:
            arrSol.append(arrDer[0])
            arrDer.pop(0)

        return arrSol




