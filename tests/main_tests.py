from nose.tools import *
from bfck import __main__

def get_code_test():
    test_code = __main__.get_code('good.bf')
    assert_equal(test_code, ['+', '-', '<', '<'])

def is_valid_test():
    code = __main__.get_code('bad.bf')
    result = __main__.is_valid(code)
    assert_equal(result, False)

