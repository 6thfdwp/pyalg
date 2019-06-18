
"""
http://wuchong.me/blog/2014/07/28/permutation-and-combination-realize/
Recursion can be applied when whole problem can be view as a set of smaller similar problems
search, enumeration, backtracking, dvc ...
"""

def permute(L):
    """ Get all permutations for given list

    In each recursion level pick one left element to the result and go deep to add more
    until result size equals to the given list (get one permutation)
    Then return to upper level to pick another and recurse again
    By doing this we achieve the rearrangement of every element
    The recursion tree can be drawn like this:
                  abc []
            l=a  /      \ l=b
              [a]          [b]         ... result size is 1 in this level
        l=b    /  \l=c     /
            [ab] [ac]     [ba]  [bc]    ... each level size increase by 1
        l=c /     /       /      /
          [abc] [acb]   [bac]  [bca]
          /      /       /      /
        print   print   print  print

    Time: O(n^n) essentially it contains n nested for loops, each also iterate n times
    """
    def recurse(L, result):
        if len(result) == len(L):
            print result
            return
        for l in L:
            if l in result:
                continue
            result.append(l)
            recurse(L, result)
            # remove the added l and return result back to
            # what is originally passed from upper level
            # print 'current l: %s' % (l)
            result.pop()
    recurse(L, [])

def permute_inplace(L):
    """
    Time:  O(n!) essentially total number of permutations
    Space: O(n)  call stack
    """
    def recurse(L, start):
        """Swap recursively
        @param L     (list) -- the input list
        @param start (int) -- the index to start swapping with
        @param _len (int)  -- the list length
                            abc
        start=0,i=0 /    i=1 |      i=2 \
        start=1  a[bc]    b[ac]
                 a[cb]    b[ca]
        start=2   / \     /
             ab[c] ac[b] ba[c] bc[a]
        """
        _len = len(L)
        if start == _len-1:
            print L
            return
        # iteration in each recursion to swap the item located at 'start'
        # with every other items after it, each recursion's 'start' will be
        # increased by 1, essentially solve permutation with size-1
        for i in range(start, _len):
            L[start], L[i] = L[i], L[start]
            # print 'start: %d i: %d\n' % (start, i),
            recurse(L, start+1)
            # swap back for make the 'start' item the same for upper level's next iteration
            L[start], L[i] = L[i], L[start]
            # print 'after recurse start: %d i: %d\n' % (start, i),

    recurse(L, 0)

def permute_gen(l):
    """
    [a, b, c] x=[a] l=[b,c] yield [a,b,c] [b,a,c] [b,c,a] ..
      /
   [b,c] x=[b]  l=[c] yield [bc], [cb]
    /   /
   [c]-- yield [c]
    """
    if len(l) == 1:
        yield l
    else:
        x = [l.pop(0)]
        for p in permute_gen(l):
            for i in range(len(p)+1):
                # List-slicing to insert one item poped in current recursion
                # to every position of each permutation from previous recursion
                yield p[:i] + x + p[i:]

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

    Corner cases: A is zero, one or two items

    Time: O(N)
    Space: O(1)
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
    L = ['a','b','c', 'd']
    # permute(L)
    # permute_inplace(L)
    for p in permute_gen(L):
        print p
    # A = [3,5,10,9]
    A = [3,10,5,9]
    A = [3, 10, 9, 5]
    # A = [5,1,7,6,3,9,8,4,2]
    # next_permutation(A)
