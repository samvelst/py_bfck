# Brainfuck interpreter!

# Need to figure out how to make loops
# current idea is to put evaluation into a function
# and call it recursively when a [ pops up.
# The trick will be how to slice the instruction set
# the correct way as to not stop at [+[->] but instead 
# get [+[->]++] and then [->] within again recursively.


cmd = raw_input(">> ")
ptr = 0
byte = [0]


while (cmd != "exit"):
    stack = list(cmd)
    i = 0

    while i < len(stack):
        if stack[i] == '.':
            if 32 < byte[ptr] < 256:
                print chr(byte[ptr]),
            else:
                print "",

        if stack[i] == '+':
            byte[ptr] += 1

        if stack[i] == '-':
            byte[ptr] -= 1

        if stack[i] == ",":
            n = raw_input()[0]
            byte[ptr] = ord(str(n))

        if stack[i] == '>':
            if ptr == (len(byte) - 1):
                byte.append(0)
                ptr += 1
            else:
                ptr += 1

        if stack[i] == '<':
            if ptr == 0:
                print "RangeError: Data pointer out of range."
            elif byte[ptr] == 0 and ptr == (len(byte) - 1):
                byte.pop()
                ptr -= 1
            else:
                ptr -= 1


        i += 1


    print "\n=>",
    for n in xrange(len(byte)):
        on_ptr = "[%d]" % byte[n]
        non_ptr = "%d" % byte[n]
        if n == ptr:
            print on_ptr,
        else:
            print non_ptr,

    cmd = raw_input("\n>> ")
