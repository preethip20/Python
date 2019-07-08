# to check whether string is palindrome
print "Enter the string:"
str1 = raw_input(">")
txt = str1[::-1]
print "The reverse of string is:"
print txt
if str1 == txt:
    print "String is palindrome"
else:
    print "String is not palindrome"
