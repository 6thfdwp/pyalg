def is_valid_brackets(S):
    """
    S contains '()', '[]', '{}'
    """
    p1 = ('(', ')')
    p2 = ('[', ']')
    p3 = ('{', '}')

    def is_left_one(s):
        return s == p1[0] or s == p2[0] or s == p3[0]

    def is_right_one(s):
        return s == p1[1] or s == p2[1] or s == p3[1]

    def matched(ls, rs):
        # print ls, rs
        return (p1[0] == ls and p1[1] == rs) or \
            (p2[0] == ls and p2[1] == rs) or \
            (p3[0] == ls and p3[1] == rs)

    temp = []
    for s in S:
        if is_left_one(s):
            temp.append(s)
        elif is_right_one(s):
            if not temp: # len(temp) == 0
                # more right bracket than left
                print 'no matched left'
                return False
            last = temp[-1]
            if matched(last, s): 
                temp.pop()
                print '%s - %s is matched' % (last, s)
            else:
                print 'not matched item'
                return False
    
    return not temp

def bracket(nn):
    """ Find all valid brackets combinations

    @param nn (int) -- the number of bracket pairs
    It can be viewed as two way recursion to consume left and right brackets

    The recursion is illustrated below when there are 2 pairs
                      2  2 results []
                    /     \
                 1 2 (    2,1 return
                //     \
            0 2 ((      1 1 ()
                \\           /      \
                0 1 (()    0 1 ()(  1 0 return
                    \           \
                    0 0 (())    0 0 ()()

    Time: O(n^2) tree height 2n, each level cost n
    Space O(2n+n) call stack + results
    """
    def gen_rec(l, r, results):
        """
        @param l       (int) -- left brackets remain
        @param r       (int) -- right brackets remain
        @param results (list) -- store current brackets
        """
        if l > r:
            # prune recursion tree for invalid state:
            # more left brackets as one left need one right to match
            return False
        if l == 0 and r == 0:
            print results
            return True
        if l > 0:
            # results are modified during recursion
            # need to pop the one we append before returning to its upper level
            results.append('(')
            gen_rec(l-1, r, results)
            results.pop()
        if r > 0:
            results.append(')')
            gen_rec(l, r-1, results)
            results.pop()

    gen_rec(nn, nn, [])

def gen_banlance(s):
    """
    @params s (str): '(())('
    @return (str): balanced portion of input s 
    
    (())(':
    lres: ['(', '(', ')', ')', '(']
    rres: ['(', '(', ')', ')', '_']
    
    other inputs: '(()))(())'
    """
    # from left to remove ')' redundancy
    lres = ['_'] * len(s)
    # from right to remove '(' redundancy
    rres = ['_'] * len(s)
    stack = []
    for i in xrange(len(s)):
        if s[i] == '(':
            stack.append(s[i])
            lres[i] = s[i]
        elif stack and stack[-1] == '(':
                stack.pop()
                lres[i] = s[i]
    stack = []
    for i in reversed(xrange(len(s))):
        if s[i] == ')':
            stack.append(s[i])
            rres[i] = s[i]
        elif stack and stack[-1] == ')':
                stack.pop()
                rres[i] = s[i]
    print lres
    print rres


if __name__ == '__main__':
    # print is_valid_brackets('[()()]')
    print is_valid_brackets('{})){}')
    # print is_valid_brackets('(){}')
    # bracket(3)
