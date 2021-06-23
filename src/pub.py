class Pub:
    def __init__(self, name, counter):
        self.name = name
        self.counter = counter
        self.drinks = []
        # {
        #     "Beer": 3,
        #     "Absinth": 30,
        #     "Whiskey": 10
        # }
        

    def increase_counter(self, counter):
        self.counter += counter


    def check_age(self):
        if self.customer.age >= 18:
            return True


    # def find_drink_by_name(self, name):
    #     for drink in self.drinks:
    #         if drink.name == name:
    #             return drink


