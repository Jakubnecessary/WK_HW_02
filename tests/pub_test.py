import unittest
from src.pub import *
from src.customer import *

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Gig", 100)
        self.customer = Customer("Nathan", 100, 20)


    def test_pub_has_name(self):
        self.assertEqual("The Gig", self.pub.name)

    def test_pub_has_counter(self):
        self.assertEqual(100, self.pub.counter)

    def test_pub_increase_counter(self):
        self.pub.increase_counter(10)
        self.assertEqual(110, self.pub.counter)

    def test_pub_check_age(self):
        self.assertEqual(True, self.customer.check_age())