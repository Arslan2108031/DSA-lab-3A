from flight_system import FlightSystem
from flight import Flight
from reservation import Reservation

def main():
    flight_system = FlightSystem()
    print("Welcome to Arslan Flight System!")
    flight_system.add_flight(Flight("B787", "Seoul", "Lahore", 5))
    flight_system.add_flight(Flight("A380", "Chicago", "Busan", 7))
    flight_system.add_flight(Flight("A350", "Tokyo", "NY", 10))  

    reservation_system = Reservation(flight_system)

    while True:
        print("\n MENU")
        print("1. View available flights")
        print("2. Reserve your comfort seat")
        print("3. View reservation queue")
        print("4. View confirmed reservations")
        print("5. Exit")

        choice = input("Please select an option (1-5): ").strip()

        if choice == "1":
            source = input("\nEnter departure city: ").strip()
            destination = input("Enter destination city: ").strip()
            flights = flight_system.search_flights(source, destination)
            flight_system.display_flights(flights)

        elif choice == "2":
            source = input("\nEnter departure city: ").strip()
            destination = input("Enter destination city: ").strip()
            passenger_name = input("Enter your name for the reservation: ").strip()
            if not reservation_system.request_reservation(passenger_name, source, destination):
                reservation_system.queue_reservation(passenger_name, source, destination)

        elif choice == "3":
            print("\nReservation Status:")


            print("\n1Queued Reservations:")
            if not reservation_system.reservation_queue:
                print("The reservation queue is empty.")
            else:
                for passenger in reservation_system.reservation_queue:
                    print(f"- {passenger[0]} (from {passenger[1]} to {passenger[2]})")

            print("\nConfirmed Reservations:")
            if not reservation_system.confirmed_reservations:
                print("No confirmed reservations.")
            else:
                for passenger_name, flight in reservation_system.confirmed_reservations:
                    print(f"- {passenger_name} (Flight {flight.flight_number}: {flight.source} → {flight.destination})")

        elif choice == "4":
            reservation_system.view_confirmed_reservations()

        elif choice == "5":
            print("\nThank you for using our system!")
            break

        else:
            print("\nInvalid choice! Please select a valid option (1-6).")

if __name__ == "__main__":
    main()
