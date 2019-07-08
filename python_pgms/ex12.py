def function1(*args):
    arg1,arg2=args
    print "Arg 1 is: %s, Arg 2 is: %s" %(arg1,arg2)
def function2(arg1,arg2):
    print "Arg 1 is: %s, Arg 2 is: %s" %(arg1,arg2)
def function3(arg1):
    print "Arg 1 is: %s" %arg1
def function4():
    print "nothin to print"

function1("preethi","avinash")
function2("preethi","avinash")
function3("preethi")
function4()