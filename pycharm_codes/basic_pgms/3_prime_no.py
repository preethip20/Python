print "Enter the number:"
number = raw_input(">")
no = int(number)
for i in range(2, no-1):
    if no % i == 0:
        print "%d is not a prime number" % no
        exit(0)
print "%d is a prime number" % no


