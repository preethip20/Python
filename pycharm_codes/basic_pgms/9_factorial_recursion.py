def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


print "Enter the number:"
no = raw_input(">")
number = int(no)
fact1 = 0
print "Factorial of number is:"
for i in range(1, number+1):
    fact1 = fact(i)
print fact1
