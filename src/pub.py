class Pub:
    def __init__(self, name, counter):
        self.name = name
        self.counter = counter
        self.drinks = []
        
    def increase_counter(self, amount):
        self.counter += amount


    def refuse_service(self, customer):
        if customer.drunkenness >= 100:
            return True
        else:
            return False

