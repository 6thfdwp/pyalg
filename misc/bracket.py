def bracket(nn):
    """ Find all valid brackets combinations

    @param nn (int) -- the number of bracket pairs
    It can be viewed as two way recursion to consume left and right brackets

    The recursion is illustrated below when there are 2 pairs
                      2  2 results []
                    /     \
                 1 2 (    2,1 return
                //     \
            0 2 ((      1 1 ()
                \\           /      \
                0 1 (()    0 1 ()(  1 0 return
                    \           \
                    0 0 (())    0 0 ()()

    Time: O(n^2) tree height 2n, each level cost n
    Space O(2n+n) call stack + results
    """
    def gen_rec(l, r, results):
        """
        @param l       (int) -- left brackets remain
        @param r       (int) -- right brackets remain
        @param results (list) -- store current brackets
        """
        if l > r:
            # prune recursion tree for invalid state:
            # more left brackets as one left need one right to match
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

def bracket_gen(nn):
    if (nn == 1):
        yield ['(',')']
    # bracket(nn-1)

if __name__ == '__main__':
    bracket(3)
