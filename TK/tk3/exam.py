"""Test 3 (R12)."""


def make_ends(nums: list) -> list:
    """
    Given an array of ints, return a new array length 2 containing the first and last elements from the original array.

    The original array will be length 1 or more.

    make_ends([1, 2, 3]) → [1, 3]
    make_ends([1, 2, 3, 4]) → [1, 4]
    make_ends([7, 4, 6, 2]) → [7, 2]

    :param nums: List of integers.
    :return: List with the first and the last element from the input list.
    """
    list1 = [nums[0], nums[-1]]
    return list1


def lucky_guess(n: int) -> bool:
    """Lucky guess."""
    stringg = str(n)
    if n == 1 or n == 3 or n == 7:
        return True
    elif -6 <= n <= 121 and n % 13 == 0:
        return True
    elif not stringg.count(str(5)) and not stringg.count(str(6)) and not n >= 0:
        return True
    else:
        return False


def extra_end(s: str) -> str:
    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string.

    The string length will be at least 2.

    extra_end('Hello') → 'lololo'
    extra_end('ab') → 'ababab'
    extra_end('Hi') → 'HiHiHi'

    :param s: Input string
    :return: 3 copies of last 2 chars.
    """
    if len(s) >= 2:
        return (s[-2] + s[-1]) * 3


def min_index_value(nums: list) -> int:
    """
    Take the first and the last element as indices of two elements and return the smaller of those elements.

    If at least one index is out of range, return -1.
    All the values are non-negative integers.

    min_index_value([1, 2, 3]) => -1 (3 is out of range)
    min_index_value([1, 2, 1]) => 2 (both elements point to 2)
    min_index_value([1, 2, 0]) => 1 (have to take minimum of 2 and 1)

    :param nums: List of non-negative integers.
    :return: Minimum value of two elements at positions of the first and the last element value.
    """
    nums_first = nums[0]
    nums_last = nums[-1]
    if nums_first > len(nums) - 1 or nums_last > len(nums) - 1:
        return -1
    nums_first = nums[nums_first]
    nums_last = nums[nums_last]
    if nums_last > nums_first:
        return nums_first
    return nums_last


def word_numeration(words: list) -> list:
    """
    For a given list of string, add numeration for every string.

    The input list consists of strings. For every element in the input list,
    the output list adds a numeration after the string.
    The format is as follows: #N, where N starts from 1.
    String comparison should be case-insensitive.
    The case of symbols in string itself in output list should remain the same as in input list.

    The output list has the same amount of elements as the input list.
    For every element in the output list, "#N" is added, where N = 1, 2, 3, ...

    word_numeration(["tere", "tere", "tulemast"]) => ["tere#1", "tere#2", "tulemast#1"]
    word_numeration(["Tere", "tere", "tulemast"]) => ["Tere#1", "tere#2", "tulemast#1"]
    word_numeration(["Tere", "tere", "tulemast", "no", "tere", "TERE"]) => ["Tere#1", "tere#2", "tulemast#1", "no#1", "tere#3", "TERE#4"]

    :param words: A list of strings.
    :return: List of string with numeration.
    """
    main_list = []
    list_2 = []
    for i in words:
        list_2.append(i.lower())
        main_list.append(i + '#' + str(list_2.count(i.lower())))
    return main_list


if __name__ == '__main__':
    print(make_ends([1, 2, 3]))
    print(lucky_guess(-123))
    print(extra_end('Hello'))
    print(min_index_value([1, 2, 1]))
    print(word_numeration(["Tere", "tere", "tulemast", "no", "tere", "TERE"]))
