"""EX05 - OEE."""

import csv


def read_production_data(filename: str) -> dict:
    """
    Open the file in the provided path, read in values and return them as a dictionary.

    where the key is the machine name and value is a list of integers for the production data for each shift.

    :param filename: string file path for the CSV file to be read
    :return: dictionary with the production data per machine
    """
    try:
        with open(filename) as file:
            file_list = file.readlines()
        dict = {}
        for line in file_list:
            line = line.replace("\n", "")
            splited_list = line.split(',')
            dict[splited_list[0]] = list(map(int, splited_list[1:]))

        return dict
    except FileNotFoundError:
        return {}


def calculate_quality(production_data: dict) -> dict:
    """
    Go through the input dictionary and for each machine, calculate the Quality percentage (as a float, e.g. 98.1).

    Save each value in a new dictionary, where the key is the machine name and value is the calculated Quality.
    Return the newly created dictionary.

    :param production_data: dictionary with production data
    :return: dictionary with OEE Quality value per machine
    """
    dict2 = {}
    for key, values in production_data.items():
        if values[2] != 0:
            dict2[key] = round((values[3] / values[2] * 100), 1)
        else:
            dict2[key] = round((values[3] * 100), 1)
    return dict2


def calculate_availability(production_data: dict) -> dict:
    """
    Go through the input dictionary and for each machine, calculate the Availability percentage (as a float, e.g. 98.1).

    Save each value in a new dictionary, where the key is the machine name and value is the calculated Availability.
    Return the newly created dictionary.

    :param production_data: dictionary with production data
    :return: dictionary with OEE Availability value per machine
    """
    dict2 = {}
    for key, values in production_data.items():
        dict2[key] = round(100 / 420 * values[0], 1)
    return dict2


def calculate_performance(production_data: dict) -> dict:
    """
    Go through the input dictionary and for each machine, calculate the Performance percentage (as a float, e.g. 98.1).

    Save each value in a new dictionary, where the key is the machine name and value is the calculated Performance.
    Return the newly created dictionary.

    :param production_data: dictionary with production data
    :return: dictionary with OEE Performance value per machine
    """
    dict2 = {}
    for key, values in production_data.items():
        if values[0] and values[1] != 0:
            dict2[key] = round((values[2] / (values[0] * values[1]) * 100), 1)
        else:
            dict2[key] = round((values[2] * 100), 1)
    return dict2


def add_values_in_dict(sample_dict, key, list_of_values):
    """
    Append multiple values to a key in the given dictionary.

    Dlsllslslssl.

    :return: dictionary with OEE percentage value per machine
    """
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict


def calculate_oee(production_data: dict) -> dict:
    """
    Using the previously defined functions, calculate the final OEE percentage for each machine.

    Save each value in a new dictionary, where the key is the machine name and value is the calculated Performance.
    Return the newly created dictionary.

    :return: dictionary with OEE percentage value per machine
    """
    dict_oee = {}
    dict_qual = calculate_quality(production_data)
    dict_perfom = calculate_performance(production_data)
    dict_avail = calculate_availability(production_data)
    for key, value in dict_avail.items():
        dict_oee.update({key: round((dict_perfom[key] * dict_qual[key] * value) / 10000, 1)})

    return dict_oee


def write_results_to_file(production_data: dict, filename: str):
    """
    Write the calculation results to a CSV formatted file.

    :param filename: string file path for the CSV file to be written to
    :param production_data: dictionary with production data
    """
    dict_oee = calculate_oee(production_data)
    dict_qual = calculate_quality(production_data)
    dict_perfom = calculate_performance(production_data)
    dict_avail = calculate_availability(production_data)
    with open(filename, mode='w') as csv_file:
        fieldnames = ["Liin", "Saadavus", "Tootlus", "Kvaliteet", "OEE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in production_data.items():
            writer.writerow(
                {"Liin": key, "Saadavus": dict_avail[key], "Tootlus": dict_perfom[key], "Kvaliteet": dict_qual[key],
                 "OEE": dict_oee[key]})
    return csv_file


if __name__ == '__main__':
    dic = read_production_data(r"C:\Users\Alina\PycharmProjects\iti0102-2020\EX\ex05_oee\reedzzzene_vahzetus.csv")
    prod_data = read_production_data("reedene_vsssahetus.csv")
    print('\n- Production data -')
    print('[Run Time (minutes), Ideal Run Rate (pcs/min), Total Count (pcs), Good Count (pcs)]')
    for key, value in prod_data.items():
        print(f"{key}: {value}")

    # Sildistaja: [358, 57, 18602, 18388]
    # Hapukurgipurgitaja: [415, 12, 4800, 2013]
    # Autoklaav: [450, 10, 4500, 4500]
    # Supivillija: [402, 36, 14230, 14214]
    # Makaronikeetja: [410, 25, 10230, 10230]
    # Kartulikoorija: [420, 111, 46620, 44123]
    # Mahlapress: [0, 0, 0, 0]

    quality_dict = calculate_quality(prod_data)
    print('\n- Quality calculation results -')
    for key, value in quality_dict.items():
        print(f"{key}: {value}")

    # Sildistaja: 98.8
    # Hapukurgipurgitaja: 41.9
    # Autoklaav: 100.0
    # Supivillija: 99.9
    # Makaronikeetja: 100.0
    # Kartulikoorija: 94.6
    # Mahlapress: 0.0

    availability_dict = calculate_availability(prod_data)
    print('\n- Availability calculation results -')
    for key, value in availability_dict.items():
        print(f"{key}: {value}")

    # Sildistaja: 85.2
    # Hapukurgipurgitaja: 98.8
    # Autoklaav: 107.1
    # Supivillija: 95.7
    # Makaronikeetja: 97.6
    # Kartulikoorija: 100.0
    # Mahlapress: 0.0

    performance_dict = calculate_performance(prod_data)
    print('\n- Performance calculation results -')
    for key, value in performance_dict.items():
        print(f"{key}: {value}")

    # Sildistaja: 91.2
    # Hapukurgipurgitaja: 96.4
    # Autoklaav: 100.0
    # Supivillija: 98.3
    # Makaronikeetja: 99.8
    # Kartulikoorija: 100.0
    # Mahlapress: 0.0

    oee_dict = calculate_oee(prod_data)
    print('\n- Total OEE calculation results -')
    for key, value in oee_dict.items():
        print(f"{key}: {value}")

    # Sildistaja: 76.8
    # Hapukurgipurgitaja: 39.9
    # Autoklaav: 107.1
    # Supivillija: 94.0
    # Makaronikeetja: 97.4
    # Kartulikoorija: 94.6
    # Mahlapress: 0.0

    write_results_to_file(prod_data, 'reedene_oee.csv')

    # contents of 'reedene_oee.csv':
    # Liin, Saadavus, Tootlus, Kvaliteet, OEE
    # Sildistaja, 85.2, 91.2, 98.8, 76.8
    # Hapukurgipurgitaja, 98.8, 96.4, 41.9, 39.9
    # Autoklaav, 107.1, 100.0, 100.0, 107.1
    # Supivillija, 95.7, 98.3, 99.9, 94.0
    # Makaronikeetja, 97.6, 99.8, 100.0, 97.4
    # Kartulikoorija, 100.0, 100.0, 94.6, 94.6
    # Mahlapress, 0.0, 0.0, 0.0, 0.0
