from src.my_array import MyArray


def reverse_array(array: MyArray) -> MyArray:
    left = 0
    right = len(array) - 1

    while left < right:
        array[left], array[right] = array[right], array[left]

        left += 1
        right -= 1

    return array
