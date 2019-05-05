def romanToInt(A):
    rule = {
      'I': {step:1, jump: ['V', 'X'], m:'V', r:'X'},
      'V': {step:5, jump: []},
      'X': {step:10,jump: ['L', 'C'], m:'L', r:'C'},
      'L': {step:50, jump: []},
      'C': {step:100, jump: []}
    }
    result, i = 0, 0
    _len = len(A)
    while i <= _len:
        symbol, nextSymbol = A[i], A[i+1]
        if symbol != nextSymbol:
            if nextSymbol in rule[symbol].jump:
                result += rule[nextSymbol].step - rule[symbol].step
                i += 2
            else:
                result += rule[symbol].step
        else:
            result += rule[symbol].step
            i += 1
    
    return result

def removeDuplicates(A):
    _len = len(A)
    if _len == 0 or _len == 1: return _len
    nj = 0
    for i in xrange(_len-1):
        if A[i] != A[i+1]:
            nj += 1
            A[nj] = A[i+1]
            # print nj

    print 'final nj %d' % nj
    return nj



            
if __name__ == '__main__':
    P = [ 87, 14, 25, 41, 17, 48, 42, 15, 74, 45, 73, 20, 11, 39, 54, 5, 29, 53, 89, 66, 56, 4, 60, 98, 92, 20, 16, 80 ]

    A = [ 5, 6, 6, 7,7,8 ]
    B = [1,1,2,2,3,5,5]
    A1 = [5,5,5,5,5,6]
    A2 = [1,1,1, 2, 1]
    
    # A = ["eat", "tea", "tan", "ate", "nat", "bat"]
    A = [2,3,3,6,15,8,7,11,2,1]
    # print sum2(A, 4)