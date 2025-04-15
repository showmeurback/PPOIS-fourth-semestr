class Runway:
    def __init__(self):
        self.is_available = True

    def occupy(self):
        if self.is_available:
            self.is_available = False
            print("Runway is occupied.")
        else:
            print("Runway is already occupied.")

    def free(self):
        if not self.is_available:
            self.is_available = True
            print("Runway is now free.")
        else:
            print("Runway is already free.")