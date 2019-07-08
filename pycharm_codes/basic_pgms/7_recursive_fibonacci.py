from sys import stdout


def fibo1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo1(n-1) + fibo1(n-2)


print "Enter the number of fibonacci series:"
no = raw_input(">")
number = int(no)
print "Fibonacci series are:"
for i in range(0, number):
    c = fibo1(i)
    stdout.write("%d  " % c)
