import unittest
from Observer_practice import Observable

class Observer_test(unittest.TestCase):

    def setUp(self):
        self.Observer_test = Observable()

    def test_add_one_observer_populautes_array(self):
        
