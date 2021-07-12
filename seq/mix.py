def gen_nearest_smaller(A):
	"""
	https://www.interviewbit.com/problems/nearest-smaller-element/

	@param A (list): [4, 5, 2, 10, 8]
	@return (list):   [-1, 4, -1, 2, 2]

	The catch is when list is ascending, no need to be optimized, every el's nearest
	is its previous el. 
	when it starts descending, For the first el that starts descending (pivot), 
	have to compare previous one by one until a smaller one is found. 
	Bu For the rest of descending portion, we do not need to compare with 
	those greater than the one that just got its nearest

	[4,10,18, 6,2] 6 is the start of descending portion
	it checks 18, 10 until 4 is found, then no need for '2' to check 18, 10 again
	could directly start from '4', which is prev el's nearest

	Clarify & corner cases:
	A is None or 1 el
	two equal found, not smaller

	Time:  O(N * len(stack))
	  stack gets updated quite often, we won't go through long stack for every el
	  the stack is amotized across the descending portion, start growing when it is ascending again
	Space: O(N)
	  when it is sorted ascending order, len(stack) = N
	"""
	if not A:
		return None
	res = [-1]
	stack = [ A[0] ]
	for i in range(1, len(A)):
		if A[i] > stack[-1]:
			res.append(stack[-1])
		else:
			while stack and A[i] <= stack[-1]:
				stack.pop()

			if stack:
				res.append(stack[-1])
			else:
				res.append(-1)

		stack.append(A[i])

	return res

def gen_next_greater_diff(A):
	"""
	https://leetcode.com/problems/daily-temperatures/

	@param A (list): [4, 5, 2, 4, 10, 8]
	@return (list):  [1, 3, 1, 1,  0, 0]
		As the res size is fixed, we can init first with the same size of input 
		The way we fill it with result does not have to be sequential. When it is
		descending, we do not need to find next greater for every el (each involves multi loops),
		can accumulate until it is descedning again

	Time:  O(N * len(stack))
	Space: O(N) sorted in descending len(stack) = N
	 stack stored those index of items that have not found their next greater
	"""
	if not A:
		return None

	stack = []
	res = [0] * len(A)
	for i, a in enumerate(A):
		while stack and a > A[stack[-1]]:
			pre_idx = stack.pop()
			res[pre_idx] = i - pre_idx

		stack.append(i)

	return res

def stock_span(A):
	"""
	https://leetcode.com/problems/online-stock-span/

	@param A (list): [100, 80, 60, 70, 60, 75, 85] list of prices
	@reture (list):  [1, 1, 1, 2, 1, 4, 6]
		Span of stock price, max consecutive days compared backwards from current day (each el)

	The idea is to maitain current highest price and its span, cur = (price, span).
	When next day's price coming, if it's lower, we can immediately stop. If higher, means
	there is new high price, we can use prev span + 1, replace the cur
	If no higher shown (the market keep dropping), we keep pushing (price, 1) until a higher
	price appears, replace them all

	Time:  O(N*len(stack))
	Space: O(N) worst when price keep dropping (descending order)
		when it's in ascending order, the stack holds only one el, and days get accumulated
	"""
	if not A:
		return []

	stack, res = [], []
	for i in xrange(len(A)):
		days = 1
		# if it's first day or A[i] price is lower, not go into while at all
		while stack and A[i] > stack[-1][0]:
			price, span = stack.pop()
			days += span

		stack.append((A[i], days))
		res.append(days)
	return res


if __name__ == '__main__':
	# print gen_nearest_smaller([4, 5, 5, 10, 8])
	# print gen_nearest_smaller([3,2,1])
	# print gen_nearest_smaller([1,2,3])

	# print gen_next_greater_diff([4, 5, 2, 4, 10, 8])
	# print gen_next_greater_diff([4,5,9, 8,7,8,10])
	print stock_span([4,5,9, 8,7,8,10])
