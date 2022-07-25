"""ALAa."""


class Statistics:
    """lalala."""

    def __init__(self, filename):
        """Lilia, spasibo 4to tq est."""
        self.filename = filename
        dictionary = {}
        with open(filename, encoding="utf-8") as file:
            for i in file:
                splited = i.split(";")
                game_name = splited[0]
                dictionary[game_name] = [splited[2], splited[3].split(",")]

    def get(self, path: str):
        """S novqm godom."""
        self.path = path


class Player:
    """Lall."""

    def __init__(self, name: str):
        """
        Bank constructor.

        :param name: name of the bank
        """
        self.name = name

    def get_name(self):
        """Njam njam."""
        return self.name


class Game:
    """Lsldxld."""

    def __init__(self, name: str):
        """Njanja Harry Pothera."""
        self.name = name
        self.players = []

    def get_name(self):
        """Lalla."""
        return self.name
