# *
# **
# ***
# ****
from sys import stdout
rows = int(raw_input("Enter the number of rows:"))
print "First pattern:"
for i in range(0, rows):
    for j in range(0, i+1):
        stdout.write("* ")
    stdout.write("\n")
print "Second pattern:"
i1 = 3
i2 = 1
for i in range(0, rows):
    for j in range(0, i1):
        stdout.write(" ")
    for k in range(0, i2):
        stdout.write("* ")
    stdout.write("\n")
    i1 -= 1
    i2 += 1
print "Third pattern:"
i1 = 3
i2 = 1
for i in range(0, rows):
    for j in range(0, i1):
        stdout.write("  ")
    for k in range(0, i2):
        stdout.write("* ")
    stdout.write("\n")
    i1 -= 1
    i2 += 1
print "Fourth pattern:"
i1 = 0
i2 = 4
for i in range(0, rows):
    for j in range(0, i1):
        stdout.write("  ")
    for k in range(0, i2):
        stdout.write("* ")
    stdout.write("\n")
    i2 -= 1
    i1 += 1
print "Fifth pattern:"
i1 = 0
i2 = 4
for i in range(0, rows):
    for j in range(0, i1):
        stdout.write(" ")
    for k in range(0, i2):
        stdout.write("* ")
    stdout.write("\n")
    i2 -= 1
    i1 += 1
print "Sixth pattern:"
i4 = 3
i3 = 1
for i in range(0, rows-1):
    for j in range(0, i4):
        stdout.write("  ")
    for k in range(0, i3):
        stdout.write("*   ")
    stdout.write("\n")
    i3 += 1
    i4 -= 1
i1 = 0
i2 = 4
for i in range(0, rows):
    for j in range(0, i1):
        stdout.write("  ")
    for k in range(0, i2):
        stdout.write("*   ")
    stdout.write("\n")
    i2 -= 1
    i1 += 1
