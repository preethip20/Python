print "Enter the number:"
str1 = raw_input(">")
no1 = int(str1)
sum1 = 0
while no1 != 0:
    rem = no1 % 10
    sum1 = sum1 * 10 + rem
    no1 = no1 / 10
print sum1

