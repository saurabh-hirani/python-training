import sys

num1 = sys.argv[1]
operation = sys.argv[2]
num2 = sys.argv[3]

if operation == '+':
    print num1 + num2
elif operation == '*':
    print num1 * num2 
elif operation == '/':
    print num1 / num2 
else:
    print "invalid operation %s" % operation
    sys.exit(1)

sys.exit(0)

# call directly
# call with 1 + 1 
