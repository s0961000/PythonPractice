"""

(0) [2,7,3,4,5] (0)

Index = 2

2 + 7 = 9
4 + 5 = 9
9 = 9

Prefix Sum

Adding each index to each other
[2,9,12,16,21]

(2) Chris gave you A apples
---
(9) Nick gave you X apples
(12) Anthony gave you Y apples
(16) Krusty gave you Z apples
---
(21) Jesus gave you B apples

Sum of the array = 21
Sum up to 0 index = 2
Sum up to 1 index = 9
Sum of just 1 index = 7
Sum up to 2 index = 12
Sum from 1 to 2 index = 10

Sum up to any point = Addition of each index together
But for a certain block of indexes: PrefixSum(indexEnd) - PrefixSum(indexStart - 1)

"""


def create_prefix_array(numbers):
    total = 0
    prefix_array = []
    for i in numbers:
        total += i
        prefix_array.append(total)
    return prefix_array


# [2, 9, 12, 16, 21]
def find_pivot(input_array):
    prefix_array = create_prefix_array(input_array)
    for idx, val in enumerate(prefix_array):
        left_values = 0
        right_values = 0
        # If at 0 index, value will be 0
        if idx != 0:
            left_values = prefix_array[idx - 1]
        right_values = prefix_array[len(prefix_array) - 1] - prefix_array[idx]
        print(f"left_values: {left_values}, right_values: {right_values}")
        if left_values == right_values:
            return idx


if __name__ == "__main__":
    input_array = [2,1,-1]
    print(input_array)
    print(create_prefix_array(input_array))
    print(find_pivot(input_array))
