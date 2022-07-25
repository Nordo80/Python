"""KT2."""


def sum_elements_around_last_three(nums: list) -> int:
    """Get list of dictionaries where key is hard-coded string."""
    count = 0
    a = 0
    counter = 0
    counter_new = 0
    for i in nums:
        if count == 1 and counter != 0:
            counter_new = counter + i
            count = 0
        if i == 3:
            count = 1
            counter = a
        a = i
    return counter_new


def has_seven(nums: list):
    """Get list of dictionaries where key is hard-coded string."""
    counter_seven = 0
    counter = 0
    counter_new = 0
    for a in nums:
        if counter_new == a:
            counter += 1
        counter_new = a
        if a == 7:
            counter_seven += 1
    if counter == 0 and counter_seven == 3:
        return True
    else:
        return False


def g_happy(s: str):
    """Get list of dictionaries where key is hard-coded string."""
    counter = 0
    counter_pairs = 0
    in_raw = 0
    naruto = 0
    for a in s:
        if a != "g" and in_raw == 1:
            in_raw = 0
            naruto += 1
        if counter == "g" and a == "g" and in_raw == 1:
            counter_pairs += 1
            in_raw = 0
        else:
            counter = a
            if counter == "g" and in_raw == 0:
                in_raw = 1

    if counter_pairs != 0 and naruto == 0:
        return True
    else:
        return False


class Book:
    """Book object."""

    def __init__(self, name: str, pages: int, publish_year: int):
        """Book constructor."""
        self.name = name
        self.publish_year = publish_year
        self.pages = pages


def shorten_book_names(books: list, length: int):
    """Get list of dictionaries where key is hard-coded string."""
    pass


def convert_to_list_of_dicts(books: list) -> list:
    """Get list of dictionaries where key is hard-coded string."""
    pass


def get_books_in_year(books: list, year: int) -> list:
    """Get list of dictionaries where key is hard-coded string."""
    result_list = []
    list_lst = [] + books
    for y in list_lst:
        if y.publish_year == year:
            result_list.append(y)
    return result_list


def sort_books(books: list) -> list:
    """Get list of dictionaries where key is hard-coded string."""
    pass


def sort_by_name_length(books: list) -> list:
    """Get list of dictionaries where key is hard-coded string."""
    pass


class Robot:
    """Robot."""

    def __init__(self, name: str):
        """Contstructor."""
        pass

    def get_name(self) -> str:
        """Return robot name."""
        pass

    def calculate_price(self) -> int:
        """Get list of dictionaries where key is hard-coded string."""
        pass

    def __repr__(self) -> str:
        """String representation of the robot."""
        pass


class Factory:
    """Factory."""

    def __init__(self, factory_id: str):
        """Constructor."""
        pass

    def get_robots_in_factory(self) -> list:
        """Return robots in the factory as a list."""
        pass

    def get_factory_id(self) -> str:
        """Return the factory id."""
        pass

    def add_robot(self, robot: Robot) -> Robot:
        """Get list of dictionaries where key is hard-coded string."""
        pass

    def generate_robot_factory_name(self) -> str:
        """Get list of dictionaries where key is hard-coded string."""
        pass

    def get_remaining_robot_names_count(self) -> int:
        """Get list of dictionaries where key is hard-coded string."""
        pass

    def make_robot(self) -> Robot:
        """Get list of dictionaries where key is hard-coded string."""
        pass

    def get_sorted_robots_in_factory(self) -> list:
        """Get robots in factory sorted by their price in non-decreasing order."""
        pass

    def get_highest_priced_robot_in_factory(self) -> Robot:
        """Get the highest priced robot within factory."""
        pass

    def __repr__(self) -> str:
        """String representation of the factory."""
        pass
