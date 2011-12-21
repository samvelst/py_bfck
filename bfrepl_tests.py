from nose.tools import *
from brainfuck import Brainfuck

def test_plus():
    bf = Brainfuck()
    bf.eval(['+', '+', '+'])
    assert_equal(bf.cell[0], 3)

def test_minus():
    bf = Brainfuck()
    bf.eval(['-', '-', '-'])
    assert_equal(bf.cell[0], -3)

def test_shift_right():
    bf = Brainfuck()
    bf.eval(['>', '>'])
    assert_equal(len(bf.cell), 3)

def test_shift_left():
    bf = Brainfuck()
    bf.eval(['>', '>', '<'])
    assert_equal(len(bf.cell), 2)

