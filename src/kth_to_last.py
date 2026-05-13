from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:
    slow = head
    fast = head
    if k <= 0:
        return -1

    for i in range(k):
        if fast is None:
            return -1
        fast = fast.next

    while fast is not None:
        fast = fast.next
        slow = slow.next

    if slow is not None:
        return slow.value

    return -1
