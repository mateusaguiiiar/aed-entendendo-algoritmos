from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    stack = MyStack()
    mapping = {")": "(", "}": "{", "]": "["}

    for char in string:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty():
                return False
            if stack.pop() != mapping[char]:
                return False

    return stack.is_empty()
