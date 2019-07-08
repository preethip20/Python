c = ''
while len(c) != 1:
    c = raw_input('Enter a single character :')
    if len(c) != 1:
        print "You need to enter a single character..."
print "Ascii of %c is %d" % (c, ord(c))
