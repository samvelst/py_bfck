# Brainfuck interpreter!


cmd = raw_input(">> ")
ptr = 0
byte = [0]


while (cmd != "exit"):
    stack = list(cmd)

    for s in stack:
        if s == '.':
            print chr(byte[ptr])
        if s == '+':
            byte[ptr] += 1
        if s == '-':
            byte[ptr] -= 1
        if s == ",":
            n = raw_input()
            byte[ptr] = ord(str(n))

        if s == '>':
            byte.append(0)
            ptr += 1


    print "=>",
    for n in xrange(len(byte)):
        if n == ptr:
            print "[", byte[n], "]",
        else:
            print "", byte[n], "",

    cmd = raw_input("\n>> ")
