vegatables=["beans","carrot","potato","chilly"]
fruits=["apple","mango"]
numb1=[1,3,4,5]
for i in vegatables:
    print "vegatable name is : %s" %i
for i in fruits:
    print "fruit name is: %s" %i
for i in numb1:
    print "number is: %d" %i
employee=[]
for i in range(0,3):
    cont=raw_input("> ")
    employee.append(cont)
for i in employee:
    print "employee is %s" %i