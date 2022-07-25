"""lala."""


def format_time(minutes):
    """
    Given minutes as an int, return correctly formatted time in hours and minutes.

    Correct format would be '{hours}h {minutes}min'.
    However, if there is not enough minutes to form an hour, show only minutes.
    In that case the format would be '{minutes}min'.
    But when there are no remaining minutes, show only hours.
    In that case the format would be '{hours}h'.
    One hour contains of 60 minutes.

    Examples:
    1) given 112 minutes, return '1h 52min'.
    2) given 23 minutes, return '23min'.
    3) given 180 minutes, return '3h'.

    :param minutes: given minutes
    :return: formatted time in hours and minutes
    """
    hours = 0
    while minutes >= 60:
        minutes = minutes - 60
        hours += 1
    if minutes == 0 and hours == 0:
        return str(minutes) + "min"
    elif minutes == 0:
        return str(hours) + "h"
    elif hours >= 1:
        return str(hours) + "h " + str(minutes) + "min"
    elif minutes < 60:
        return str(minutes) + "min"


def sorta_sum(a: int, b: int) -> int:
    """
    Given 2 ints, a and b, return their sum.

    However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

    sorta_sum(3, 4) → 7
    sorta_sum(9, 4) → 20
    sorta_sum(10, 11) → 21

    :param a: Integer
    :param b: Integer
    :return: Sum or 20
    """
    sum = a + b
    if 10 <= sum <= 19:
        sum1 = 20
        return sum1
    else:
        sum1 = a + b
        return sum1


def combo_string(s1: str, s2: str) -> str:
    """
    Return a new string of the form short + long + short.

    Given 2 strings, a and b, return a string of the form short+long+short,
    with the shorter string on the outside and the longer string on the inside.
    The strings will not be the same length, but they may be empty (length 0).

    combo_string('Hello', 'hi') → 'hiHellohi'
    combo_string('hi', 'Hello') → 'hiHellohi'
    combo_string('aaa', 'b') → 'baaab'

    :param s1:
    :param s2:
    :return:
    """
    if len(s1) > len(s2):
        print_value = (s2 + s1 + s2)
        return print_value
    elif len(s2) > len(s1):
        print_value2 = (s1 + s2 + s1)
        return print_value2
    else:
        return ""


def num_as_index(nums: list) -> int:
    """
    Return element which index is the value of the smaller of the first and the last element.

    If there is no such element (index is too high), return the smaller of the first and the last element.

    num_as_index([1, 2, 3]) => 2 (1 is smaller, use it as index)
    num_as_index([4, 5, 6]) => 4 (4 is smaller, but cannot be used as index)
    num_as_index([0, 1, 0]) => 0
    num_as_index([3, 5, 6, 1, 1]) => 5

    :param nums: list of non-negative integers.
    :return: element value in the specific index.
    """
    list2 = [nums[0], nums[-1]]
    min_value = (min(list2))  # 4
    counter = 0
    for i in nums:
        counter += 1
    if counter < min_value:
        return min_value
    else:
        return nums[min_value]


def count_clumps(nums: list) -> int:
    """
    Return the number of clumps in the given list.

    Say that a "clump" in a list is a series of 2 or more adjacent elements of the same value.

    count_clumps([1, 2, 2, 3, 4, 4]) → 2
    count_clumps([1, 1, 2, 1, 1]) → 2
    count_clumps([1, 1, 1, 1, 1]) → 1

    :param nums: List of integers.
    :return: Number of clumps.
    """
    counter = 0
    i = 0
    counter_groups = 0
    if len(nums) <= 1:
        return 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            counter += 1
        elif nums[i] != nums[i + 1] and counter >= 1:
            counter_groups += 1
            counter = 0
        i += 1
    if nums[-1] == nums[-2]:
        counter_groups += 1
    return counter_groups


if __name__ == '__main__':
    print(format_time(0))
    print(sorta_sum(3, 4))
    print(combo_string('hello', "hi"))
    print(num_as_index([4, 5, 6]))
    print(count_clumps([1, 2, 2, 3, 4, 4]))
