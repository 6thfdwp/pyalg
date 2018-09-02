# 4,2,1,5,3
  # 2,4,[1],5,3 lastSortedIdx = 1
  # 1,2,4,[5],3 lastSortedIdx = 2
def insertsort(A):
    """
    Loop invariant: all items before i that's in current for loop are sorted
    efficient when most of items are already in sorted position

    Time: O(n^2) upper bound if in reverse order
    """
    _len = len(A)
    if _len <= 1:
        return A
    for i in xrange(1, _len):
        j = i
        while A[j] < A[j-1] and j > 0:
            # since items up to j-1 have been sorted, if A[j] is in right position
            # we could early break go to next one to check
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
    return A

def mergesort(A):
    def recurse(l, r):

    return recurse(0, len(A))

    
if __name__ == '__main__':
    A = [1,2,3,5,4]
    print insertsort(A)
