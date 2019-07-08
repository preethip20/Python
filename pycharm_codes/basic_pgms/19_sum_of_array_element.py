from sys import stdout
no = int(raw_input("Enter the number of array elements :"))
print "Enter the array elements"
arr1 = []
for i in range(0, no):
    arr1.append(int(raw_input(">")))
print "The array elements are:"
for i in range(0, no):
    stdout.write("%d  " % arr1[i])
print "\nReverse of the array:"
rev = arr1[::-1]
print rev
print "Sum of array elements:"
sum1 = 0
for i in range(0, no):
    sum1 = sum1 + arr1[i]
print sum1
