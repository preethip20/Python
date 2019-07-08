print "Enter the number:"
no = raw_input(">")
number = int(no)
fact = 1
print "Factorial of number is:"
for i in range(1, number+1):
    fact = fact * i
print fact
