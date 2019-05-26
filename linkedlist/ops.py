from linkedlist import *

def merge_sorted(A, B):
	la, lb = A, B
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

	return head

if __name__ == '__main__':
	A = LinkedList([5,8,10])
	B = LinkedList([4,11,15])
	print A, B
	# merge_sorted(A, B)