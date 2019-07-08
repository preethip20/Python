from sys import stdout
rows = int(raw_input("Enter the number of rows >"))
cols = int(raw_input("Enter the number of columns >"))
matrix = []
print "Enter the matrix elements:"
for i in range(rows):
    a = []
    for j in range(cols):
        a.append(int(raw_input(">")))
    matrix.append(a)
print "Matrix elements are:"
for i in range(rows):
    for j in range(cols):
        stdout.write("%d  " % matrix[i][j])
    stdout.write("\n")
