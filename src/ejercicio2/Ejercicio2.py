from collections import Counter
class Moda:
    def moda(arr):
        if len(arr) == 1:
            return arr

        mid = len(arr) // 2
        left_part = arr[:mid]
        right_part = arr[mid:]

        moda_izquierda = Moda.moda(left_part)
        moda_derecha = Moda.moda(right_part)

        # Combinar las modas de ambas mitades
        return Moda.combinarModas(moda_izquierda, moda_derecha, arr)


    def combinarModas(moda_izquierda, moda_derecha, arr):
        if moda_izquierda == moda_derecha:
            return moda_izquierda

        else:
            frecuencias = Counter(arr)
            max_frecuencia = max(frecuencias.values())
            modas = [elemento for elemento, frecuencia in frecuencias.items() if frecuencia == max_frecuencia]
            return modas
