def word_pattern(pattern, str):
    """
    https://leetcode.com/problems/word-pattern/

    @param pattern (string) 'abba'
    @param str (string) 'dog cat cat dog'
    @return (bool) true a=>dog b=>cat

    Clarify:
    pattern, str are all lowercase, string may be separated by single space

    Time:  O(N)
    Space: O(2N) => O(N)
     d and seen will store all words separatly, if char in pattern and word in str are all unique
    """
    pl = len(pattern), wl = len(str)
    if pl != wl:
        return False

    # char in pattern => word in str
    # or use word as key, only store one char in dict
    d = {}
    seen = set()
    for c, w in zip(pattern, str):
        # c mapped to different word
        if c in d and d[c] != w:
            return False
        # different c mapped to the same word
        if c not in d and w in seen:
            return False
        d[c] = w
        seen.add(w)

    return True

def isomorphic(s, t):
    """
    https://leetcode.com/problems/isomorphic-strings/

    @param s (string) 'egg'
    @param t (string) 'add'
    @return (bool)  true if s and t pattern matched sequentially

    Clarify:
    If s and t are both ascii chars, we know the input key range
    """
    # each c's ascii code as key, value is the index summation
    # if s and t matched exactly, e.g 'e' => 'a', e should appears in the same index of s as 'a' appears in t
    # if 'e' is in [0,3,5] in s, 'a' should also be [0,3,5] to be matched
    d1, d2 = [0 for _ in xrange(256)], [0 for _ in xrange(256)]

    for i in xrange(len(s)):
        a, b = ord(s[i]), ord(t[i])
        if d1[a] != d2[b]:
            return False

        d1[a] = i
        d1[b] = i
