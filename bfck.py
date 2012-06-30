#!/usr/bin/env python

class Brainfuck(object):
    def __init__(self):
        self.pointer = 0
        self.cell = [0]
        self.output = []

    def eval(self, tokens):
        i = 0
        while i < len(tokens):
            if tokens[i] == '+':
                self.cell[self.pointer] += 1 

            if tokens[i] == '-':
                self.cell[self.pointer] -= 1

            if tokens[i] == '.':
                if self.cell[self.pointer] < 256:
                     self.output.append(chr(self.cell[self.pointer]))
                else:
                     self.output.append("")

                if i == (len(tokens) - 1):
                    print ""

            if tokens[i] == ',':
                n = raw_input()[0]
                self.cell[self.pointer] = ord(str(n))

            if tokens[i] == '>':
                if self.pointer == (len(self.cell) - 1):
                    self.cell.append(0)
                self.pointer += 1

            if tokens[i] == '<':
                if self.pointer == 0:
                    print "RangeError: Data pointer out of range."
                elif self.cell[self.pointer] == 0 and \
                        self.pointer == (len(self.cell) -1):
                    self.cell.pop()
                    self.pointer -= 1
                else:
                    self.pointer -= 1

            if tokens[i] == '[':
                go = 1
                sub_tokens = []
                tokens.pop(i)

                while go != 0:
                    if tokens[i] == '[':
                        go += 1
                    elif tokens[i] == ']':
                        go -= 1
                    sub_tokens.append(tokens.pop(i))

                sub_tokens.pop()

                while self.cell[self.pointer] != 0:
                    self.eval(sub_tokens)
                i -= 1
            i += 1

    def show_output(self):
        print ''.join(self.output)
        self.output = []

    def run(self):
        the_input = raw_input("BF> ")

        while (the_input != "exit"):
            tokens = list(the_input)
            self.eval(tokens)

            if len(self.output) > 0:
                self.show_output

            print "=>",
            for n in xrange(len(self.cell)):
                on_pointer = "[%d]" % self.cell[n]
                non_pointer = "%d" % self.cell[n]
                if n == self.pointer:
                    print on_pointer,
                else:
                    print non_pointer,

            the_input = raw_input("\nBF> ")
