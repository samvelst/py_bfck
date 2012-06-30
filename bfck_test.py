import bfck
import unittest

class TestEval(unittest.TestCase):
    def setUp(self):
        the_bfck_evaluator = bfck.Brainfuck()

    def test_plus_token(self):
        the_bfck_evaluator.eval('+')
        the_test_cell = the_bfck_evaluator.cell[0]
        assertEqual(the_test_cell, 1)
