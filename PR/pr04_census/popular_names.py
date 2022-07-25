"""Hellllo."""


def read_from_file() -> list:
    """
    Create the list of all the names.

    :return: list
    """
    names = []
    with open("popular_names.txt", encoding='utf-8') as file:
        for line in file:
            names.append(line.strip())
    return names


def to_dictionary(names: list) -> dict:
    """
    Make a dictionary from a list of names.

    :param names: list of all the names
    :return: dictionary {"name:sex": number}
    """
    dictionary = {}
    for word in names:
        if word in dictionary:
            dictionary[word] = dictionary[word] + 1
        else:
            dictionary[word] = 1
    return dictionary


def to_sex_dicts(names_dict: dict) -> tuple:
    """
    Divide the names by sex to 2 different dictionaries.

    :param names_dict: dictionary of names
    :return: two dictionaries {"name": number}, {"name": number}
    first one is male names, seconds is female names.
    """
    male_names = {(i.split(':'))[0]: names_dict.get(i) for i in names_dict.keys() if ':M' in i}
    female_names = {(i.split(':'))[0]: names_dict.get(i) for i in names_dict.keys() if ':F' in i}
    return male_names, female_names


def most_popular(names_dict: dict) -> str:
    """
    Find the most popular name in the dictionary.

    If the dictionary is empty, return "Empty dictionary."
    :param names_dict: dictionary of names (key is name, value is count)
    :return: string
    """
    if len(names_dict) == 0:
        return "Empty dictionary."
    max_val = max(names_dict.values())
    result = {k: v for k, v in names_dict.items() if v == max_val}
    return list(result.keys())[0]


def number_of_people(names_dict: dict) -> int:
    """
    Calculate the number of people in the dictionary.

    :param names_dict: dictionary of names (key is name, value is count)
    :return: int
    """
    counter_of_names = 0
    d_values = names_dict.values()
    for name in d_values:
        if name > 0:
            counter_of_names += name
        else:
            counter_of_names += 0
    return counter_of_names


def names_by_popularity(names_dict: dict) -> str:
    r"""
    Create a string used to print the names by popularity.

    Format:
        1. name: number of people + "\n"
        ...

    Example:
        1. Kati: 100
        2. Mati: 90
        3. Nati: 80
        ...

    :param names_dict: dictionary of the names (key is name, value is count)
    :return: string
    """
    result = ""
    i = 0
    sorter_list = sorted(names_dict.items(), key=lambda x: x[1], reverse=True)
    for name in sorter_list:
        i += 1
        result += f"{i}. {name[0]}: {name[1]}\n"
    return result


if __name__ == '__main__':
    example_names = ("Kati:F\n" * 1000 + "Mati:M\n" * 800 + "Mari:F\n" * 600 + "Tõnu:M\n" * 400).rstrip("\n").split(
        "\n")
    people = to_dictionary(example_names)
    print(people)  # -> {'Kati:F': 1000, 'Mati:M': 800, 'Mari:F': 600, 'Tõnu:M': 400}
    male_names, female_names = to_sex_dicts(people)
    print(male_names)  # -> {'Mati': 800, 'Tõnu': 400}
    print(female_names)  # -> {'Kati': 1000, 'Mari': 600}
    print(most_popular(male_names))  # -> "Mati"
    print(number_of_people(people))  # -> 2800
    print(names_by_popularity(male_names))  # ->   1. Mati: 800
