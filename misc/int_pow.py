"""
 Different way to implement integer based power function
 See discussions here:
 http://stackoverflow.com/questions/101439/the-most-efficient-way-to-implement-an-integer-based-power-function-powint-int
"""

def pow_iter(base, exp):
    """
    Time:  O(n) the exp size
    Space: O(1) since use xrange
    """
    res = 1
    for i in xrange(exp):
        res = base * res
    return res

def pow_rec(base, exp):
    """
    Recurse by one

    Time:  O(exp)
           Similar to iteration, actual running time will be bigger since involves function call
    Space: O(exp)
           exp <= 1000 otherwise will exceed the maximum depth of recursive call
    """
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    return base * pow_rec(base, exp-1)

def pow_rec_2(base, exp):
    """ 
    Recurse by half
    x^n = x^(n/2) * x^(n/2) if n is even else x^n = x * x^(n/2) * x^(n/2)

    Time:  O(log(exp)) 
           Dominated by the depth of recursive tree, each level takes O(1) to compute
    Space: O(log(exp)) 
           used for recursive call stack
    """
    if exp == 0:
        return 1
    elif exp == 1:
        return base

    res = pow_rec_2(base, exp>>1)
    #if exp % 2 == 0:
    if (exp & 1 == 0): # if it is even
        return res * res
    else:
        return base * res * res

def pow_by_squaring(x, n):
    """
    Exponentiation by squaring
    Time:   O(logn)
    Space:  O(1)
    """
    res = 1
    while n:
        if (n & 1): # if it is odd
            # this will be at least executed once when n == 1
            res *= x
            print 'res * %d' % x
        print n
        n = n >> 1 # halve the exp
        x *= x     # ((x^2) ^2) ^2 ...
    return res

if __name__ == '__main__':
    import timeit
    def verbose(algname, size, secs, loops):
        print '%s exponent %d:' % (algname, size),
        print 'total %.3f sec in %d loops' % (secs, loops)

    #base, exp = 6, 900
    base, exp = 10, 50501
    loops, repts = 100, 3
    #print pow_iter(base, 9)
    #print pow_rec_2(base, 9)
    print pow_by_squaring(3, 6)

    # secs1 = timeit.timeit("pow_iter(%d,%d)" % (base,exp), setup="from __main__ import pow_iter", number=loops)
    #secs_r = timeit.timeit("pow_rec(%d,%d)" % (base,exp), setup="from __main__ import pow_rec", number=loops)
    # secs2 = timeit.timeit("pow_rec_2(%d,%d)" % (base,exp), setup="from __main__ import pow_rec_2", number=loops)
    # secs3 = timeit.timeit("pow_by_squaring(%d,%d)" % (base,exp), setup="from __main__ import pow_by_squaring", number=loops)
    # verbose('iteration', exp, secs1, loops)
    #verbose('recurse by one', exp, secs_r, loops)
    # verbose('recurse by half', exp, secs2, loops)
    # verbose('by squaring', exp, secs3, loops)


