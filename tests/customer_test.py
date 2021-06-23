import unittest
from src.customer import *

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Nathan", 100)

    def test_customer_has_name(self):
        self.assertEqual("Nathan", self.customer.name)

    def test_customer_reduce_wallet(self):
        self.customer.reduce_wallet(10)
        self.assertEqual(90, self.customer.wallet)
