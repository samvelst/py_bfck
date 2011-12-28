from nose.tools import *
from bfck import bfck

def test_plus():
    bf = bfck.Brainfuck()
    bf.eval(['+', '+', '+'])
    assert_equal(bf.cell[0], 3)

def test_minus():
    bf = bfck.Brainfuck()
    bf.eval(['-', '-', '-'])
    assert_equal(bf.cell[0], -3)

def test_shift_right():
    bf = bfck.Brainfuck()
    bf.eval(['>', '>'])
    assert_equal(len(bf.cell), 3)

def test_shift_left():
    bf = bfck.Brainfuck()
    bf.eval(['>', '>', '<'])
    assert_equal(len(bf.cell), 2)

