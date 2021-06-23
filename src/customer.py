class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def buy_drink(self, drink):
        self.reduce_wallet(drink.price)
        self.pub.increase_counter(drink.price)

