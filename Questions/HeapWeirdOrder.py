"""

Given an unsorted array such as: [1,3,2,5,4], return an array with the following:

    [Highest, Lowest, Highest - 1, Lowest - 1, Highest - 2, Lowest - 2, ..., Highest - n, Lowest - n]

The answer here would be:

    [5,1,4,2,3]

"""

from heapq import heappop, heappush, heapify


def highest_lowest(values):

    val_len = len(values)

    # Creating min-heap and max-heap of values
    min_heap = values
    max_heap = []
    result_array = []
    heapify(min_heap)
    for i in values:
        heappush(max_heap, -1 * i)
    print(f"min_heap: {min_heap} max_heap: {max_heap}")

    # Getting Remaining Values
    for i in range(val_len):
        result_array.append(-1 * heappop(max_heap))
        result_array.append(heappop(min_heap))

    final_array = result_array[0:val_len]

    return final_array


if __name__ == "__main__":
    input_array = [1, 3, 2, 5, 4]
    print(highest_lowest(input_array))


"""

Anthony's

# Getting Remaining Values
    is_large_next = True
    for i in range(val_len):
        if is_large_next:
            result_array.append(-1 * heappop(max_heap))
        else:
            result_array.append(heappop(min_heap))
            
        is_large_next = not is_large_next

    return result_array

"""
