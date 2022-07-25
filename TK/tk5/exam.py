"""Test 5."""


def rotate_left3(nums):
    """
    Given an array of ints length 3, return an array with the elements "rotated left" so [1, 2, 3] yields [2, 3, 1].

    rotate_left3([1, 2, 3]) → [2, 3, 1]
    rotate_left3([5, 11, 9]) → [11, 9, 5]
    rotate_left3([7, 0, 0]) → [0, 0, 7]

    :param nums: List of integers of length 3.
    :return: Rotated list.
    """
    return [nums[1], nums[2], nums[0]]


def is_sum_of_two(a, b, c):
    """
    Whether one parameter is a sum of other two.

    is_sum_of_two(3, 2, 1) => True
    is_sum_of_two(3, 1, 1) => False
    is_sum_of_two(3, 2, 5) => True
    """
    if a == b + c or b == a + c or c == a + b:
        return True
    return False


def middle_chars(s: str) -> str:
    """Return two chars in the middle of string.

    The length of the string is an even number.

    middle_chars("abcd") => "bc"
    middle_chars("bc") => "bc"
    middle_chars("aabbcc") => "bb"
    middle_chars("") => ""
    """
    half = len(s) // 2
    if len(s) == 3:
        return s[half]
    elif len(s) > 3:
        return s[half - 1:half + 1]
    return s


def non_decreasing_list(nums):
    """
    Given a list of numbers.

    If given list is a non-decreasing list, return True, otherwise False.
    Non-decreasing means every next element in the list must not be smaller than the previous one.

    non_decreasing_list([0, 1, 2, 3, 98]) => True
    non_decreasing_list([50, 49]) => False
    non_decreasing_list([12, 12]) => True

    :param nums:
    :return:
    """
    counter = -1000
    naruto = 0
    for a in nums:
        if a >= counter:
            naruto += 1
            counter = a
    if naruto == len(nums):
        return True
    return False


def remove_in_middle(text, to_remove):
    """
    Remove substring from the text, except for the first and the last occurrence.

    remove_in_middle("abc", "def") => "abc"
    remove_in_middle("abcabcabc", "abc") => "abcabc"
    remove_in_middle("abcdabceabcabc", "abc") => "abcdeabc"
    remove_in_middle("abcd", "abc") => "abcd"
    remove_in_middle("abcdabc", "abc") => "abcdabc"
    remove_in_middle("ABCAaaaAA", "a") => "ABCAaaAA

    :param text: string from where the remove takes place.
    :param to_remove: substring to be removed.
    :return: string with middle substrings removed.
    """
    if len(to_remove) > len(text) // 2:
        return text
    first = text.index(to_remove) + len(to_remove)
    last = text.rindex(to_remove)
    text = text[:first] + text[first:].replace(to_remove, "") + text[last:]
    return text


if __name__ == '__main__':
    print(rotate_left3([1, 2, 3]))
    print(is_sum_of_two(3, 2, 1))
    print(middle_chars("fas"))
    print(non_decreasing_list([0, 1, 2, 3, 98]))
    print(remove_in_middle("aaaaaaa", "aaaa"))
