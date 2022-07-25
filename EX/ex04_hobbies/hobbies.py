"""Hobbiexs."""
import csv
import re


def create_list_from_file(file):
    """
    Collect lines from given file into list.

    :param file: original file path
    :return: list of lines
    """
    with open(file) as file:
        file_list = file.readlines()
    return file_list


def create_dictionary(file):
    """
    Create dictionary about given peoples' hobbies as Name: [hobby_1, hobby_2].

    :param file: original file path
    :return: dict
    """
    file_list = set(create_list_from_file(file))
    dictionary = dict()
    pattern = r"(\w*):(\w*)"
    for element in file_list:
        match = re.search(pattern, element)
        name = match.group(1)
        hobby = match.group(2)
        dictionary.setdefault(name, []).append(hobby)
        if hobby not in dictionary[name]:
            dictionary[name].append(hobby)
    return dictionary


def find_person_with_most_hobbies(file):
    """
    Find the person (or people) who have more hobbies than others.

    :param file: original file path
    :return: list
    """
    dictionary = create_dictionary(file)
    names_most_hobbies = list()
    most_hobbies = len(max(dictionary.values(), key=len))
    for key, value in dictionary.items():
        if most_hobbies == len(value):
            names_most_hobbies.append(key)
    return names_most_hobbies


def find_person_with_least_hobbies(file):
    """
    Find the person (or people) who have less hobbies than others.

    :param file: original file path
    :return: list
    """
    dictionary = create_dictionary(file)
    names_least_hobbies = list()
    least_hobbies = len(min(dictionary.values(), key=len))
    for key, value in dictionary.items():
        if least_hobbies == len(value):
            names_least_hobbies.append(key)
    return names_least_hobbies


def find_most_popular_hobby(file):
    """
    Find the most popular hobby.

    :param file: original file path
    :return: list
    """
    dictionary = create_dictionary(file)
    value_dictionary = dict()
    value_list = []
    for i in dictionary.values():
        value_list += i
    for hobby in set(value_list):
        value_dictionary.setdefault(value_list.count(hobby), []).append(hobby)
    return value_dictionary[max(value_dictionary)]


def find_least_popular_hobby(file):
    """
    Find the least popular hobby.

    :param file: original file path
    :return: list
    """
    dictionary = create_dictionary(file)
    value_dictionary = dict()
    value_list = []
    for i in dictionary.values():
        value_list += i
    for hobby in value_list:
        value_dictionary.setdefault(value_list.count(hobby), []).append(hobby)
    return value_dictionary[min(value_dictionary)]


def to_sort_dict(dictionary: dict):
    """
    Sort dictionary.

    :param dict:
    :return: sorted dict
    """
    sorted_dictionary = dict()
    sorted_keys = sorted(dictionary.keys())
    for word in sorted_keys:
        sorted_dictionary[word] = sorted(dictionary[word])
    return sorted_dictionary


def write_corrected_database(file, file_to_write):
    """
    Write .csv file in a proper way. Use collected and structured data.

    :param file: original file path
    :param file_to_write: file to write result
    """
    dictionary = to_sort_dict(create_dictionary(file))
    with open(file_to_write, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        name = "Name"
        hobbies = "Hobbies"
        writer.writerow([name, hobbies])
        for key, value in dictionary.items():
            writer.writerow([key, "-".join(value)])


if __name__ == '__main__':
    dic = create_dictionary("hobbies_database.txt")
    print(len(create_list_from_file("hobbies_database.txt")))  # -> 100
    print("Check presence of hobbies for chosen person:")
    print("shopping" in dic["Wendy"])  # -> True
    print("fitness" in dic["Sophie"])  # -> False
    print("gaming" in dic["Peter"])  # -> True
    print("Check if hobbies - person relation is correct:")
    print("Check if a person(people) with the biggest amount of hobbies is(are) correct:")
    print(find_person_with_most_hobbies("hobbies_database.txt"))  # -> ['Jack']
    print(len(dic["Jack"]))  # ->  12
    print(len(dic["Carmen"]))  # -> 10
    print("Check if a person(people) with the smallest amount of hobbies is(are) correct:")
    print(find_person_with_least_hobbies("hobbies_database.txt"))  # -> ['Molly']
    print(len(dic["Molly"]))  # -> 5
    print(len(dic["Sophie"]))  # -> 7
    print("Check if the most popular hobby(ies) is(are) correct")
    print(find_most_popular_hobby("hobbies_database.txt"))  # -> ['gaming', 'sport', 'football']
    print("Check if the least popular hobby(ies) is(are) correct")
    print(find_least_popular_hobby("hobbies_database.txt"))  # -> ['tennis', 'dance', 'puzzles', 'flowers']
    write_corrected_database("hobbies_database.txt", 'correct_hobbies_database.csv')
