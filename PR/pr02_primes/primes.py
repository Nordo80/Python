"""Prime numbers."""
import math


def is_prime_number(number: int) -> bool:
    """
    Thi function defines prime number.

    :rtype: boolean
    """
    counter = 0
    """for i in range(2, number + 1):
        c = number % i
        if c == 0:
            counter += 1
        if counter > 2:
            break"""
    if number <= 1:
        return False
    b = number % number
    c = number % 1
    d = number % 2
    e = number % 3
    f = number % 5
    if c == 0:
        counter += 1
    if b == 0:
        counter += 1
    if d == 0 and number != 2:
        counter += 1
    if e == 0 and number != 3:
        counter += 1
    if f == 0 and number != 5:
        counter += 1
    if (math.sqrt(number) % 1) == 0:
        counter += 1
    if counter == 2:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_prime_number(121))  # -> True
    print(is_prime_number(169))  # -> True
    print(is_prime_number(0))  # -> True
    print(is_prime_number(4))  # -> False
    print(is_prime_number(7))  # -> True
    print(is_prime_number(88))  # -> False"""
