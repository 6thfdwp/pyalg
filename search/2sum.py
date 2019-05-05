def twoSum(nums, target):
    """
    Time:  O(N)
    Space: O(N)
    """
    seen = {} # record num -> idx visited so far
    for idx, n in enumerate(nums):
      m = target - n
      # later number n has parity m visited before
      if m in seen:
        return [seen[m], idx]
      
      seen[n] = idx

# two pointers
def twoSumSorted(nums, target):
    """
    Time:  O(N)
    Space: O(1)
    """
    l, r = 0, len(nums) -1
    while l < r:
        if nums[l] + nums[r] == target:
            return [l+1, r+1]
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            r -= 1

def twoSumSorted(nums, target):
    l, r = 1, len(nums)
    while l <= r:
        m = (l + r) / 2
        s = nums[l] + nums[m] 
        if s < target:
            l = m
        elif s > target:
            r = m
        else:
            return
    pass

from collections import OrderedDict
from collections import defaultdict 
# need to return multi results 
def sum2(A, B):
    res = []
    target = B
    d = defaultdict(list)
    for i, a in enumerate(A):
        d[a].append(i+1)
    print d
    for i, a in enumerate(A):
        b = target - a
        if b in d:
            for idx in d[b]:
                # idx = d[b][0]
                # only a on left and b on right, can not be self
                if i+1 < idx:
                    res.append([i+1, idx])
                    break
    print res
    if len(res) == 0: return []
    if len(res) == 1: return res[0]

    n = len(res)
    i, l = 1, res[0]
    while i < n:
        i1, i2 = l[1], res[i][1]
        if i2 < i1:
            l = res[i]
        i += 1

    return l