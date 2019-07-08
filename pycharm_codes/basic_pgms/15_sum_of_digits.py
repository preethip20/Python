print "Enter a number:"
no = raw_input(">")
no1 = int(no)
sum1 = 0
while no1 != 0:
    rem = no1 % 10
    sum1 = sum1 + rem
    no1 = no1 / 10
print "Sum of digits of entered number is: %d" % sum1
