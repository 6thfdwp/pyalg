def find_pivot(A):
	"""
	A = [15,16,19,20,1,3] pivot (20) index 3
	"""
	def recurse(A, l, r):
		m = l + (r-l) / 2
		if l > r:
			return -1

		# pivot property
		if m > l and A[m] < A[m-1]:
			# m smaller than its left
			# print 'm smaller than left l:%d, m:%d' % (l, m)
			print 'current l,r = (%d, %d) pivot at %d, [%d, %d]' % (l,r, m-1, A[m-1], A[m])
			return m-1
		if m < r and A[m] > A[m+1]:
			# or larger than its right
			print 'current l,r = (%d, %d) pivot at %d, [%d, %d]' % (l, r, m, A[m], A[m+1])
			return m

		if A[m] < A[l]:
			# pivot can only appear in left half, right half sorted
			print 'go to left (%d, %d)' % (l, m-1)
			return recurse(A, l, m-1)
		else:
			print 'go to right (%d, %d)' % (m+1, r)
			return recurse(A, m+1, r)

	l, r = 0, len(A) - 1
	pivot = recurse(A, l, r)
	return pivot


def _search(A, target, l, r):
	if l > r:
		return -1
	m = l + (r-l) / 2
	print l, m, r
	if A[m] == target:
		return m
	if target < A[m]:
		return _search(A, target, l, m-1)
	else:
		return _search(A, target, m+1, r)

def rotate_search(A, target):
	"""
	A = [15,16,19,20,1,3]
	search 1: return 4 (index)
	find pivot can be used to search target, the left and right of pivot are sorted
	just find which part target falls into, by comparing with the first item

	Time: O(ClogN)
	"""
	pivot = find_pivot(A)
	_len = len(A) - 1
	if pivot == -1:
		# no rotate, perform normal search
		return _search(A, target, 0, _len)
	if A[pivot] == target:
		return pivot

	if target >= A[0]:
		# target is within items which not rotated
		return _search(A, target, 0, pivot-1)
	else:
		# otherwise is within those which are rotated
		return _search(A, target, pivot+1, _len)


def rotate_search_1(A, target):
	"""
	One pass search without finding pivot first
	"""
	def search(A, target, l, r):
		if l > r:
			return -1

		m = l + (r-l) / 2
		if A[m] == target:
			return m
		# all items before m are sorted, can apply normal binsearch
		# in this portion of the array
		if A[m] >= A[l]:
			if target > A[l] and target < A[m]:
				return search(A, target, l, m-1)
			else:
				return search(A, target, m+1, r)
		else:
			if target > A[m] and target < A[r]:
				return search(A, target, m+1, r)
			else:
				pass

	_len = len(A) - 1

if __name__ == '__main__':
	A = [3,5,6,6,6,7,7]
	A1 = [5,1,1,4,5,5,5]

	# A = [3,15,16,19,20,1,2]
	A = [16,17,18,19,20,1,2,3,15,16,16,16,16,16]
	# A = [20,1,2,3,15,16]
	# A = [1,2,3,4,5,6,7]
	# A1 = [4,5,6,7,0,1,2]

	print find_pivot(A)

	# print rotate_search(A1, 3)
