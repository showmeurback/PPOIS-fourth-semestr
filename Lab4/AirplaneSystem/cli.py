from Source.airplane import Airplane
from Source.runway import Runway
from Source.passenger import Passenger
from Source.ticket import Ticket
from Source.crew import Crew
from Source.inflight_service import InflightService
from Source.flight_operations import FlightOperations


def main():
    airplanes = [Airplane("Boeing 737", 200)]
    runways = [Runway()]

    while True:
        print("\n=== Airline Management System (CLI) ===")
        print("1. List airplanes")
        print("2. Add passenger")
        print("3. Add crew")
        print("4. Take off")
        print("5. Land")
        print("6. Serve meal")
        print("7. Plan route")
        print("8. Save airplane state")
        print("9. Load airplane state")
        print("10. Occupy runway")
        print("11. Free runway")
        print("12. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            for i, airplane in enumerate(airplanes):
                print(
                    f"{i}: {airplane.model}, Status: {airplane.status}, Passengers: {len(airplane.passengers)}/{airplane.capacity}")

        elif choice == "2":
            airplane_idx = int(input("Enter airplane index: "))
            name = input("Enter passenger name: ")
            flight_number = input("Enter flight number: ")
            seat = input("Enter seat: ")
            ticket = Ticket(flight_number, seat)
            passenger = Passenger(name, ticket)
            airplanes[airplane_idx].add_passenger(passenger)

        elif choice == "3":
            airplane_idx = int(input("Enter airplane index: "))
            name = input("Enter crew name: ")
            role = input("Enter crew role: ")
            crew_member = Crew(name, role)
            airplanes[airplane_idx].add_crew(crew_member)

        elif choice == "4":
            airplane_idx = int(input("Enter airplane index: "))
            airplanes[airplane_idx].take_off()

        elif choice == "5":
            airplane_idx = int(input("Enter airplane index: "))
            airplanes[airplane_idx].land()

        elif choice == "6":
            InflightService.serve_meal()

        elif choice == "7":
            start = input("Enter start location: ")
            destination = input("Enter destination: ")
            FlightOperations.plan_route(start, destination)

        elif choice == "8":
            airplane_idx = int(input("Enter airplane index: "))
            filename = input("Enter filename to save: ")
            airplanes[airplane_idx].save_state(filename)

        elif choice == "9":
            filename = input("Enter filename to load: ")
            airplane = Airplane.load_state(filename)
            if airplane:
                airplanes.append(airplane)

        elif choice == "10":
            runway_idx = int(input("Enter runway index: "))
            runways[runway_idx].occupy()

        elif choice == "11":
            runway_idx = int(input("Enter runway index: "))
            runways[runway_idx].free()

        elif choice == "12":
            break


if __name__ == "__main__":
    main()12