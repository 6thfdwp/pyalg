def atoi(S):
    """
    Requirements:
    1. Discard white spaces until the first non-whitespace is found
    2. Take an optional plus or minus sign followed by numeric digits
    3. If there are additional chars at the end after those number ignore them
    4. If the sequence of non-whitespace chars is not a valid integer or it's
       empty or contains only whitespaces nothing happens
    5. If the return value is out of range, INT_MAX ( 2147483647) or INT_MIN returned
    """
    ls = len(S)
    res = 0
    for i, n in enumerate( reversed(range(ls)) ):
        if S[i] == '-':
            m = True
            continue
        # ord return an int representing the value of byte when it is
        # ASCII 8-bit string. The value difference with '0' is the int we want 
        res += (ord(S[i]) - ord('0')) * 10**i
    # return (0-res) if m else res
    return res

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
        print ls, rs
        return (p1[0] == ls and p1[1] == rs) or \
            (p2[0] == ls and p2[1] == rs) or \
            (p3[0] == ls and p3[1] == rs)

    temp = []
    for s in S:
        if is_left_one(s):
            temp.append(s)
        elif is_right_one(s):
            if not temp:
                print 'no matched left'
                return False
            elif matched(temp.pop(), s): 
                print '%s is matched' % s
            else:
                print 'not matched item'
                return False
    
    return not temp

if __name__ == '__main__':
    # print atoi('9')
    print is_valid_brackets('[{}}]')
    print is_valid_brackets(')){}')
    print is_valid_brackets('(){}')
