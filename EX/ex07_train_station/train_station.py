"""Train Station."""


class Passenger:
    """Description."""

    def __init__(self, passenger_id: str, seat: str):
        """Description."""
        self.passenger_id = passenger_id
        self._seat = seat

    @property
    def id(self) -> str:
        """Description."""
        return self.passenger_id

    @property
    def seat(self) -> str:
        """Description."""
        return self._seat


class Train:
    """Description."""

    def __init__(self, train_id: str, carriages: int, seats_in_carriage: int):
        """Description."""
        self._train_id = train_id
        self._carriages = carriages
        self._seats_in_carriage = seats_in_carriage
        self.passengers_data = {}

    @property
    def carriages(self) -> int:
        """Description."""
        return self._carriages

    @property
    def train_id(self) -> str:
        """Description."""
        return self._train_id

    @property
    def seats_in_carriage(self) -> int:
        """Description."""
        return self._seats_in_carriage

    @property
    def passengers(self) -> list:
        """Description."""
        list_passengers = []
        for key, carriage in self.passengers_data.items():
            for seat, passanger_obj in carriage.items():
                list_passengers.append(passanger_obj)
        return list_passengers

    def get_seats_in_train(self) -> int:
        """Description."""
        return self._seats_in_carriage * self._carriages

    def get_number_of_passengers(self) -> int:
        """Description."""
        return len(self.passengers)

    def get_passengers_in_carriages(self) -> dict:
        """Description."""
        result = {}
        for i in range(1, self.carriages + 1):
            result[str(i)] = []
            if i in self.passengers_data:
                for key, value in self.passengers_data[i].items():
                    result[str(i)].append(value)
        return result

    @train_id.setter
    def train_id(self, value: str):
        """Description."""
        self._train_id = value

    @carriages.setter
    def carriages(self, value: int):
        """Description."""
        self._carriages = value

    @seats_in_carriage.setter
    def seats_in_carriage(self, value: int):
        """Description."""
        self._seats_in_carriage = value

    def add_passenger(self, passenger: Passenger) -> Passenger:
        """Description."""
        splited_seat = passenger.seat.split("-")
        carriage_id = int(splited_seat[1])
        seat_id = int(splited_seat[2])
        if carriage_id > self.carriages or seat_id > self._seats_in_carriage or carriage_id <= 0 or seat_id <= 0:
            return None
        if self.train_id != splited_seat[0]:
            return None
        if carriage_id not in self.passengers_data:
            self.passengers_data[carriage_id] = {seat_id: passenger}
            return passenger
        else:
            if seat_id in self.passengers_data[carriage_id]:
                return None
            else:
                self.passengers_data[carriage_id].update({seat_id: passenger})
                return passenger


class TrainStation:
    """Description."""

    def __init__(self, trains: list, passengers: list):
        """Description."""
        self._passengers = []
        self._trains = []
        train_ids = {}
        for i in trains:
            train_ids.update({i.train_id: i})
        for p in passengers:
            splited_data = p.seat.split("-")
            if splited_data[0] in train_ids:
                result = train_ids[splited_data[0]].add_passenger(p)
                if result is not None:
                    self._passengers.append(p)
        for j, t in train_ids.items():
            self._trains.append(t)

    def get_station_overview(self) -> list:
        """Description."""
        list = []
        for i in self._trains:
            list.append({'train_id': i.train_id,
                         'carriages': i.carriages,
                         'seats': f"{len(i.passengers)}/{i.get_seats_in_train()}"})
        return list

    def get_number_of_passengers(self) -> int:
        """Description."""
        return len(self._passengers)

    @property
    def passengers(self) -> list:
        """Description."""
        return self._passengers

    @passengers.setter
    def passengers(self, value_list: list):
        """Description."""
        self._passengers = value_list

    @property
    def trains(self) -> list:
        """Description."""
        return self._trains

    @trains.setter
    def trains(self, value_list: list):
        """Description."""
        self._trains = value_list
