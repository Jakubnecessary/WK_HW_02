class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def buy_drink(self, drink, pub):
        if self.check_age():
            self.reduce_wallet(drink.price)
            pub.increase_counter(drink.price)
            self.drunkenness += drink.alcohol_level

    def check_age(self):
        if self.age >= 18:
            return True

