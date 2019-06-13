def next_permutation(A):
    """
    https://www.interviewbit.com/problems/next-permutation/

    @param A (list) -- current permutation of A
    @return A: in place permutation which is numerically next greater
        if no such permutation (A is given as last one in descending order), 
        there is no next greater, so return the first one
    
    This is called lexicographic ordering on permutation. The following 3 and 4
    ints permutations with lexicographic ordering give some ideas:
    1,2,3 -> 1,3,2 -> 2,1,3 -> 2,3,1 -> 3,1,2 -> 3,2,1
    3,5,9,10 -> 3,5,10,9 -> 3,9,5,10 -> 3,9,10,5 -> 3,10,5,9 -> 3,10,9,5 -> 5,3,9,10 ..

    Essentially the next greater one shares the longest common prefix with given A
    This leads us to loop A backwards to find where starts decreasing, call it 'P'
    find the next greater int after P, swap the two, we get a greater one preserving the longest prefix
    reverse those after P to make them ascending, see below:

    ... [5,1,7,6],3, 9,8,4,2 -> [5,1,7,6],4, 2,3,8,9 ...
    A[4] = 3, swap with A[7] = 4: [5,1,7,6],4, 9,8,3,2
    reverse 9,8,3,2
    
    Time: O()
    """
    length = len(A)
    pivot = -1
    # 1: find pivot 
    for j in reversed( xrange(1, length) ):
        if A[j] > A[j-1]:
            pivot = j-1
            break
    print 'pivot A[%d] = %d' % (pivot, A[pivot])
    if pivot == -1:
        A.reverse()
        return A

    # 2: find next greater after p
    # if all greater, ng is the last one
    ng = length-1
    for i in xrange(pivot+1, length):
        if A[i] < A[pivot]:
            ng = i-1
            break
    print 'swap with next greater A[%d]=%d' % (ng, A[ng])
    A[pivot], A[ng] = A[ng], A[pivot]

    # 3: reverse the original descending to ascending order
    l, r = pivot+1, length-1
    print 'reverse from A[%d] to A[%d]' % (l, r)
    while l < r:
        A[l], A[r] = A[r], A[l]
        l, r = l+1, r-1

    return A

if __name__ == '__main__':
    # A = [3,5,10,9]
    A = [3,10,5,9]
    A = [3, 10, 9, 5]
    # A = [5,1,7,6,3,9,8,4,2]
    next_permutation(A)
    print A


        
