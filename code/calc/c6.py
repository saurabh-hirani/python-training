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

    calc_funcs = {
        '+': do_add,
        '*': do_mul,
        '/': do_div,
    }

    if not operation in calc_funcs.keys():
        errmsg = "invalid operation %s" % operation
        raise Exception(errmsg)
    return calc_funcs[operation](num1, num2)

if __name__ == '__main__':
    result = do_calc(sys.argv)
    print result
