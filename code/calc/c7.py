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

def do_calc(*args):
    calculations = args[0].split(',')
    calc_funcs = {
        '+': do_add,
        '*': do_mul,
        '/': do_div,
    }
    calc_output = {}
    for calculation in calculations:
        print "doing %s" % calculation
        num1, operation, num2 = calculation.split(' ')
        
        num1 = int(num1)
        num2 = int(num2)

        if not operation in calc_funcs.keys():
            errmsg = "invalid operation %s" % operation
            raise Exception(errmsg)
        
        result = calc_funcs[operation](num1, num2)
        calc_output[calculation] = result
    print calc_output
    return calc_output

if __name__ == '__main__':
    results = do_calc(sys.argv[1]) # check
    for calculation, result in results.items():
        print calculation + ' = ' + str(result)

# give space in calculations
# random order to results
