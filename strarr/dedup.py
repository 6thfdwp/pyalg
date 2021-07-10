def remove_dup(S):
    """
    Remove duplicate chars of a string, only keep the first occurrence

    To achieve time efficiency, use dict or bool array to keep track
    if a char is already seen before and don't add to the result string

    @param S (string) -- input string to be checked

    Time : O(n)
    Space: O(n) worst case no duplicate found
    """

    if len(S) == 1 or len(S) == 0:
        return S
    hit = dict(); res = []
    for c in S:
        if c in hit:
            continue
        hit[c] = True
        res.append(c)
    return ''.join(res)

"""
Two pointers: 
i for iteration index, tail holds position right after the last non-dup char found so far
So we know where to put the next non-duplicate char (at tail)
"""
def remove_dup_inplace(ss):
    """
     Time :  O(n^2)
             worst case no duplicate found (tail always equal to i)
             1 + 2 + 3 + ... + n-1
     Space:  O(1)
             without considering the input string
    """
    if len(ss) <= 1:
        return ss
    S = list(ss) # python string is immutable, convert it to list to be able to modify
    tail = 1
    for i in range(1, len(S)):
        # loop invariant is tail always holds position such that
        # all chars on its left are non-duplicate
        j = tail - 1

        # for each char compare every el before tail to see if new el is a duplicate
        while j >= 0 and S[i] != S[j]:
            j -= 1
        if j < 0:
            # ith char not a duplicate add this char to the tail and advance the tail
            S[tail] = S[i]
            tail += 1

    # finish checking all chars, put termination
    # all chars before tail are the result string
    # tail equals to len(S), no duplicate
    return ''.join(S[:tail])

def remove_insorted(ss):
    # all the dups are stay together
    # Time: O(N) Space: O(1)
    tail = 1
    for i in xrange(1, len(ss)):
        if (ss[i] != ss[i-1]):
            ss[tail] = ss[i]
            tail += 1
    print 'new length after removing %d' % tail
    return ''.join(ss[:tail])

if __name__ == '__main__':
    # print remove_dup_inplace('55556')
    # print remove_dup_inplace('5678')
    # print remove_dup_inplace('555788900')
    # print remove_dup_inplace('989898055')
    
    print remove_insorted(['5'])
    print remove_insorted(['5', '6', '7','8','9'])
    print remove_insorted(['5', '5','5','7','8','9'])
