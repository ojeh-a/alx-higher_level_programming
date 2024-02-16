#!/usr/bin/python3

import unittest
import calculator

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calculator.add(10, 5)
        self.assertEqual(result, 15)
