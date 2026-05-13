from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:
    if array is None or len(array) <= 1:
        return array

    _quick_sort_recursive(array, 0, len(array) - 1)
    return array


def _quick_sort_recursive(array: MyArray, low: int, high: int):
    if low < high:
        pivot_index = _partition(array, low, high)

        _quick_sort_recursive(array, low, pivot_index - 1)
        _quick_sort_recursive(array, pivot_index + 1, high)


def _partition(array: MyArray, low: int, high: int) -> int:

    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            # Troca os elementos de lugar (swap)
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1
