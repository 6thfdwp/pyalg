def permute(L):
    """ Get all permutations for given list
    
    In each recursion level pick one left element to the result and go deep to add more
    until result size equals to the given list (get one permutation) 
    Then return to upper level to pick another and recurse again
    By doing this we achieve the rearrangement of every element
    The recursion tree can be drawn like this:
                  abc   []
                /
              [a]           [b]         ... result size is 1 in this level
             /             /
            [ab] [ac]     [ba]  [bc]    ... each level size increase by 1
           /     /       /      /
          [abc] [acb]   [bac]  [bca]
          /      /       /      /
        print   print   print  print
    
    Time: O(n^n) essentially it contains n nested for loops, each also iterate n times
    """
    def recurse(L, result):
        if len(result) == len(L):
            #print result
            return
        for l in L:
            if l in result:
                continue
            result.append(l)
            recurse(L, result)
            # remove the added l and return back to 
            # what is originally passed from upper level
            result.pop()
    recurse(L, [])
    
def permute_inplace(L):
    """ Generate all permutations in place by swapping
    
    The recursion tree can be drawn like this:
         start=0    [a]bc               [b]ac           [c]ba    
                      |                   |
       start=1  a[b]c  a[c]b         b[a]c  b[c]a        ... iteration in each recursion
             i=start  i=start          |      |
                |        |             
       print  ab[c]    ac[b]         ba[c]  bc[a]
    """
    def recurse(L, start, _len):
        """Swap recursively
        @param L     (list) -- the input list
        @param start (int) -- the index of the start el
        @param _len (int)  -- the list length
        """
        if start == _len-1:
            #print L
            return
        # iteration to swap the item located at 'start'
        # with every other items after it
        for i in range(start, _len):
            # swap for generating new arrangement
            L[start], L[i] = L[i], L[start]

            # see how recursion executed
            #print 'start: %d i: %d' % (start, i), 

            recurse(L, start+1, _len)
            # swap again for restoring the original order
            L[start], L[i] = L[i], L[start]

            #print 'after recurse start: %d i: %d' % (start, i), 
 
    recurse(L, 0, len(L))

def permute_gen(L):
    """ Generator for all permutations

    @param L (list)
    @results (list) -- each yielded permutation
    """
    if len(L) == 1:
        yield L
    else:
        a = [L.pop(0)]
        # each recursion yield partial results of a permutation
        for p in permute_gen(L):
            for i in range(len(p)+1):
                yield p[:i] + a + p[i:]



if __name__ == '__main__':
    import timeit

    def verbose(algname, size, secs, loops):
        print '%s list size %d:' % (algname, size),
        print 'total %.3f sec in %d loops' % (secs, loops)

    size, loops = 3, 10

    #permute(range(3))
    c = 0
    for p in permute_gen( range(10) ):
        #print p
        c += 1
    print c

    #secs1 = timeit.timeit("permute(L)", setup="from __main__ import permute; L=range(8) ", number=loops)
    #secs2 = timeit.timeit("permute_inplace(L)", setup="from __main__ import permute_inplace; L=range(9) ", number=loops)
    #secs3 = timeit.timeit("for p in permute_gen(L): cc=1", setup="from __main__ import permute_gen;L=range(11) ", number=loops)
    #verbose('permute', 8, secs1, loops)
    #verbose('permute_inplace', 9, secs2, loops)
    #verbose('permute_gen', 11, secs3, loops)
