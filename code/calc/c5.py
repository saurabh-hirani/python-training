import sys

def do_add(n1, n2):
    return n1 + n2

def do_mul(n1, n2):
    return n1 * n2

def do_div(n1, n2):
    if n2 == 0:
        errmsg = "invalid division by zero\n"
        sys.stderr.write(errmsg)
        raise Exception(errmsg)
    return float(n1) / n2

def do_calc(args):
    num1 = args[1]
    operation = args[2]
    num2 = args[3]
    
    num1 = int(num1)
    num2 = int(num2)
    
    if operation == '+':
        return do_add(num1, num2)
    elif operation == '*':
        return do_mul(num1, num2)
    elif operation == '/':
        return do_div(num1, num2)
    else:
        errmsg = "invalid operation %s" % operation
        raise Exception(errmsg)

if __name__ == '__main__':
    result = do_calc(sys.argv)
    print result
