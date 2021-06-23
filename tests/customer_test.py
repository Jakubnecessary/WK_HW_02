import unittest
from src.customer import *
from src.pub import *
from src.drink import *

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Nathan", 100, 20)
        self.drink = Drink("Absinth", 30, 80)
        self.pub = Pub("Starbar", 0)

    def test_customer_has_name(self):
        self.assertEqual("Nathan", self.customer.name)

    def test_customer_age(self):
        self.assertEqual(20, self.customer.age)

    def test_customer_reduce_wallet(self):
        self.customer.reduce_wallet(10)
        self.assertEqual(90, self.customer.wallet)

    def test_buy_drink(self):
        self.customer.reduce_wallet(self.drink.price)
        self.pub.increase_counter(self.drink.price)
        self.assertEqual(70, self.customer.wallet)
        self.assertEqual(30, self.pub.counter)
    

    def test_has_drunkness_level(self):
        self.assertEqual(0, self.customer.drunkenness)
