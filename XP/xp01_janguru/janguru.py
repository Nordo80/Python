"""Ladla."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2) -> int:
    """Calculate the meeting position of 2 jangurus.

    @:param pos1: position of first janguru
    @:param jump_distance1: jump distance of first janguru
    @:param sleep1: sleep time of first janguru
    @:param pos2: position of second janguru
    @:param jump_distance2: jump distance of second janguru
    @:param sleep2: sleep time of second janguru

    @:return positions where jangurus first meet
    """
    counter1 = 0
    counter2 = 0
    sleep1 -= 1
    sleep2 -= 1
    pos1 += jump_distance1
    pos2 += jump_distance2
    naruto1 = 0
    naruto2 = 0
    for i in range(10000000):
        if pos1 == pos2:
            return pos1
        if sleep1 > naruto1:
            sleep1 -= 1
            counter1 += 1
        else:
            pos1 += jump_distance1
            sleep1 = counter1
            counter1 = 0

        if sleep2 > naruto2:
            sleep2 -= 1
            counter2 += 1
        else:
            pos2 += jump_distance2
            sleep2 = counter2
            counter2 = 0
    else:
        return -1


if __name__ == "__main__":
    print(meet_me(1, 2, 1, 2, 1, 1))
    print(meet_me(1, 2, 1, 2, 1, 1))
    print(meet_me(0, 2, 1, 2, 1, 1))
    print(meet_me(1, 1000000000000000000, 1, 1000000000000000000, 1, 2))
    print(meet_me(1, 6, 1, 14, 5, 1))
    print(meet_me(10, 7, 7, 5, 8, 6))
    print(meet_me(3, 5, 10, 4, 1, 2))
    print(meet_me(1, 3, 2, 1, 2, 1))
    print(meet_me(0, 15, 6, 5, 5, 3))
    print(meet_me(1, 2, 1, 2, 1, 1))
    print(meet_me(1, 2, 1, 2, 1, 1))
    print(meet_me(1, 2, 1, 2, 1, 1))
    print(meet_me(100000, 21, 2, 0, 11, 1))
    print(meet_me(0, 3, 1, 20000000, 2, 1))
    print(meet_me(4662, 94, 4611, 4978, 12, 3375))
    print(meet_me(3576, 73, 6152, 17230, 10, 3069))
    print(meet_me(9550, 34, 7262, 10874, 14, 3003))
    print(meet_me(15930, 69, 54, 926361, 55, 44))
    print(meet_me(46017, 333, 1084, 933597, 900, 5047))
    print(meet_me(931345, 7621, 6346, 80624, 7778, 6339))
