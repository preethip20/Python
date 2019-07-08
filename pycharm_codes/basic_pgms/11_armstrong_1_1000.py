print "Armstrong numbers between 1 to 1000"
for i in range(1, 1000):
    no = i
    sum1 = 0
    while no != 0:
        rem = no % 10
        sum1 = sum1 + (rem * rem * rem)
        no = no / 10
    if i == sum1:
        print i

