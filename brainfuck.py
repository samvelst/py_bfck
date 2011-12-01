# Brainfuck interpreter!


command = raw_input(">> ")
pointer = 0
register = [0 for x in xrange(32)]

while (command != "exit"):
    stack = list(command)

    for s in stack:
        if s == '.':
            print chr(register[pointer])
        if s == '+':
            register[pointer] += 1
        if s == '-':
            register[pointer] -= 1
        if s == ",":
            n = raw_input()
            register[pointer] = ord(str(n))


    print "=> [%d]" % register[pointer]
    command = raw_input(">> ")
