def reverse_num(num):
    ret = 0
    while num > 0:
        ret = ret * 10 + num % 10
        num = num / 10
    return ret

def is_palindrome_num(x):
    div = 1
    while x/div >= 10:
        # num is in [10,99] div is 10
        # num is in [100, 999] div is 100 etc.,
        # how many digits x has
        div *= 10
    while x > 0:
        l = x / div
        r = x % 10
        if r != l:
            return False
        x %= div # remove leftmost digit
        x /= 10  # remove rightmost digit
        div /= 100
    return True

def is_palindrome_num_rec(x):
    pass

def is_palindrome_str(s):
    def valid_char(c):
        return True if (c < 'z' and c > 'a') \
                or (c < 'Z' and c > 'A') else False
    l, r = 0, len(s)-1
    while l != r :
        if s[l] != s[r]:
            return False
        if not valid_char(s[l]):
            l += 1
            continue
        if not valid_char(s[r]):
            r -= 1
            continue
        l += 1
        r -= 1
    return True

def longest_subpalindrome_dp(s):
    """
    Find the longest palindromic substring in string s

    There exists a optimal substructure, that is if a substring is
    already a plindrome, we can add two more chars at both ends to see if
    they are equal. If true we get a longer one. Formulated below:

    P[i][j] - 2-d array P[i][j] is true iff s[i:j] is palindrome
    P[i][j] = P[i+1][j-1] and s[i][j]
    Base case is one char and two chars plindrome

    time : O(n^2)
    space: O(n^2)
    """
    ls = len(s)
    start, maxlen, end = 0, 1, 0

    P = [ [False]*ls for i in range(ls) ]
    # one char is always palindrome
    for i in range(ls):
        P[i][i] = True
    # two chars checking
    for i in range(ls-1):
        if s[i] == s[i+1]:
            P[i][i+1] = True
            start, maxlen, end = i, 2, i+1
    # start length of 3 up to the whole length of string
    for slen in range(3, ls+1):
        # for each length 'slen' try different parts of substring
        for i in range(ls-slen+1):
            j = i + slen - 1
            if s[i] == s[j] and P[i+1][j-1]:
                P[i][j] = True
                start, maxlen, end = i, slen, j

    print 'maxlen %d, from %d to %d' % (maxlen, start, j)
    return s[start:end+1]


def longest_subpalindrome_2(s):
    """
    time : O(n^2)
    space: O(1)
    """
    def expand(s, l, r):
        """
        @param s (string) -- the input string
        @param l (int) -- left index of substring
        @param r (int) -- right index of substring
        loop invaraint can be l, r maintain boundry of subpalindrome
        """
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # l+1 make sure it's empty when not expanded
        return s[l+1:r]

    ls = len(s)
    if ls == 0:
        return ''
    # use the first char to initialize
    longest = s[0:1]
    for i in range(ls):
        # first expand is to find subpalindrome of odd length
        res = expand(s, i, i)
        if len(res) > len(longest):
            longest = res

        # second expand is to find subpalindrome of even length
        res = expand(s, i, i+1)
        if len(res) > len(longest):
            longest = res
    return longest

if __name__ == '__main__':
    print longest_subpalindrome_2('ababa')
    print longest_subpalindrome_2('abcccccdd')
    # print longest_subpalindrome_dp('aaaaa')
    # print longest_palindrome_dp('abacdfgdcaba')
    # print is_palindrome_str('amannama')
    # print reverse_num(5698)
    # print is_palindrome_num(99)
    # print is_palindrome_num(9875645789)
    # print is_palindrome_num(9)
