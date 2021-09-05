# https://leetcode.com/problems/minimum-window-substring/discuss/26808/here-is-a-10-line-template-that-can-solve-most-substring-problems

from collections import defaultdict

def lengthOfLongestSubstring(s):
    """
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
    Time:  O(s.length)
    Space: O(s.length) worst case no duplicates in string

    :type s: str
     0 <= s.length <= 5 * 10**4
     s consists of English letters, digits, symbols and spaces.
    :rtype: int
     The length of longest substring 
    """
  
    seen = {}
    head, lsub = 0, 0
    for tail, char in enumerate(s):
      # "abcadebbce" when s[tail=8]=c, head is already at 7 due to bb portion
      # we should not move head back to where c was seen last time at 2
      if char in seen and head <= seen[char]: 
        print 'head %d not greater than seen %d' % (head, seen[char])
        # head = max(head, seen[char]+1)
        head = seen[char] + 1
        print 'current tail:%d, seen "%s" at %d, set head %d' % (tail, char, seen[char], head)
      
      lsub = max(lsub, tail-head+1)
      print 'current lsub %d' % (lsub)
      seen[char] = tail
    
    return lsub

def characterReplacement(s, k):
    """
    https://leetcode.com/problems/longest-repeating-character-replacement/
    Time:  O(N) how about inner while ?
    Space: O(1) up to 26 letters counter

    :type s: str
      1 <= s.length <= 10**5
      s consists of only uppercase English letters.
    :type k: int
      0 <= k <= s.length
      
    :rtype: int
     longest substring length containing the same chars after k replacements
     The sliding window need to keep this constraint valid
    """
    _len = len(s)
    if _len == 1:
      return 1
    
    # counter = [0] * 26
    counter = defaultdict(int)
    head, maxRes = 0, 1 
    for tail, a in enumerate(s):
      counter[a] += 1
      # how many replacements needed within window size ? 
      # if need more than k replacement, keep moving head to find the sub range which can become the same chars again
      while head < tail and (tail-head + 1 - max(counter.values()) > k):
        print 'cur window size %d - max occurrence %d > %d' % (tail-head + 1, max(counter.values()), k)
        counter[s[head]] -= 1
        head += 1
        print 'move head to %d: %s' % (head, s[head])
      
      print 'maxRes %d, dist %d' % (maxRes, tail-head+1)
      maxRes = max(maxRes, tail-head+1)
      
    return maxRes

if __name__ == '__main__':
  s = "abcadebbc"
  # s = "abcadabbc"
  # lengthOfLongestSubstring(s)

  s1, k = "AABACCE", 1
  characterReplacement(s1, k)
