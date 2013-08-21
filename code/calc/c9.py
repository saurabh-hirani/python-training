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
    calc_output = []
    calc_cache = {}
    for calculation in calculations:
        calculation = calculation.strip()
        vals = [x for x in calculation.split() if x]
        num1, operation, num2 =  vals
        num1 = int(num1)
        num2 = int(num2)

        if not operation in calc_funcs.keys():
            errmsg = "invalid operation %s" % operation
            raise Exception(errmsg)

        if calculation in calc_cache:
            print "got cached result for %s" % calculation
            result = calc_cache[calculation]
        else:
            result = calc_funcs[operation](num1, num2)

        calc_output.append({'calculation': calculation, 'result': result})
        calc_cache[calculation] = result
    return calc_output

if __name__ == '__main__':
    results = do_calc(sys.argv[1]) # check
    for calc_hash in results:
        calculation = calc_hash['calculation']
        result = calc_hash['result']
        print calculation + ' = ' + str(result)
