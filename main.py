import bfck
from sys import argv

legal_tokens = ['+', '-', '.', ',', '<', '>', '[', ']']
allowed_tokens = [' ', '\n']

def extract_tokens_from(a_source_file):
    source_file = open(a_source_file, 'r')
    source_code = source_file.read()
    return [token for token in source_code if token not in allowed_tokens]

def tokens_are_valid(tokens):
    for token in tokens:
        if token not in legal_tokens:
            return False
    return True

def main():
    bfck_evaluator = bfck.Brainfuck()

    try:
        the_script = argv[1]

        if the_script.endswith('.bf'):
            tokens_from_script = extract_tokens_from(the_script)
            if tokens_are_valid(tokens_from_script):
                bfck_evaluator.eval(tokens_from_script)
                bfck_evaluator.show_output()
            else:
                print "Error: Invalid syntax in %s" % script 

    except IndexError:
        # If no script is given, run the REPL
        bfck_evaluator.run()

if __name__ == '__main__':
    main()
