def gen_nearest_smaller(A):
	"""
	https://www.interviewbit.com/problems/nearest-smaller-element/
	
	@param A (list): [4, 5, 2, 10, 8]
	@return (list):   [-1, 4, -1, 2, 2]

	The catch is when list is ascending, nothing can be optimized, every el's nearest 
	is its previous el. when it starts descending, there is something we can do. 
	For the first el that starts descending (pivot), have to compare previous one by one
	until a smaller one is found. So For the rest of descending portion, we do not need 
	to compare those greater than the one that just got its nearest. 
	
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
	  For each el, put the index diff with its next greater el into result
	  same as next greater, as need to find it to calculate the diff
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


if __name__ == '__main__':
	# print gen_nearest_smaller([4, 5, 5, 10, 8])
	# print gen_nearest_smaller([3,2,1])
	# print gen_nearest_smaller([1,2,3])

	print gen_next_greater_diff([4, 5, 2, 4, 10, 8])
	print gen_next_greater_diff([4,5,9, 8,7,8,10])



