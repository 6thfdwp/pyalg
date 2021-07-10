from collections import defaultdict

def groupAnagrams(strs):
    """
    https://leetcode.com/problems/group-anagrams/

    :type strs: List[str]
    :rtype: List[List[str]]

    input 1: ["eat","tea","tan","ate","nat","bat"] => 
        [["bat"],["nat","tan"],["ate","eat","tea"]]
    input 2: [""] => [[""]]
    can return in any order (Hash table unordered)
    """
    d = defaultdict(list)
    for str in strs:
        k = ''.join(sorted(str))
        d[k].append(str)
    
    return d.values()

if __name__ == '__main__':
   input1 = ["eat","tea","tan","ate","nat","bat"] 
   input2 = [""]
   input3 = ['a']
   print groupAnagrams(input2)