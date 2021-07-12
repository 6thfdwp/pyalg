def merge_intv(intervals):
    """
    https://www.interviewbit.com/problems/merge-overlapping-intervals/

    @params intervals (list of list)
        [(1,3),(2,6),(8,10],[15,18]]
    @return (list)
        [1,6],[8,10],[15,18]
        merged all overlapped intervals and sorted by start

    Clarify:
    If end of prev interval == start of next interval, merge?
    If there is same intervals, [[5, 6] [5,6]] => [ [5,6] ]
    Can use sort to pre-process the input

    Time:  O(NlogN)
    Space: O(1) exclude result
    """
    def isoverlapped(prev, next):
        return prev[1] >= next[0]

    # in-place sort, can do adjacent merge in one pass, also result is sorted
    intervals.sort( key= lambda x: x[0] )
    print intervals
    result = [intervals[0]]

    for i in xrange(1, len(intervals)):
        prev, next = result[-1], intervals[i]
        if isoverlapped(prev, next):
            # next overlapped end > the end of prev, do merge by updating prev's end
            # Otherwise just skip the next
            if prev[1] < next[1]:
                prev[1] = next[1]
        else:
            result.append(next)

    return result

def max_dist(nums):
    """
    https://www.interviewbit.com/problems/max-distance/

    @params nums (list): [3  5  4  2]
    @return (int): max(j - i) where A[i] <= A[j] i < j

    The idea is to sort the input list but keep the original idx along with each el
    [(2,3), (3,0), (4,2), (5,1)]
    For each el, all els after it are bigger, we need to find their idx diff, pick max one

    The trick is right max: [ 3, 2, 2, 1]
    For each from the right part of the sorted list, find the max idx so far. The diff between
    its original idx and the corresponding max idx is the distance for this el

    Time:  O(NlogN)
    Space: O(N)
    """
    nums_with_idx = [(n, i) for i, n in enumerate(nums)]
    nums_with_idx.sort(key = lambda x: x[0])
    print nums_with_idx
    midx = -1
    rmax = [-1] * len(nums)
    for r in reversed( xrange(len(nums)) ):
        n, idx = nums_with_idx[r]
        midx = max(midx, idx)
        rmax[r] = midx
    print rmax

    res = 0
    for i, (n, idx) in enumerate(nums_with_idx):
        if rmax[i] - idx > res:
            print 'bigger diff found between nums[%d]=%d and nums[%d]=%d' % (rmax[i], nums[rmax[i]], idx, nums[idx])
        res = max(res, rmax[i] - idx)
    return res


if __name__ == '__main__':
    # print A
    intv = [[2,6],[8,10],[15,18],[1,9]]
    # print merge_intv(intv)

    print max_dist([5, 3, 4, 2, 5])
    print max_dist([8, 6, 4, 2])
