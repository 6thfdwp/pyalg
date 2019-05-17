def countOccurrence(A, target):
  """
  @param A: given sorted array potentially with dups
  	A = [3,5,6,6,6,7,7] target = 6
  	A = [5,5,5,5]  target = 5
 
  Time: O(N)
  """
  count = 0
  for i in xrange(len(A)):
  	if A[i] == target:
  		count += 1
  	elif A[i] < target:
  		# move next larger to find
  		continue
  	else:
  		break
  
  return count

def count1(A, target):
	"""
	Time: O(logN + C) 
	worst case is all items are the same
	"""
	l, r, m = 0, len(A) - 1, -1
	count = 0
	while l <= r:
		m = l + (r - l) / 2
		print l, r
		if A[m] == target:
			count += 1
			break
		elif target < A[m]:
			r = m - 1
		else:
			l = m + 1

	print '(%d, %d) find %d at %d' % (l, r, target, m)
	if m == -1: return 0

	i, j = m-1, m+1
	while i >= l and A[i] == target:
		print 'check left at %d' % i
		count += 1
		i -= 1
	while j <= r and A[j] == target:
		print 'check right at %d' % j
		count += 1
		j += 1

	return count


if __name__ == '__main__':
	A = [3,5,6,6,6,7,7] 
	A = [5,5,5,5]
	# A = [1,2,3,4] 
	target = 4
	# print countOccurrence(A, target)
	print count1(A, target)

