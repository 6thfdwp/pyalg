def dNums(A, K):
    """
    https://www.interviewbit.com/problems/distinct-numbers-in-window/

    @param A (list): [1, 2, 1, 3, 4, 3] len(A) = 6
    @param K (int): sliding window with K length 3
    @return (list)  [2, 3, 3, 2] len = N-K+1
        each in returned list is the counter of distinct numbers for window K in A

    We do not need to slice the A by K, and count the distinct numbers
    Maintain a counter map for each el, the number of entries in the map is the counter of distinct numbers
    We count for the first window, slide it and calcuate for next window:
    deduct the top el in previous window, add next el for next window

    Time:  O(N)
    Space: O(K) counter map has the K entries at most (no duplicate)
    """
    d = {}
    res = []
    if K > len(A):
        return []
    for i in xrange(len(A)):
        num = A[i]
        d[num] = d.get(num, 0) + 1
        # finish the first window
        if i == K-1:
            res.append(len(d))
            continue

        if i >= K:
            top = A[i-K]
            d[top] -= 1
            # if it is distinct number, delete from current map to maintain right number of keys
            if d[top] == 0:
                del d[top]

            res.append(len(d))

    return res


if __name__ == '__main__':
    print dNums([1, 2, 1, 3, 4, 3], 4)
