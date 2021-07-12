def maxsum_subs(A):
	"""
	https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

	@params A (list): [-2,1,-3,4,-1,2,1,-5,4]
	@return (int):  [4,-1,2,1] = 6

	There is sub-optimal structure, assume f[i] is max sum end at i:
	f[i] = max(f[i-1]+A[i], A[i])
	We either start sub from A[i] if it's bigger (f[i-1]<0) or add it to previous sum
	f[i] is also called local optimal value (max sum)

	There is no overlapping subproblems

	Time: O(N)
	Space: O(1)
		only care about the previous max sum, no need to store for every el
	"""
	size = len(A)
	f = [0] * size
	f[0] = A[0]

	# localmas = A[0]
	res = A[0]
	for i in xrange(1, size):
		f[i] = max(f[i-1]+A[i], A[i])
		print f
		res = max(f[i], res)
		print res
	return res

def maxsum_subs1(A):
	sidx, eidx, t = 0, 0, 0
	localmax, res = 0, -float('inf')

	for i in xrange(len(A)):
		localmax += A[i]
		if localmax < 0:
			localmax = 0
			t = i + 1
		elif res < localmax:
			res = localmax
			sidx = t
			eidx = i
	print 'max sum is between A[%d]=%d and A[%d]=%d: %d' % (sidx, A[sidx], eidx, A[eidx], res)

def max_profit1(A):
    """
	https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-i/

	Only allow buy once and sell once. Find the max profit.
	@params A (list): [7,1,5,3,6,4]
	@return (int): max profit number 5 (buy day 2 and sell day 5)

	If price is alway dropping, no transaction, return 0
	There is sub-optimal structure
    """
    low = A[0]
    res = 0
    for i in xrange(1, len(A)):
        res = max(A[i] - low, res)
        print 'local max res: %d until day %d:' % (res, i+1)
        low = min(A[i], low)
        print 'latest low %d' % low
    return res

if __name__ == '__main__':
	# max_profit1([7,1,5,3,6,4])
    # max_profit1([7,3,5,1,6,4])
    max_profit1([7,3,9,1,6,4]) 
    # max_profit1([7,9,3,1,6,4])
