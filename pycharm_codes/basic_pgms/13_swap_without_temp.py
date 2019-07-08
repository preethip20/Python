# swapping using function
from sys import stdout


def swap1(num1, num2):
    return num2, num1


print "Enter the first number:"
no1 = raw_input(">")
number1 = int(no1)
print "Enter the second number:"
no2 = raw_input(">")
number2 = int(no2)
number1, number2 = swap1(number1, number2)
print "Numbers after swapping:"
stdout.write("Value of first number is: %d\nValue of second number is: %d" % (number1, number2))
