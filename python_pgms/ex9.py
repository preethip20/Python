from sys import argv
script,filename=argv
print "if you want to truncate the file enter return"
print "if you dont want to truncate the file click on control c"
print "the filename is %s" %filename
print "truncating the file"
file1=open(filename,'w')
file1.truncate()
print "Adding new content to file"
line1=raw_input(">")
line2="how"
line3="are u"
file1.write(line1)
file1.write("\n")
file1.write(line2)
file1.write("\n")
file1.write(line3)
file1=open(filename)
print file1.read()
file1.close()
