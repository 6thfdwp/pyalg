def lengthOfLongestSubstring(s):
    """
    :type s: str
     0 <= s.length <= 5 * 10**4
     s consists of English letters, digits, symbols and spaces.
    :rtype: int

    Time:  O(s.length)
    Space: O(s.length) worst case no duplicates in string
    """
  
    seen = {}
    head, lsub = 0, 0
    for i, char in enumerate(s):
      # "abcadebbce" when s[i]=c, head is already at 7 due to bb portion
      # we should not move head back to where c was seen last time at 2
      if char in seen and head <= seen[char]: 
        print 'head %d not greater than seen %d' % (head, seen[char])
        # head = max(head, seen[char]+1)
        head = seen[char] + 1
        print 'current i:%d, seen "%s" at %d, set head %d' % (i, char, seen[char], head)
      
      lsub = max(lsub, i-head+1)
      print 'current lsub %d' % (lsub)
      seen[char] = i
    
    return lsub

if __name__ == '__main__':
  s = "abcadebbc"
  # s = "abcadabbc"
  lengthOfLongestSubstring(s)
