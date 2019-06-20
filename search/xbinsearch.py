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

def countOccurrence1(A, target):
	"""
	Time: O(logN + C)
	O(N) worst case when all items are the same
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

def searchrange(A, target):
    """
    @params A (list): [3,5,6,6,6,7,7] with potential dups
    @params target (int): key to find
    @return (list) target range [start idx, end idx], return empty [] if not found

    Do it in O(logN)
    If we follow counting dups, it will be O(N) if we have lots of dups
    """
    def sided_search(A, target, dir):

        l, r = 0, len(A)-1
        while l <= r:
            m = l + (r-l)/2
            if target < A[m]:
                r = m-1
            elif target > A[m]:
                l = m+1
            else:
                # target found, go left to find start if dir = 'left'
                # print 'find'
                if dir == 'left':
                    r = m-1
                else:
                    l = m + 1

        if target == A[m]:
            return m
        if dir == 'left':
            return m + 1
        if dir == 'right':
            return m - 1

    lr = sided_search(A, target, 'left')
    rr = sided_search(A, target, 'right')
    return [lr, rr]

# def searchcloset(A, target):

if __name__ == '__main__':
    A = [3,5,6,6,6,7,7]
    A = [1,3,4,5,6,6]
    A = [3,4,5,6,6,7,7]
    print searchrange(A, 1)
    print 'aaa'

# if __name__ == '__main__':
#
# 	A = [3,5,6,6,6,7,7]
    # print searchrange(A, 6)
