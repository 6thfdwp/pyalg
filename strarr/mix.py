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

if __name__ == '__main__':
    # print A
    intv = [[2,6],[8,10],[15,18],[1,9]]
    print merge_intv(intv)
