"""Test 1 (K14)."""


def workday_count(days):
    """
    Given number of days.

    Return how many of these days are workdays.
    Workdays are first five days of the weeks, last two are not.
    Always start from the start of the week.

    workday_count(9) => 7
    workday_count(3) => 3
    workday_count(7) => 5
    workday_count(15) => 11

    :param days: given number of days
    :return: workdays in given days
    """
    counter = 0
    sum = days
    temporary = sum - (sum % 7)
    counter += (temporary / 7)
    temporary = sum - (sum % 6)
    counter += (temporary / 6)
    counter2 = days - counter
    return counter2


def caught_speeding(speed, is_birthday):
    """
    Return which category speeding ticket you would get.

    You are driving a little too fast, and a police officer stops you.
    Write code to compute the result, encoded as an int value:
    0=no ticket, 1=small ticket, 2=big ticket.
    If speed is 60 or less, the result is 0.
    If speed is between 61 and 80 inclusive, the result is 1.
    If speed is 81 or more, the result is 2.
    Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

    caught_speeding(60, False) => 0
    caught_speeding(65, False) => 1
    caught_speeding(65, True) => 0

    :param speed: Speed value.
    :param is_birthday: Whether it is your birthday (boolean).
    :return: Which category speeding ticket you would get (0, 1, 2).
    """
    if is_birthday:
        speed -= 5
        if speed <= 60:
            return 0
        elif 61 <= speed <= 80:
            return 1
        elif speed >= 81:
            return 2
    else:
        if speed <= 60:
            return 0
        elif 61 <= speed <= 80:
            return 1
        elif speed >= 81:
            return 2


def first_half(text):
    """
    Return the first half of an string.

    The length of the string is even.

    first_half('HaaHoo') => 'Haa'
    first_half('HelloThere') => 'Hello'
    first_half('abcdef') => 'abc'
    """
    if len(text) % 2 == 0:
        slovo = text[:len(text) // 2]
        return slovo
    else:
        return text


def last_indices_elements_sum(nums):
    """
    Return sum of elements at indices of last two elements.

    Take element at the index of the last element value
    and take element at the index of the previous element value.
    Return the sum of those two elements.

    If the index for an element is out of the list, use 0 instead.

    The list contains at least 2 elements.

    last_indices_elements_sum([0, 1, 2, 0]) => 2 (0 + 2)
    last_indices_elements_sum([0, 1, 1, 7]) => 1 (just 1)
    last_indices_elements_sum([0, 1, 7, 2]) => 7 (just 7)
    last_indices_elements_sum([0, 1, 7, 8]) => 0 (indices too large, 0 + 0)

    :param nums: List of non-negative integers.
    :return: Sum of elements at indices of last two elements.
    """
    elem1 = nums[-1] #0
    elem2 = nums[-2] #2
    counter = 0
    counter2 = 0
    for word in nums:  # 0 1 2 0
        if elem2 == word:  # esli 0==0
            counter2 = word  #counter2 = 0
        elif elem1 == word:  # esli 2==2
            counter = word   #counter = 2
        sum = counter2 + counter
    return sum








def max_duplicate(nums):
    """
    Return the largest element which has at least one duplicate.

    If no element has duplicate element (an element with the same value), return None.

    max_duplicate([1, 2, 3]) => None
    max_duplicate([1, 2, 2]) => 2
    max_duplicate([1, 2, 2, 1, 1]) => 2

    :param nums: List of integers
    :return: Maximum element with duplicate. None if no duplicate found.
    """
    list_dublic = []
    for number in nums:
        if nums.count(number) > 1:
            list_dublic.append(number)

    if len(list_dublic) == 0:
        return None
    else:
        return max(list_dublic)


if __name__ == '__main__':
    print(workday_count(9))
    print(caught_speeding(50, False))
    print(first_half("HelloThere"))
    print(last_indices_elements_sum([0, 1, 2, 0]))
    print(max_duplicate([1, 2, 3, 7]))
