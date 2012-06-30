import unittest
from bfck import bfck

class TestEval(unittest.TestCase):
    def setUp(self):
        self.the_bfck_evaluator = bfck.Brainfuck()

    def test_plus_token(self):
        self.the_bfck_evaluator.eval('+')
        the_test_cell = self.the_bfck_evaluator.cell[0]
        self.assertEquals(the_test_cell, 1)

    def test_minus_token(self):
        self.the_bfck_evaluator.eval(['-', '-', '-'])
        the_test_cell = self.the_bfck_evaluator.cell[0]
        self.assertEquals(the_test_cell, -3)

    def test_shift_right(self):
        self.the_bfck_evaluator.eval(['>', '>'])
        self.assertEquals(len(self.the_bfck_evaluator.cell), 3)

    def test_left_shift(self):
        self.the_bfck_evaluator.eval(['>', '>', '<'])
        self.assertEquals(len(self.the_bfck_evaluator.cell), 2)
