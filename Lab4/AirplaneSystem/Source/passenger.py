from Source.ticket import Ticket

class Passenger:
    def __init__(self, name, ticket: Ticket):
        self.name = name
        self.ticket = ticket