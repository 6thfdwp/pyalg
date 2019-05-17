from collections import OrderedDict
from collections import defaultdict 

"""
Return first pair indices [i, j] that add up to target
"""
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
# some binary search form?
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


"""4sum
[1, 0, -1, 0, -2, 2], target = 0
all solution set:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
This is how twoSums dict would look like:
s[1] = [{0, 1}, {0,3}]
s[0] = [{0, 2}, {1,3}, {4,5}]
s[-1] = [{0, 4}, {1,2}, {2,3} ]
s[3] = [{0, 5} ]
s[-2] = [{1,4}, ...]
s[-3] = [{2,4}]
"""
def foursum(nums, target):
    i, _len = 0, len(nums)
    res = []
    twoSums = defaultdict(list)
    for i in xrange(_len-1):
      for j in xrange(i+1, _len):
        s = nums[i] + nums[j]
        # record the current two sums between {i,j}
        twoSums[s].append({i, j})

        # print i, j 
        diff = target - s
        if diff in twoSums:
            # find the other two items' index that add up to target
            idxs = twoSums[diff]
            for t in idxs:
                # only consider 4 unique items (their index not overlapped)
                if t.intersection({i, j}):
                    continue

                _i, _j = t
                # form the new 4 unique items
                four = {_i, _j, i, j}
                print four
                if not res:
                    res.append(four)
                    continue
                
                existed = False
                for r in res:
                    common = r.intersection(four)
                    if len(common) == 4:
                        existed = True
                        break
                if not existed:
                    res.append(four)
                    print res

    results = []
    for idxset in res:
        results.append([ nums[i] for i in idxset ])
            
    return results

if __name__ == '__main__':
    print foursum([1,0,-1,0,-2,2,2,3], 2)


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