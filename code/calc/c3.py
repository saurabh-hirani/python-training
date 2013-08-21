import sys

num1 = sys.argv[1]
operation = sys.argv[2]
num2 = sys.argv[3]

num1 = int(num1)
num2 = int(num2)

if operation == '+':
    print num1 + num2
elif operation == '*':
    print num1 * num2 
elif operation == '/':
    if num2 == 0:
        sys.stderr.write("invalid division by zero\n")
        sys.exit(1)
    print float(num1 / num2)
    print float(num1) / num2
else:
    print "invalid operation %s" % operation
    sys.exit(1)

sys.exit(0)

# call directly
# call with 2 + 2
# call with 2 '*' 33
# call with 2 / 0
# call with 4 / 3
# call with a + b
