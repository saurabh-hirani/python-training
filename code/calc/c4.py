import sys

def do_calc(args):
    num1 = args[1]
    operation = args[2]
    num2 = args[3]
    
    num1 = int(num1)
    num2 = int(num2)
    
    if operation == '+':
        return num1 + num2
    elif operation == '*':
        return num1 * num2 
    elif operation == '/':
        if num2 == 0:
            errmsg = "invalid division by zero\n"
            sys.stderr.write(errmsg)
            raise Exception(errmsg)
        return float(num1) / num2
    else:
        errmsg = "invalid operation %s" % operation
        raise Exception(errmsg)

if __name__ == '__main__':
    result = do_calc(sys.argv)
    print result
    

# call directly
# call with 2 + 2
# call with 2 '*' 33
# call with 2 / 0
# call with 4 / 3
# call with a + b
