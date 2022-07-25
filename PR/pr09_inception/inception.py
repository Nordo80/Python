"""If you're going to perform inception, you need imagination."""

list_countdown = []


def countdown(n: int):
    """
    Write a simple recursive function that returns a list of numbers that count down from n.

    countdown(5) -> [5, 4, 3, 2, 1, 0]
    countdown(8) -> [8, 7, 6, 5, 4, 3, 2, 1, 0]
    countdown(-1) -> []

    :param n: start
    :return: countdown sequence
    """
    if n <= -1:
        list_countdown.clear()
        list_countdown == []
        return list_countdown
    if n >= 1:
        if len(list_countdown) == 0:
            list_countdown.append(n)
            return countdown(n - 1)
        if list_countdown[-1] != n + 1:
            list_countdown.clear()
            list_countdown.append(n)
            return countdown(n - 1)
        else:
            list_countdown.append(n)
            return countdown(n - 1)
    if n == 0:
        list_countdown.append(n)
        return list_countdown


string_add_commas1 = ""
string_numbers = ""


def add_commas(n: int):
    """
    In representing large numbers, from the right side to the left.

    English texts usually use commas to separate each group of three digits in front of the decimal.
    Your challenge is to output a number n formatted with commas.

    add_commas(1245) -> '1,245'
    add_commas(123456789) -> '123,456,789' 9
    add_commas(1011) -> '1,011'

    :param n: int
    :return: string of the formatted int
    """
    global string_add_commas1
    global string_numbers
    str_n = str(n)
    if len(string_numbers) >= 1:
        if string_numbers[-1] == "a":
            string_numbers = ""
            string_add_commas1 = ""
    if len(str_n) >= 1:
        if len(string_numbers) % 3 == 0 and len(string_add_commas1) != 0:
            a = "," + str_n[-1]
            b = str_n[-1]
            removed_n = str_n[:-1]
            string_add_commas1 += a
            string_numbers += b
            return add_commas(removed_n)
        else:
            a = str_n[-1]
            removed_n = str_n[:-1]
            string_add_commas1 += a
            string_numbers += a
            return add_commas(removed_n)
    else:
        reversed_string = string_add_commas1[::-1]
        string_numbers += "a"

        return reversed_string


def truncate(n, decimals=0):
    """
    Each year your crypto-investment grows.

    Wqdwdwdq.

    :returns n
    """
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def stonks(coins, rate, years):
    """
    Each year your crypto-investment grows.

    Write a recursive function that calculates the net worth of coins after some years.
    Rate is in percents.
    Round the answer down to the nearest integer.

    stonks(1000, 10, 10) -> 2593
    stonks(100000, 12, 3) -> 140492

    :param coins: starting amount (0-100000)
    :param rate: starting amount (0-100)
    :param years: starting amount (0-50)
    :return: coins after years
    """
    if years != 0:
        coins += (coins * (rate / 100))
        return stonks(coins, rate, years - 1)
    return truncate(coins)


def quic_mafs(a: int, b: int):
    """
    Write a recursive function that applies the following operations.

    i) If a=0 or b=0, return [a,b]. Otherwise, go to step (ii);
    ii) If a>=2*b, set a = a-2*b, and repeat step (i). Otherwise, go to step (iii);
    iii) If b>=2*a, set b = b-2*a, to i or return [a,b].

    quic_mafs(6, 19) -> [6, 7]
    quic_mafs(2, 1) -> [0, 1]
    quic_mafs(22, 5) -> [0, 1]
    quic_mafs(8796203,7556) -> [1019,1442]

    :param a: int
    :param b: int
    :return: result
    """
    if a >= 2 * b:
        return quic_mafs(a - (2 * b), b)  # a = 12 b = 5
    else:
        if a == 0 or b == 0:
            return [a, b]
        else:
            if b > 2 * a:
                return quic_mafs(a, b - (2 * a))
            elif a < 2 * b and b < 2 * a:
                return [a, b]


counter = 0
counter1 = 0


def sum_squares(nested_list):
    """
    Write a function that sums squares of numbers in list.

    That list may contain additional lists.
    (Hint use the type() or isinstance() function)

    sum_squares([1, 2, 3]) -> 14
    sum_squares([[1, 2], 3]) -> sum_squares([1, 2]) + 9 -> 1 + 4 + 9 -> 14
    sum_squares([[[[[[[[[2]]]]]]]]]) -> 4

    :param nested_list: list of lists of lists of lists of lists ... and ints
    :return: sum of squares
    """
    # [1,2],3
    # list_list22 [[1,2]]
    # nested_list 3
    # counter =
    global counter
    global counter1
    if counter1 == 1:
        counter = 0
        counter1 = 0
    if len(nested_list) != 0:
        if type(nested_list[0]) is list:
            lala = nested_list[0] + nested_list[1::]
            return sum_squares(lala)
        else:
            counter += nested_list[0] ** 2
            nested_list.remove(nested_list[0])
            return sum_squares(nested_list)
    else:
        counter1 += 1
        return counter


if __name__ == "__main__":
    print(countdown(5))  # -> [5, 4, 3, 2, 1, 0]
    print(countdown(8))  # -> [8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(countdown(-1))  # -> []

    print(add_commas(1245))  # -> '1,245'
    print(add_commas(123456789))  # -> '123,456,789'
    print(add_commas(1011))  # -> '1,011'

    print(stonks(1000, 10, 10))  # -> 2593
    print(stonks(100000, 12, 3))  # -> 140492

    print(quic_mafs(6, 19))  # -> [6, 7]
    print(quic_mafs(2, 1))  # -> [0, 1]
    print(quic_mafs(22, 5))  # -> [0, 1]
    print(quic_mafs(8796203, 7556))  # -> [1019,1442]

    print(sum_squares([1, 2, 3]))  # -> 14
    print(sum_squares([[1, 2], 3]))  # -> 14
    print(sum_squares([[[[[[[[[2]]]]]]]]]))  # -> 4
