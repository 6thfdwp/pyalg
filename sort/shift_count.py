"""
Problem:
 https://www.hackerrank.com/challenges/insertion-sort

 This is an advanced analysis for insertion sort to count the number of shifts 
 insertion sort requires to sort a large list of keys where size N >= 100000. 
 It shows how a list of keys are close to a sorted order

 The basic idea is to use modified mergesort procedure instead of original
 insertion sort which would timeout under large number of keys.
 Time complexity is bound to O(nlogn). 
"""
def merge_count(A, l, r):
    """
     Modified mergesort to recursively count between divided subarrays

     @param A  a list to be operated on
     @param l  int left index of subarray
     @param r  int right index of subarray

     @returns tuple including count and sorted subarray 
    """
    def merge(A, lh, rh):
        """
        Merge two sorted list and count the shifts between the two

        Given both are sorted, the shifts can only happen when ith item
        in left half is greater than jth in right half. That is jth item
        need to be shifted before ith item. So the number of shifts is simply
        len(left half) - i
        Example:
         lh = [1, 3, 5]
         rh = [2, 4, 6]
         lh[1] > rh[0], rh[0] needs to shift before lh[1] which is len(lh)-1 = 2
         So is lh[2] > rh[1] which is 3-2=1. The total shifts is 3
        
        @param A  the whole input list
        @param lh left half sorted list
        @param rh right half sorted list

        @returns tuple including count and the merged list
        """
        i, j, k = 0, 0, 0 # index for left half, right half and merged list
        llen, rlen = len(lh), len(rh)
        count = 0
        r = [0] * (llen+rlen)
        while i<llen and j<rlen:
            if lh[i] <= rh[j]:
                r[k] = lh[i]; i += 1
            else:
                r[k] = rh[j]; j += 1
                count += llen - i
            k += 1
        while i < llen:
            r[k] = lh[i]
            k += 1; i += 1
        while j < rlen:
            r[k] = rh[j]
            k += 1; j += 1
        return (count, r)

    if l >= r:
        return ( 0,[A[l]] )
    m = l + (r-l)/2
    #if (m-l) > 1:
    lc, lh = merge_count(A, l, m)
    rc, rh = merge_count(A, m+1, r)

    # We need to add shift count in the current recursive level
    # between lh and rh together with
    # the counts from those two subarray respectively
    count, merged = merge(A, lh, rh)
    count += lc + rc 
    return (count, merged)

if __name__ == '__main__':
    #A = [1,1,1,2,2]
    A = [2,1,3,1,2]
    c, r = merge_count(A, 0, len(A)-1)
    print c
