from sys import stdout
print "Enter the number of fibonacci series:"
no = raw_input(">")
number = int(no)
a = 0
b = 1
print "Fibonacci series are:"
stdout.write("%d  %d  " % (a, b))
for i in range(2, number):
    c = a + b
    stdout.write("%d  " % c)
    a = b
    b = c
