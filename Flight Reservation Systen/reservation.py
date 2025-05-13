class Reservation:
    def __init__(self, flight_system):
        self.flight_system = flight_system
        self.reservation_queue = []
        self.confirmed_reservations = []

    def request_reservation(self, passenger_name, source, destination):
        flights = self.flight_system.search_flights(source, destination)
        for flight in flights:
            if flight.reserve_seat(passenger_name):
                self.confirmed_reservations.append((passenger_name, flight))
                print(f"Reservation confirmed for {passenger_name} on flight {flight.flight_number}.")
                return True
        print(f"⚠️ No available seats to confirm reservation for {passenger_name}.")
        return False


    def queue_reservation(self, passenger_name, source, destination):
        self.reservation_queue.append((passenger_name, source, destination))
        print(f"No seats available. {passenger_name} has been added to the reservation queue.")

    def process_queue(self):
        if not self.reservation_queue:
            print("No reservations in the queue to process.")
            return

        print("\nProcessing reservation queue...")
        still_queued = []

        for passenger_name, source, destination in self.reservation_queue:
            flights = self.flight_system.search_flights(source, destination)
            reserved = False
            for flight in flights:
                if flight.reserve_seat(passenger_name):
                    self.confirmed_reservations.append((passenger_name, flight))
                    print(f"Reservation confirmed for {passenger_name} on flight {flight.flight_number}.")
                    reserved = True
                    break
            if not reserved:
                print(f"Could not confirm reservation for {passenger_name} (no available seats).")
                still_queued.append((passenger_name, source, destination))

        self.reservation_queue = still_queued  


    def view_confirmed_reservations(self):
        if not self.confirmed_reservations:
            print("No confirmed reservations.")
        else:
            for passenger_name, flight in self.confirmed_reservations:
                print(f"{passenger_name} -> {flight.flight_number}: {flight.source} to {flight.destination}")
