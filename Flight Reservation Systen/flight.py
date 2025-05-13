class Flight:
    def __init__(self, flight_number, source, destination, seats_available):
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.seats_available = seats_available
        self.passengers = []

    def reserve_seat(self, passenger_name):
        if self.seats_available > 0:
            self.seats_available -= 1
            self.passengers.append(passenger_name)
            return True
        return False

    def __str__(self):
        return f"{self.flight_number}: {self.source} to {self.destination} - Seats Available: {self.seats_available}"
