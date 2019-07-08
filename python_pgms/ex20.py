i=0
numbers=[]
while i<6:
    print "value of i is %d" %i
    numbers.append(i)
    print "numbers now:", numbers
    i=i+1
    print "value of changed i is: %d" %i
for num in numbers:
    print num