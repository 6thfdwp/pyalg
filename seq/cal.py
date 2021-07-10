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

if __name__ == '__main__':
    # print addBinary('11', '1')
    print addBinary('1010', '1011')