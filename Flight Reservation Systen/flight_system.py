from flight import Flight

class FlightSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights(self, source, destination):
        result = []
        for flight in self.flights:
            if flight.source.lower() == source.lower() and flight.destination.lower() == destination.lower():
                result.append(flight)
        return result

    def display_flights(self, flights):
        if not flights:
            print("No flights available for the selected route.")
        else:
            for flight in flights:
                print(flight)
