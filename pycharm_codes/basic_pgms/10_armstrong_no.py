print "Enter the number:"
number = raw_input(">")
no1 = int(number)
sum1 = 0
temp = no1
for i in range(0, no1-1):
    rem = no1 % 10
    sum1 = sum1 + (rem * rem * rem)
    no1 = no1 / 10
if temp == sum1:
    print "%d is a armstrong number" % temp
else:
    print "%d is not a armstrong number" % temp
