from src.my_array import MyArray


def merge_sort(array: MyArray) -> MyArray:
    if array is None or len(array) <= 1:
        return array

    def sort_logic(arr_list: list) -> list:
        if len(arr_list) <= 1:
            return arr_list

        mid = len(arr_list) // 2
        left = sort_logic(arr_list[:mid])
        right = sort_logic(arr_list[mid:])

        return merge(left, right)

    sorted_elements = sort_logic(list(array))

    for i in range(len(array)):
        array[i] = sorted_elements[i]

    return array


def merge(left: list, right: list) -> list:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result
