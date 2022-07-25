"""KTs3."""


def only_one_pair(numbers: list) -> bool:
    """
    Whether the list only has one pair.

    Function returns True, if the list only has one pair (two elements have the same value).
    In other cases:
     there are no elements with the same value
     there are more than 2 elements with the same value
     there are several different pairs
    returns False.

    only_one_pair([1, 2, 3]) => False
    only_one_pair([1]) => False
    only_one_pair([1, 2, 3, 1]) => True
    only_one_pair([1, 2, 1, 3, 1]) => False
    """
    if len(numbers) - len(set(numbers)) == 1:
        return True
    else:
        return False


def odd_even_pairs(nums: list):
    """
    Given a list of integers, return the sum of all the odd pairs and even pairs in the list.

    A pair is considered two consecutive odd numbers or two consecutive even numbers.
    There can be any number of odd numbers between the pair even numbers and vice versa.
    If there are not enough odd and/or even numbers in the list to form a pair, or the list is empty, return -1.

    print(odd_even_pairs([1, 2, 3, 4, 5, 6, 7, 8]))  # 1 * 3 + 2 * 4 + 5 * 7 + 6 * 8 = 94
    print(odd_even_pairs([3, 2, 4, 1]))  # 3 * 1 + 2 * 4 = 11
    print(odd_even_pairs([4, 3, 5]))  # -1
    print(odd_even_pairs([-5, 2, 1, 1, 4, 1]))  # -5 * 1 + 2 * 4 + 1 * 1 = 4
    print(odd_even_pairs([3, 0, 1, -5]))  # -1

    :param nums: given list of integers
    :return: sum of pairs of odd and even numbers
    """
    trigger_a = 0
    trigger_b = 0
    a = 0
    ab1 = 0
    ab2 = 0
    if len(nums) % 2 == 0:
        for i in nums:
            if i % 2 == 0:
                if trigger_a == 0:
                    a = i
                    trigger_a = 1
                else:
                    ab1 = ab1 + (a * i)
                    trigger_a = 0

            else:
                if trigger_b == 0:
                    b = i
                    trigger_b = 1
                else:
                    ab2 = ab2 + (b * i)
                    trigger_b = 0
        return ab1 + ab2
    else:
        return -1


def pentabonacci(n: int) -> int:
    """
    Find the total number of odd values in the sequence up to the f(n) [included].

    The sequence is defined like this:
    f(0) = 0
    f(1) = 1
    f(2) = 1
    f(3) = 2
    f(4) = 4
    f(n) = f(n - 1) + f(n - 2) + f(n - 3) + f(n - 4) + f(n - 5)


    Keep in mind that 1 is the only value that is duplicated in the sequence
    and must be counted only once.

    pentabonacci(5) -> 1
    pentabonacci(10) -> 3
    pentabonacci(15) -> 5

    :param n: The last term to take into account.
    :return: Total number of odd values.
    """
    list_list = []
    list2 = [0, 1]
    if n == 0:
        return 0
    if n in {1, 2}:
        return 1
    while len(list2) <= n:
        list2.append(sum(list2[-5:]))
    for num in list2:
        if num % 2 == 1:
            list_list.append(n)
    result = len(list_list) - 1
    return result


class Account:
    """Represent a bank account."""

    def __init__(self, name, balance):
        """
        Class constructor. Each account has owner's name and starting balance.

        :param name: account owner name. String.
        :param balance: starting balance of account. Integer.
        """
        self._name = name
        self._balance = balance

    def get_balance(self):
        """
        Get account balance.

        :return: balance in double form
        """
        return self._balance

    def get_name(self):
        """
        Get account owner's name in uppercase.

        :return: owner name in string form
        """
        return self._name.upper()

    def withdraw(self, amount):
        """
        Withdraw money from account.

        :param amount: amount to withdraw from account, has to be positive
        and the balance can't go below 0.
        :return: amount withdrawn string
        """
        if amount >= 0:
            if self._balance - amount <= -1:
                result = f"Amount withdrawn: {self._balance}"
                self._balance = 0
                return result
            else:
                self._balance = self._balance - amount
                return f"Amount withdrawn: {amount}"
        return None

    def deposit(self, amount):
        """
        Deposit money to account.

        :param amount: amount to deposit to account, has to be positive
        :return: amount deposited string
        """
        if amount >= 0:
            self._balance = self._balance + amount
            return f"Amount deposited: {amount}"
        return None


class Song:
    """Song class."""

    def __init__(self, name: str, duration: str):
        """Constructor."""
        pass

    def get_name(self) -> str:
        """Return song name."""
        pass

    def display_song_info(self) -> str:
        """
        Display song information.

        Song information should be represented as "name - duration".
        """
        pass


class Album:
    """Album class."""

    def __init__(self, name: str, year: int, songs: list):
        """Constructor."""
        pass

    def get_name(self) -> str:
        """Return song name."""
        pass

    def get_album_length(self) -> str:
        """
        Calculate full album length.

        To get the album length you need to add the duration for every song. Additionally, there is a 2 second pause
        between every two songs, and 5 seconds at the start and end of the album. The result should be returned as
        "hh:mm:ss".
        """
        pass

    def display_album_info(self) -> str:
        """
        Display album information.

        First row has the album name with the release year in brackets. Example: "24K Magic (2016)".
        Every song is on a separate line and has an order number which you need to add. After the number and song title
        comes the song duration, separated with a dash from the title.

        Example:
        24K Magic (2016)
        1. 24K Magic - 3:46
        2. Chunky - 3:06
        ...
        """
        pass


class Artist:
    """Artist class."""

    def __init__(self, name: str, albums: list):
        """Constructor."""
        pass

    def get_name(self) -> str:
        """Return artist name."""
        pass

    def get_albums(self) -> list:
        """Return list of albums ordered alphabetically by title."""
        pass

    def get_songs(self) -> list:
        """
        Return list of all artist's songs ordered alphabetically by song name.

        This function returns a list of all songs by the artist, including songs on albums.
        Each song can be in the list only once.
        """
        pass

    def add_album(self, album: Album) -> Album:
        """Add album to the artist."""
        pass

    def display_artist_albums(self) -> str:
        """
        Display artist albums ordered by release year, starting from the latest.

        First row of the output is "artist_name discography" and second row is an empty line, followed by albums.
        It is recommended to use display_album_info() function here.

        The first line of each album is: "album_title (release_year)".
        Following lines are songs: "song_number. song_title - song_duration".
        Albums are separated by an empty row.

        Example:
        Bruno Mars discography

        24K Magic (2016)
        1. 24K Magic - 3:46
        2. Chunky - 3:06
        ...

        Unorthodox Jukebox (2012)
        1. "Young Girls" - 3:49
        2. "Locked Out of Heaven" - 3:53
        ...

        """
        pass
