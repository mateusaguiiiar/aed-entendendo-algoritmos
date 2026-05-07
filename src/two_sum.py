from src.my_array import MyArray


def two_sum(array: MyArray, target: int) -> tuple[int, int]:
    n = len(array)

    for i in range(n):
        for j in range(i + 1, n):
            if array[i] + array[j] == target:
                return i, j

    return -1, -1
