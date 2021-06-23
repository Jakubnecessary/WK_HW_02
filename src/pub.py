class Pub:
    def __init__(self, name, counter):
        self.name = name
        self.counter = counter
        self.drinks = []

    def increase_counter(self, counter):
        self.counter += counter
