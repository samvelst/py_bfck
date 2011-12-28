import bfck
from sys import argv

legal = ['+', '-', '.', ',', '<', '>', '[', ']']
ok = [' ', '\n']

def get_code(s):
    f = open(s, 'r')
    code = f.read()
    return [t for t in code if t not in ok]


def is_valid(tokens):
    for t in tokens:
        if t not in legal:
            return False
    return True


def main():
    bfuck = bfck.Brainfuck()

    try:
        script = argv[1]

        if script.endswith('.bf'):
            tokens = get_code(script)
            if is_valid(tokens):
                bfuck.eval(tokens)
            else:
                print "Error: Invalid syntax in %s" % script 

    except IndexError:
        bfuck.run()


if __name__ == '__main__':
    main()
