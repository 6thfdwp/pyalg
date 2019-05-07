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
    def recurse(L, start, _len):
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
        if start == _len-1:
            print L
            return
        # iteration in each recursion to swap the item located at 'start'
        # with every other items after it, each recursion's 'start' will be
        # increased by 1, essentially solve permutation with size-1
        for i in range(start, _len):
            L[start], L[i] = L[i], L[start]
            # print 'start: %d i: %d\n' % (start, i),
            recurse(L, start+1, _len)
            # swap back for make the 'start' item the same for upper level's next iteration
            L[start], L[i] = L[i], L[start]
            # print 'after recurse start: %d i: %d\n' % (start, i),

    recurse(L, 0, len(L))

def permute_gen(l):
    """
    [a, b, c] x=[a]
      /
   [b,c] x=[b]
    /   /
   [c]--
    """
    if len(l) <= 1:
        yield l
    else:
        x = [l.pop(0)]
        for p in permute_gen(l):
            for i in range(len(p)+1):
                # List-slicing to insert one item poped in current recursion
                # to every position of each permutation from previous recursion
                yield p[:i] + x + p[i:]


if __name__ == '__main__':
    L = ['a','b','c', 'd']
    # permute(L)
    # permute_inplace(L)
    for p in permute_gen(L):
        print p
