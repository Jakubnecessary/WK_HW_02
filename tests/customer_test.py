import unittest
from src.customer import *
from src.pub import *
from src.drink import *

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Nathan", 100)
        self.drink = Drink("Absinth", 30)
        self.pub = Pub("Starbar", 0)

    def test_customer_has_name(self):
        self.assertEqual("Nathan", self.customer.name)

    def test_customer_reduce_wallet(self):
        self.customer.reduce_wallet(10)
        self.assertEqual(90, self.customer.wallet)

    def test_buy_drink(self):
        self.customer.reduce_wallet(self.drink.price)
        self.pub.increase_counter(self.drink.price)
        self.assertEqual(70, self.customer.wallet)
