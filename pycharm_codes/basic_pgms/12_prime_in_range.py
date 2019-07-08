# prime numbers between 1 to 50
from sys import stdout
print "Enter the first range:"
no1 = raw_input(">")
range1 = int(no1)
print "Enter the second range:"
no2 = raw_input(">")
range2 = int(no2)
print "Prime numbers in range %d and %d are:" %(range1, range2)
for i in range(range1, range2):
    no = i
    count = 0
    for j in range(2, i-1):
        if no % j == 0:
            count += 1
    if count == 0:
        stdout.write("%d  " %no)


