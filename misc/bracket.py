def bracket(nn):
    """ Find all valid brackets combinations
    It can be viewed as two way recursion.
    go left to add left brackets until no one left 
    and then go right to add right brackets until no one left
    reach leaf nodes when both left and right brackets are finished.

    The recursion is illustrated below when there are 2 pairs
                      2  2   
                    /
                1   2   (
                /       \
            0 2 ((      1 1 ()
                \           /
                0 1 (()   0 1 ()(
                    \           \
                    0 0 (())    0 0 ()()

    @param nn (int) -- the number of bracket pairs
    """
    def gen_rec(l, r, results):
        """ 
        @param l       (int) -- left brackets remain
        @param r       (int) -- right brackets remain
        @param results (list) -- store current brackets
        """
        if l > r: # invalid state: more left brackets
            return False
        if l == 0 and r == 0:
            print results
            return True
        if l > 0:
            # results are modified during recursion
            # need to pop the one we append before returning to its upper level
            results.append('(')
            gen_rec(l-1, r, results)
            results.pop()
        if r > 0:
            results.append(')')
            gen_rec(l, r-1, results)
            results.pop()
 
    gen_rec(nn, nn, [])