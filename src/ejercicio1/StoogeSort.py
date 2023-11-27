class sSort:
    @staticmethod
    def stoogeSort(arr, i = 0, j = None):
        if j is None:
            j = len(arr) - 1

        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

        if i + 1 >= j:
            return

        k = (j - i + 1) // 3

        sSort.stoogeSort(arr, i, j - k)
        sSort.stoogeSort(arr, i + k, j)
        sSort.stoogeSort(arr, i, j - k)

        return arr