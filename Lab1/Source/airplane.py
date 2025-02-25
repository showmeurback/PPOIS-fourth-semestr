from Source.passenger import Passenger
from Source.crew import Crew

class Airplane:
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity
        self.passengers = []
        self.crew = []
        self.status = "on_ground"  # on_ground или in_air

    def take_off(self):
        if self.status == "on_ground":
            print(f"{self.model} is taking off.")
            self.status = "in_air"
        else:
            print(f"{self.model} is already in the air.")

    def land(self):
        if self.status == "in_air":
            print(f"{self.model} is landing.")
            self.status = "on_ground"
        else:
            print(f"{self.model} is already on the ground.")

    def add_passenger(self, passenger: Passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"Passenger {passenger.name} has been registered on board.")
        else:
            print("The airplane is full. Registration is not possible.")

    def add_crew(self, crew_member: Crew):
        self.crew.append(crew_member)
        print(f"Crew member {crew_member.name} ({crew_member.role}) has been added.")