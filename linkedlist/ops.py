from linkedlist import *

def merge_sorted(A, B):
	la, lb = A._head, B._head
	prev, head = None, None # new head for result list
	while la and lb:
		if not head:
			# first node, pick small one as new head
			if la.value < lb.value:
				head = la
				la = la.next
			else:
				head = lb
				lb = lb.next
			prev = head
			continue

		if la.value < lb.value:
			prev.next = la
			prev = la
			la = la.next
		else:
			prev.next = lb
			prev = lb
			lb = lb.next
	while la:
		prev.next = la
		prev = la
		la = la.next

	while lb:
		prev.next = lb
		prev = lb
		lb = lb.next

	ml = LinkedList()
	ml._head = head
	return ml

def remove_dup(duplist):
	"""
	Time: O(N)
	Space: O(N) when no duplicate
	"""
	s = set()
	pre, node = None, duplist._head
	while node:
		if node.value in s:
			# remove the current duplicate but not move the pre
			# in case next is still duplicate
			pre.next = node.next
		else:
			s.add(node.value)
			pre = node
		# always move to next node
		node = node.next

def rotatek(ll, k):
	"""
	Rotate singly linklist to the right by k (k>0, k could be larger than length)
	1 - 2 - 5 - 8 - 9 k=2
	return 8 - 9 - 1 - 2 - 5
	Assume the length is 5, need to move 5-2=3 nodes to the end
	in case k > length, need to move 5 - k % length
	"""
	# calculate the length
	n = 0
	node, tail = ll._head, None
	while node:
		tail = node
		node = node.next
		n += 1
	move = n - (k % n)

	# start from head, work to get new head ref
	cur = ll._head
	# loop 'move' times to rotate
	for i in xrange(move):
		# roate cur to the right (as tail next)
		tail.next = cur
		# update the tail ref (cur rotated one becomes new tail)
		tail = cur

		# rotate next node
		cur = cur.next

	# make tail real tail node
	tail.next = None
    # update or return the new head ref
	ll._head = cur




if __name__ == '__main__':
	A = LinkedList([5,8,10])
	B = LinkedList([4,11,15])

	duplist = LinkedList([5,6,5,5,6,3,15])
	duplist = LinkedList([5,6,4,9,15])
	# duplist = LinkedList([5,6,5,4,6,3,15])
	# duplist1 = LinkedList([5,5,5,6,8,15,15])

	# print merge_sorted(A, B)
	ll = LinkedList([1,2,5,8,9])
	print ll
	rotatek(ll, 6)
	print ll
