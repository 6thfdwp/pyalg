def subsets(S):
    """ Get all possible subsets of the given set
    The idea is to find subset in smaller range, then increase the range
    by adding one item to each subset found before until all items are combined
    """
    def subsets_rec(A, index):
        # base case only one item left
        if index == 0:
            # subsets of one item including an empty set
            return [set([ A[index] ]), set()]
        # go deep to get the subset for base case
        subsets = subsets_rec(A, index-1)
        newItem = A[index]
        newSubsets = []
        for subset in subsets:
            # add the new item to each subset found before
            # need to create a new subset otherwise it modifys original one
            nset = set(subset)
            nset.add( newItem )
            newSubsets.append(nset)
        return subsets + newSubsets
    A = list(S)
    return subsets_rec(A, len(A)-1)


def subsets_yield(S):
    """ Generator version using yield

    Allow caller to inspect each subset generated during recursive process
    no need to wait all the subsets returned to do so
    It's also memory efficient, get rid of an extra list (newSubsets)
    to store intermediate results
    """
    def subsets_rec(A, index):
        if index == 0:
            yield set()
            yield { A[index] }
            #yield set([ A[index] ])
        else:
            newitem = { A[index] }
            # iterate the yielded results from smaller range
            for sub in subsets_rec(A, index-1):
                # yield both original and newly generated subset
                yield sub
                # new set by union
                yield sub | newitem

    A = list(S)
    for sub in subsets_rec(A, len(A)-1):
        yield sub

def subsets_yield_with_copy(S):
    if not S:
        yield set()
    else:
        item = {set(S).pop()}
        for sub in subsets_yield_with_copy(S - item):
            yield sub
            yield sub | item

def subsets_yield_inplace(S):
    """
     Time:  O(n*2^n) almost the total number of given input's subsets if we take set union
            as constant in each recursion
     Space: O(n) mainly for recursion call stack, and we ignore output subsets space

      [5,6,7,8]
        |
       [6,7,8] item = 5
        |
       [7,8] item = 6
        |
       [8] item = 7 yield set(7) yield set(7,8)
        |  /
       [] item = 8 yield set() yield set(8)
        | /
       [] yield set()
    """
    if not S:
        yield set()
    else:
        # we can pop directly on original set S
        item = {S.pop()}
        # each recursion take the popped set which is one item less than previous one
        # when func returns, the original S becomes empty
        for sub in subsets_yield_inplace(S ):
            yield sub
            yield sub | item


if __name__ == '__main__':
  S = set([5,6,7,8])
  # results = subsets(A1)
  def verbose(t):
    return '%.2f ms' % t*1000

  sp0 = 'from subset import subsets;'
  sp1 = 'from subset import subsets_yield_with_copy; gensub=subsets_yield_with_copy(set([5,6,7,8,9,0,1,3]))'
  sp2 = 'from subset import subsets_yield_inplace; gensub=subsets_yield_inplace(set([5,6,7,8,9,0,1,3]))'
  import timeit
  print timeit.repeat("subsets(set([5,6,7,8,9,0,1,3]))", setup=sp0, number=1)
  print timeit.repeat("for sub in gensub: continue", setup=sp1, number=1)
  print timeit.repeat("for sub in gensub: continue", setup=sp2, number=1)
