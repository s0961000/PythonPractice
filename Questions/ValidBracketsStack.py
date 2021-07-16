"""

[], {}, ()

Given a string, return true or false if valid parentheses

[{()}] = Valid
{} = Valid
( = Not Valid
{]} = Not Valid

"""

from collections import deque


def valid_parentheses(value):
    # Empty String returns True
    if value == "":
        return True

    if len(value) <= 1 or value is None or len(value) % 2 != 0:
        return False

    my_stack = deque()
    brackets = {")": "(", "]": "[", "}": "{"}
    opening_brackets = ["(", "[", "{"]
    closing_brackets = [")", "]", "}"]

    # Need to Check that Stack does not start with Closing Bracket
    if value[0] in closing_brackets:
        return False

    for i in value:
        if i in opening_brackets:
            my_stack.append(i)
        elif len(my_stack) == 0 and i in closing_brackets:
            # If there is a closing bracket and stack is empty, there is no matching opening bracket
            return False
        else:
            if my_stack.pop() != brackets[i]:
                return False

    # Need to Check that Stack is empty
    if len(my_stack) != 0:
        return False

    # Otherwise return True
    return True


if __name__ == "__main__":
    print(valid_parentheses("]["))

    print("--- These Should All Be True ---")
    print(valid_parentheses(""))
    print(valid_parentheses("{}"))
    print(valid_parentheses("[]"))
    print(valid_parentheses("()"))
    print(valid_parentheses("[{()}]"))
    print(valid_parentheses("{}()[]"))
    print("--- These Should All Be False ---")
    print(valid_parentheses("({"))
    print(valid_parentheses("{]}"))
    print(valid_parentheses("{"))
    print(valid_parentheses("}"))
    print(valid_parentheses("(){}}{"))
