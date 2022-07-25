"""Train."""


class Train:
    """Description."""

    def __init__(self, passengers: list, carriages: int, seats_in_carriage: int):
        """Description."""
        self._seats_in_carriage = seats_in_carriage
        self._carriages = carriages
        self._passengers = self.check_tickets(passengers)

    def check_tickets(self, passengers: list):
        """Description."""
        list_list = []
        for a in passengers:
            splited = a.seat.split("-")
            splited_carriage = int(splited[0])
            splited_seat = int(splited[-1])
            if splited_carriage <= self._carriages and splited_seat <= self._seats_in_carriage:
                list_list.append(a)
        return list_list

    @property
    def passengers(self) -> list:
        """Description."""
        return self._passengers

    @property
    def carriages(self) -> int:
        """Description."""
        return self._carriages

    @property
    def seats_in_carriage(self) -> int:
        """Description."""
        return self._seats_in_carriage

    def get_seats_in_train(self) -> int:
        """Description."""
        return self.carriages * self.seats_in_carriage

    def get_number_of_passengers(self) -> int:
        """Description."""
        return len(self._passengers)

    def get_passengers_in_carriages(self) -> dict:
        """Description 8=D."""
        dict_result = {}
        for a in range(1, self._carriages + 1):
            dict_result[str(a)] = []
        for i in self._passengers:
            splited_list = i.seat.split("-")
            if splited_list[0] in dict_result:
                dict_result[splited_list[0]].append(i.__correct_passenger__())
        return dict_result

    @passengers.setter
    def passengers(self, value_list: list):
        """Description."""
        self._passengers = value_list
        pass

    @carriages.setter
    def carriages(self, value: int):
        """Description."""
        self._carriages = value
        pass

    @seats_in_carriage.setter
    def seats_in_carriage(self, value: int):
        """Description."""
        self._seats_in_carriage = value
        pass


class Passenger:
    """Description."""

    def __init__(self, passenger_id: str, seat: str):
        """Description."""
        self._passenger_id = passenger_id
        self.seat = seat

    def __dict__(self):
        """Description."""
        return {"id": self._passenger_id, "seat": self.seat}

    def __correct_passenger__(self):
        """Description."""
        return {"id": self._passenger_id, "seat": self.seat.split("-")[-1]}
