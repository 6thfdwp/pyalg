def next_permutation(A):
    """
    https://www.interviewbit.com/problems/next-permutation/

    @param A (list) -- current permutation of
    @return A: in place permutation which is numerically next greater
        if no such permutation (descending order), make it ascending

    1,2,3 → 1,3,2
    3,4,5,6,7 → 3,4,5,7,6
    3,2,1 → 1,2,3 (no such permutation
    20, 50, 113 → 20, 113, 50

    Find the pivot where number start descreasing, this is where we need to swap

    """
    _len = len(A)
    for a in reverse( xrange(_len-1) ):
        
