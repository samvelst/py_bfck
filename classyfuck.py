#!/usr/bin/env python

class Brainfuck(object):
    """ A Brainfuck repl """

    def __init__(self):
        """ Creates an initial cell and a pointer to that cell """
        self.ptr = 0
        self.cell = [0]

    def eval(self, tokens):
        """ Evaluate the tokens of the program """
        i = 0

        while i < len(tokens):
            if tokens[i] == '+':
                self.cell[self.ptr] += 1 

            if tokens[i] == '-':
                self.cell[self.ptr] -= 1

            if tokens[i] == '.':
                if 32 < self.cell[self.ptr] < 256:
                     print chr(self.cell[self.ptr]),
                else:
                    print "",

                if i == (len(tokens) - 1):
                    print ""

            if tokens[i] == ',':
                n = raw_input()[0]
                self.cell[self.ptr] = ord(str(n))

            if tokens[i] == '>':
                if self.ptr == (len(self.cell) - 1):
                    self.cell.append(0)
                self.ptr += 1

            if tokens[i] == '<':
                if self.ptr == 0:
                    print "RangeError: Data pointer out of range."
                elif self.cell[self.ptr] == 0 and \
                        self.ptr == (len(self.cell) -1):
                    self.cell.pop()
                    self.ptr -= 1
                else:
                    self.ptr -= 1

            if tokens[i] == '[':
                pass    
            
            i += 1

        print "=>",
        for n in xrange(len(self.cell)):
            on_ptr = "[%d]" % self.cell[n]
            non_ptr = "%d" % self.cell[n]
            if n == self.ptr:
                print on_ptr,
            else:
                print non_ptr,

    def run(self):
        """ Run the repl """
        inp = raw_input("BF> ")

        while (inp != "exit"):
            tokens = list(inp)
            self.eval(tokens)
            inp = raw_input("\nBF> ")


repl = Brainfuck()

if __name__ == "__main__":
    repl.run()