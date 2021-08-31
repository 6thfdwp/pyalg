def addBinary(a, b):
    """
    https://leetcode.com/problems/add-binary/
    
    :type a: str
    :type b: str
    :rtype: str
    """
    i, j = len(a)-1, len(b)-1
    carry = 0
    result = []
    while i >=0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        
        # if carry = 2, 0 will be appended
        result.append(str(carry % 2))
        # then it will be used as 1 for next sum
        carry /= 2
    
    return ''.join(result[::-1])

def atoi(S):
    """
    Requirements:
    1. Discard white spaces until the first non-whitespace is found
    2. Take an optional plus or minus sign followed by numeric digits
    3. If there are additional chars at the end after those number ignore them
    4. If the sequence of non-whitespace chars is not a valid integer or it's
       empty or contains only whitespaces nothing happens
    5. If the return value is out of range, INT_MAX ( 2147483647) or INT_MIN returned

    '958'
    9 * (10 ** 2) + 5 * (10 ** 1) + 8 * (10 ** 0)
    """
    ls = len(S)
    res = 0
    for i, n in enumerate( reversed(xrange(ls)) ):

        if S[i] == '-':
            m = True
            continue
        # ord return an int representing the value of byte when it is
        # ASCII 8-bit string. The value difference with '0' is the int we want
        # the first digit need to multiply by 10^ (last index), 100, 10, 1..
        res += (ord(S[i]) - ord('0')) * 10**n
    # return (0-res) if m else res
    return res

if __name__ == '__main__':
    print atoi('567')

if __name__ == '__main__':
    # print addBinary('11', '1')
    print addBinary('1010', '1011')