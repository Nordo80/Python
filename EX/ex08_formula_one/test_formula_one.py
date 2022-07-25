"""Save the turtle graphic to file which can be opened with a image editor like GIMP."""

import pytest

from formula_one import Driver, Race, FormulaOne

file = "example.txt"
file2 = "dadwwd.txt"
r1 = Race(file)
f1 = FormulaOne("example.txt")
d1 = Driver("name", "team")
filename = "example.txt"


def test_extract_info():
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    lines = r1.file_data
    assert r1.extract_info(lines[0]) == {'Name': 'Mika Hakkinen', 'Team': 'Mclaren-Mercedes', 'Time': 79694, 'Diff': '',
                                         'Race': 1}


def test_get_results_by_race():
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    assert len(r1.get_results_by_race(1)) == 7


def test_filter_data_by_race():
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    assert r1.filter_data_by_race(3) == [
        {'Name': 'Mika Hakkinen', 'Team': 'Mclaren-Mercedes', 'Time': 78831, 'Diff': '', 'Race': 3},
        {'Name': 'David Coulthard', 'Team': 'Mclaren-Mercedes', 'Time': 80498, 'Diff': '', 'Race': 3},
        {'Name': 'Heinz-Harald Frentzen', 'Team': 'Jordan-Mugen-Honda', 'Time': 80251, 'Diff': '', 'Race': 3},
        {'Name': 'Jacques Villeneuve', 'Team': 'BAR-Honda', 'Time': 82018, 'Diff': '', 'Race': 3},
        {'Name': 'Jenson Button', 'Team': 'Williams-BMW', 'Time': 81899, 'Diff': '', 'Race': 3},
        {'Name': 'Mika Salo', 'Team': 'Sauber-Petronas', 'Time': 78907, 'Diff': '', 'Race': 3},
        {'Name': 'Pedro de la Rosa', 'Team': 'Arrows-Supertec', 'Time': 83315, 'Diff': '', 'Race': 3}]


def test_format_time():
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    assert Race.format_time("000000") == "0:00.000"
    assert Race.format_time("123456") == "2:03.456"


def test_calculate_time_difference():
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    assert Race.calculate_time_difference(67410, 71620) == "+0:04.210"


def test_write_race_results_to_file():
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    f1.write_race_results_to_file(1)
    f1.write_race_results_to_file(2)
    with open('results_for_race_1.txt', 'r') as file1:
        d = set(file1.readlines())
    with open('test_results_for_race_1.txt', 'r') as file2:
        e = set(file2.readlines())
    with open('results_for_race_2.txt', 'r') as file3:
        d2 = set(file3.readlines())
    with open('test_results_for_race_2.txt', 'r') as file4:
        e2 = set(file4.readlines())
    assert d == e
    assert d2 == e2


def test_write_race_results_to_csv():
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    f1.write_race_results_to_csv(1)
    f1.write_race_results_to_csv(2)
    f1.write_race_results_to_csv(3)
    with open('race_1_results.csv', 'r') as file1, open('race_1_results.csv', 'r') as file2:
        fil1 = file1.readlines()
        fil2 = file2.readlines()
    with open('race_2_results.csv', 'r') as file1, open('race_results.csv', 'r') as file2:
        filee1 = file1.readlines()
        filee2 = file2.readlines()
    with open('race_3_results.csv', 'r') as file1, open('race_3_results.csv', 'r') as file2:
        fileone = file1.readlines()
        filetwo = file2.readlines()

    assert fileone == filetwo
    assert fil1 == fil2
    assert filee1 == filee2


def test_get_results():
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    d1.add_result(1, 123)
    assert Driver.get_results(d1) == {1: 123}


def test_sort_data_by_time():
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    assert r1.sort_data_by_time(r1.get_results_by_race(2)) == [
        {'Name': 'David Coulthard', 'Team': 'Mclaren-Mercedes', 'Time': '1:17.522', 'Diff': '', 'Race': 2, 'Place': 1,
         'Points': 25},
        {'Name': 'Pedro de la Rosa', 'Team': 'Arrows-Supertec', 'Time': '1:19.061', 'Diff': '+0:01.539', 'Race': 2,
         'Place': 2, 'Points': 18},
        {'Name': 'Jenson Button', 'Team': 'Williams-BMW', 'Time': '1:19.459', 'Diff': '+0:01.937', 'Race': 2,
         'Place': 3, 'Points': 15},
        {'Name': 'Heinz-Harald Frentzen', 'Team': 'Jordan-Mugen-Honda', 'Time': '1:21.516', 'Diff': '+0:03.994',
         'Race': 2, 'Place': 4, 'Points': 12},
        {'Name': 'Mika Salo', 'Team': 'Sauber-Petronas', 'Time': '1:21.565', 'Diff': '+0:04.043', 'Race': 2, 'Place': 5,
         'Points': 10},
        {'Name': 'Jacques Villeneuve', 'Team': 'BAR-Honda', 'Time': '1:24.254', 'Diff': '+0:06.732', 'Race': 2,
         'Place': 6, 'Points': 8},
        {'Name': 'Mika Hakkinen', 'Team': 'Mclaren-Mercedes', 'Time': '1:24.981', 'Diff': '+0:07.459', 'Race': 2,
         'Place': 7, 'Points': 6}]


def test_filter_by_race_no_such_race():
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    assert r1.filter_data_by_race(5) == []


def test_set_points():
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    assert Driver.set_points(d1) is None


def test_write_championship_to_file():
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    assert FormulaOne.write_championship_to_file(f1) is None


def test_read_file_to_list():
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    try:
        Race("dwqqwd.txt")
        pytest.fail("Did not raise exception")

    except FileNotFoundError as e:
        assert str(e) == 'No file found!'
