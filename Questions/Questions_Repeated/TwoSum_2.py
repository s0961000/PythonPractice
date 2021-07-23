"""

[2,3,7,9] -> target = 5

Return (0,1)

"""


def two_sum(values, target):
    # Must have at least two numbers to add
    if len(values) <= 1 or values is None:
        return False
    # Creating Map to associate numbers
    map_values = {}
    for idx, val in enumerate(values):
        map_values[target - val] = idx

    # Loop through values to find match in map and return both indices
    for idx, val in enumerate(values):
        if val in map_values and idx != map_values[val]:
            return idx, map_values[val]
    return False


if __name__ == "__main__":
    print(two_sum([2, 3, 7, 9], 5))
    print(two_sum([9, 7, 3, 2], 11))
    print(two_sum([5], 5))
    print(two_sum([1, 2, 3], 7))
