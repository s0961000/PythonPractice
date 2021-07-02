"""
def times_by_2(number):
    1A/B. Define needed variables

    1A/B. Edge cases (bad input)
        if number is not None (making sure input is valid)
        if number > 0 (if only accepting positive numbers)
        if number is not string (making sure only integers are passed in)

    2. Comment out logic
        Write some psuedocode to have basic structure
        - Create maps
        - Add in digit tallies
        - Compare tallies

    3. return the output
        return True

def add_word(word_to_add):
    # Given a word, add to an empty string
    output = ""

     --- This prevents against NULL POINTER EXCEPTIONS ---

    return output

"""


"""
Efficient Example:

def is_anagram(s1, s2):
    ht = dict()

    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1
    for i in ht:
        if ht[i] != 0:
            return False
    return True

s1 = "fairy tales"
s2 = "rail safety"
## normalizing the strings
s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

print(is_anagram(s1, s2))
"""



def is_anagram(one, two):
    # If strings are different size
    if len(one) != len(two):
        return False

    map_one = {}
    map_two = {}

    for i in one:
        map_one[i] = 0
    for i in one:
        map_one[i] += 1
    for i in two:
        map_two[i] = 0
    for i in two:
        map_two[i] += 1

    # Letter in first word not found in second
    for key in map_one:
        if key not in map_two.keys():
            return False

    # Letter in second word not found in first
    for key in map_two:
        if key not in map_one.keys():
            return False

    # Both words have same letters, compare number
    for key in map_one:
        if map_one[key] != map_two[key]:
            return False

    return True


if __name__ == '__main__':
    print(is_anagram("aba", "bab"))        # false
    print(is_anagram("abba", "bbaa"))      # true
    print(is_anagram("", ""))              # true
    print(is_anagram("abaa", "aba"))       # false
    print(is_anagram("babba", "cabba"))    # false

