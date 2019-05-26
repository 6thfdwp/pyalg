import random
 
"""
Partition, merge variations
"""
def partition(ar, l, r):
    """
    Partition the array in the range [l..r)

    @param ar (list) -- the input array
    @param l  (int)  -- the left most index (inclusive) of current partition
    @param r  (int)  -- the right most index (exclusive) of current partition

    @return int -- the position where the pivot should sit in the array
    """
    # use a random pivot to avoid getting the bad pivot if input array is sorted
    idx = random.randrange(l,r)
    ar[l], ar[idx] = ar[idx], ar[l]
    pivot = ar[l]
    m = l
    # loop invariant is that m always holds position such that 
    # where the pivot should sit
    #
    # 4,[2],1,5,3 pivot = 4 m = 1
    # 4,2,[1],5,3   m = 2
    # 4,2,1,[5],3   m = 2
    # 4,2,1,3,[5]   m = 3
    # => 3,2,1,4,5  return 3
    for i in range(l+1, r):
        # when pivot is the biggest one, m will always equal to i
        if ar[i] < pivot:
            m += 1
            ar[m], ar[i] = ar[i], ar[m]
 
    # swap the pivot (a[l]) to its right position (pointed by m)
    ar[l], ar[m] = ar[m], ar[l]
    #print 'partition %d to %d, pivot %d' % (l,r,pivot)
    return m
 
def quickselect(ar, k):
    """
     Select the kth smallest el in an array
     refer: http://en.wikipedia.org/wiki/Quickselect     
     Utilize the partition procedure in quicksort, but only recurse in one side instead of two

     @param ar (list) -- the input array
     @param k  (int)  -- the index of the kth smallest el
     
     worst case: O(n^2)
        in each recursive partition costs n, n-1, n-2 .. 1
     best case: O(n)
        in each recursive partition costs n, n/2, n/4 .. 1
    """
    def recurse(ar, l, r, k):
        """
        Internal function to recursively partition the array to find the kth smallest el

        @param ar (list) -- the input array
        @param l  (int)  -- the left most index (inclusive) of current partition
        @param r  (int)  -- the right most index (exclusive) of current partition
        @param k  (int)  -- the index of the kth smallest (k-1)

        @return int -- the index that equals to k after several partition procedures
        """
        if l+1 >= r: return l
 
        # after partion m is the right position if the array sorted
        m = partition(ar, l, r)
        if m == k:
            return m
        elif m < k:
            # The kth el is bigger sitting on the right side of pivot el
            return recurse(ar, m+1, r, k)
        else:
            # Otherwise is smaller sitting on the left side of pivot el
            return recurse(ar, l, m, k)
    
    idx = recurse(ar, 0, len(ar), k)
    return ar[idx]