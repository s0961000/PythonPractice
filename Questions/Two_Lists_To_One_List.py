# Two pointers ie: i and j

# Lists are already sorted

"""
[1,2,10]     [7,8]
 ^
 ^

 [1,2,10]     [7,8]
  ^            ^

[1,]
"""


def one_list(list_one, list_two):
    final_list = []
    one_ptr = 0
    two_ptr = 0

    length = len(list_one) + len(list_two)

    print(length)

    for i in range(length):
        if one_ptr >= len(list_one):
            # only use two
            print(f"adding {list_two[two_ptr]}")
            final_list.append(list_two[two_ptr])
            two_ptr += 1
            continue
        elif two_ptr >= len(list_two):
            # only use one
            print(f"adding {list_one[one_ptr]}")
            final_list.append(list_one[one_ptr])
            one_ptr += 1
            continue
        # append the smallest one
        # update the correct pointer
        if list_one[one_ptr] < list_two[two_ptr]:
            print(f"ONE comparing {list_one[one_ptr]} to {list_two[two_ptr]}")
            final_list.append(list_one[one_ptr])
            one_ptr += 1
        else:
            print(f"TWO comparing {list_one[one_ptr]} to {list_two[two_ptr]}")
            final_list.append(list_two[two_ptr])
            two_ptr += 1

    return final_list


"""
    longest_list = []
    shortest_list = []
    final_list = []
    
    # Getting Longest List
    if len(list_one) > len(list_two):
        longest_list = list_one
        shortest_list = list_two
    else:
        longest_list = list_two
        shortest_list = list_one

    for i in longest_list:
        final_list.append(i)

    for idx, val in enumerate(shortest_list):
        for idx_long, val_long in enumerate(final_list):
            if val < val_long:
                final_list.insert(idx_long, val)
                shortest_list[idx] = 0
                break

    # if short_list length != 0 add remaining items to final_list
    if len(shortest_list) > 0:
        for i in shortest_list:
            if i != 0:
                final_list.append(i)

"""

if __name__ == "__main__":
    # print(one_list(['7', '8', '9'], ['1', '2', '3']))
    print(one_list([1, 2, 10], [7, 8]))
