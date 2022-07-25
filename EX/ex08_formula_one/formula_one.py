"""Formula One."""

import re
import csv
import os


class Driver:
    """Driver class."""

    def __init__(self, name: str, team: str):
        """
        Driver constructor.

        Here you should save driver's results as dictionary,
        where key is race number and value is points from that race.
        You must also save driver's points into a variable "points".

        :param name: Driver name
        :param team: Driver team
        """
        self._name = name
        self._team = team
        self._points = 0
        self._dict_results = {}

    def get_results(self) -> dict:
        """
        Get all driver's results.

        :return: Results as dictionary
        """
        return self._dict_results

    def get_points(self) -> int:
        """
        Return calculated driver points.

        :return: Calculated points
        """
        return self._points

    def get_name(self):
        """
        Return calculated driver points.

        :return: Calculated points
        """
        return self._name

    def get_team(self):
        """
        Return calculated driver points.

        :return: Calculated points
        """
        return self._team

    def set_points(self):
        """Set points for driver."""
        self._points = 0
        for a in self._dict_results.values():
            self._points += a

    def add_result(self, race_number: int, points: int):
        """
        Add new result to dictionary of results.

        Dictionary is located in the constructor.

        :param race_number: Race number
        :param points: Number of points from the race
        """
        self._dict_results[race_number] = points
        self.set_points()


class Race:
    """Race class."""

    def __init__(self, file):
        """
        Race constructor.

        Here you should keep data collected from file.
        You must read file rows to list.

        :param file: File with race data
        """
        self._file = file
        self.file_data = []
        self.read_file_to_list()
        self.number_races = int(self.file_data.pop(0))

    def get_remove_race(self):
        """
        Return calculated driver points.

        :return: Calculated points
        """
        return self.number_races

    def read_file_to_list(self):
        """
        Read file data to list in constructor.

        First line shows number of races in data file.
        Rest of the data follows same rules. Each line consists of 'Driver Team Time Race'.
        There are 2 or more spaces between each 'category'.
        E.g. "Mika Häkkinen  McLaren-Mercedes      42069   3"

        If file does NOT exist, throw FileNotFoundError with message "No file found!".
        """
        if os.path.isfile(self._file):
            with open(self._file) as file:
                lines = file.read().splitlines()
            for i in lines:
                self.file_data.append(i)
        else:
            raise FileNotFoundError("No file found!")

    @staticmethod
    def extract_info(line: str) -> dict:
        """
        Helper method for read_file_to_list.

        Here you should convert one data line to dictionary.
        Dictionary must contain following key-value pairs:
            'Name': driver's name as string
            'Team': driver's team as string
            'Time': driver's time as integer (time is always in milliseconds)
            'Diff': empty string
            'Race': race number as integer

        :param line: Data string
        :return: Converted dictionary
        """
        splited_line = re.split(r"\s\s+", line)
        dictionary1 = {"Name": splited_line[0], "Team": splited_line[1], "Time": int(splited_line[2]), "Diff": "",
                       "Race": int(splited_line[3])}
        return dictionary1

    def filter_data_by_race(self, race_number: int) -> list:
        """
        Filter data by race number.

        :param race_number: Race number
        :return: Filtered race data
        """
        new_list = []
        for a in self.file_data:
            dictionary_line = self.extract_info(a)
            if dictionary_line["Race"] == race_number:
                new_list.append(dictionary_line)
        return new_list

    @staticmethod
    def format_time(time: str) -> str:
        """
        Format time from milliseconds to M:SS.SSS.

        format_time('12') -> 0:00.012
        format_time('1234') -> 0:01.234
        format_time('71620') -> 1:11.620

        :param time: Time in milliseconds
        :return: Time as M:SS.SSS string
        """
        new_string = ""
        ak = time.zfill(6)
        counter = 0
        for a in ak:
            new_string += a
            counter += 1
            if counter == 1:
                new_string = new_string + ":"
            elif counter == 3:
                new_string += "."
        mjau = int(new_string[0] + new_string[2])
        if mjau >= 6:
            lala = str(mjau / 6)
            aba = mjau % 6
            naruto = str(aba) + str(new_string[3])
            if int(naruto) >= 10:
                aff = lala[0] + new_string[1] + naruto + new_string[4] + new_string[5] + new_string[6] + new_string[7]
                return aff
            else:
                aff = lala[0] + new_string[1] + naruto + new_string[4] + new_string[5] + new_string[6] + \
                    new_string[7]
                return aff
        else:
            return new_string

    @staticmethod
    def calculate_time_difference(first_time: int, second_time: int) -> str:
        """
        Calculate difference between two times.

        First time is always smaller than second time. Both times are in milliseconds.
        You have to return difference in format +M:SS.SSS

        calculate_time_difference(4201, 57411) -> +0:53.210

        :param first_time: First time in milliseconds
        :param second_time: Second time in milliseconds
        :return: Time difference as +M:SS.SSS string
        """
        plus_time = "+" + Race.format_time(str(second_time - first_time))
        return plus_time

    @staticmethod
    def sort_data_by_time(results: list) -> list:
        """
        Sort results data list of dictionaries by 'Time'.

        :param results: List of dictionaries
        :return: Sorted list of dictionaries
        """
        return sorted(results, key=lambda x: x["Time"])

    def get_results_by_race(self, race_number: int) -> list:
        """
        Final results by race number.

        This method combines the rest of the methods.
        You have to filter data by race number and sort them by time.
        You must also fill 'Diff' as time difference with first position.
        You must add 'Place' and 'Points' key-value pairs for each dictionary.

        :param race_number: Race number for filtering
        :return: Final dictionary with complete data
        """
        points = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
        dictionary_line = self.filter_data_by_race(race_number)
        list_sorted_data = self.sort_data_by_time(dictionary_line)
        first_time = 0
        place = 1
        for dictionary in list_sorted_data:
            if place == 1:
                first_time = dictionary["Time"]
            else:
                dictionary["Diff"] = self.calculate_time_difference(first_time, dictionary["Time"])
            dictionary["Place"] = place
            if place <= 10:
                point = points[place - 1]
                if place == 1:
                    first_time = dictionary["Time"]
            else:
                point = 0
            dictionary["Time"] = self.format_time(str(dictionary["Time"]))
            dictionary["Points"] = point
            place += 1
        return list_sorted_data


class FormulaOne:
    """FormulaOne class."""

    def __init__(self, file):
        """
        FormulaOne constructor.

        It is reasonable to create Race instance here to collect all data from file.

        :param file: File with race data
        """
        self._file = file
        self._race = Race(file)

    def write_race_results_to_file(self, race_number: int):
        """
        Write one race results to a file.

        File name is 'results_for_race_{race_number}.txt'.
        Exact specifications are described in the text.

        :param race_number: Race to write to file
        """
        dict_race = self._race.get_results_by_race(race_number)
        headers = ["PLACE", "NAME", "TEAM", "TIME", "DIFF", "POINTS"]
        numbers = [10, 25, 25, 15, 15, 6]
        f = open("results_for_race_" + str(race_number) + ".txt", "w+")
        counter1 = 0
        headers_string = ""
        divider_string = ""
        for i in headers:
            headers_string += self.fixed_string(i, numbers[counter1])
            divider_string += self.divider(numbers[counter1])
            counter1 += 1
        f.write(headers_string + "\n" + divider_string + "\n")
        for v in dict_race:
            f.write(self.fixed_string(str(v["Place"]), numbers[0])
                    + self.fixed_string(v["Name"], numbers[1])
                    + self.fixed_string(v["Team"], numbers[2])
                    + self.fixed_string(v["Time"], numbers[3])
                    + self.fixed_string(str(v["Diff"]), numbers[4])
                    + self.fixed_string(str(v["Points"]), numbers[5]) + "\n")

    def write_race_results_to_csv(self, race_number: int):
        """
        Write one race results to a csv file.

        File name is 'race_{race_number}_results.csv'.

        :param race_number: Race to write to file
        """
        headers = ["Place", "Name", "Team", "Time", "Diff", "Points", "Race"]
        with open('race_' + str(race_number) + '_results.csv', 'w', newline="") as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerow(headers)
            dict_race = self._race.get_results_by_race(race_number)
            for v in dict_race:
                filewriter.writerow([v["Place"], v["Name"], v["Team"], v["Time"], v["Diff"], v["Points"], race_number])

    def fixed_string(self, word: str, n: int) -> str:
        """
        Return calculated driver points.

        :return: Calculated points
        """
        result = word
        while len(result) < n:
            result += " "
        return result

    def divider(self, n: int) -> str:
        """
        Return calculated driver points.

        :return: Calculated points
        """
        result = ""
        while len(result) < n:
            result += "-"
        return result

    def write_championship_to_file(self):
        """
        Write championship results to file.

        It is reasonable to create Driver class instance for each unique driver name and collect their points
        using methods from Driver class.
        Exact specifications are described in the text.
        """
        drivers_dictionary = {}
        for num_of_race in range(1, self._race.get_remove_race() + 1):
            for dictionary in self._race.get_results_by_race(num_of_race):
                name = dictionary["Name"]
                race = dictionary["Race"]
                points = dictionary["Points"]
                if name in drivers_dictionary.keys():
                    drivers_dictionary[name].add_result(race, points)
                else:
                    drivers_dictionary[name] = Driver(name, dictionary['Team'])
                    drivers_dictionary[name].add_result(race, points)
        headers = ["PLACE", "NAME", "TEAM", "POINTS"]
        numbers = [10, 25, 25, 6]
        f = open("championship_results.txt", "w+")
        counter1 = 0
        headers_string = ""
        divider_string = ""
        for i in headers:
            headers_string += self.fixed_string(i, numbers[counter1])
            divider_string += self.divider(numbers[counter1])
            counter1 += 1
        f.write(headers_string + "\n" + divider_string + "\n")
        sorted_dict = sorted(drivers_dictionary.items(), key=lambda x: x[1].get_points(), reverse=True)
        place = 1
        for v in sorted_dict:
            f.write(self.fixed_string(str(place), numbers[0])
                    + self.fixed_string(v[1].get_name(), numbers[1])
                    + self.fixed_string(v[1].get_team(), numbers[2])
                    + self.fixed_string(str(v[1].get_points()), numbers[3]) + "\n")
            place += 1
        f.close()
