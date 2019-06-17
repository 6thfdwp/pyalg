"""
key range is [0, 1000000]
could have 10000 items at most (1000 ops)
"""
class LinkedNode():
	def __init__(self, k, v):
		self.pair = (k, v)
		self.next = None
		# pass
	
	def __repr__(self):
		return str(self.pair)

class HashMap(object):
	"""docstring for HashTable"""
	def __init__(self):
		self._size = 1000
		self._occupiedSize = 0

		self.slots = [None] * self._size

	def _hash(self, k):
		return k % self._size
	
	def findNode(cur, k):
		pass

	def put(self, k, v):
		idx = self._hash(k)
		item = self.slots[idx]
		if item is None:
			# new slot assinged 
			print 'new slot[%d] assinged for k: %d' % (idx, k)
			self.slots[idx] = LinkedNode(k, v)
			return

		# slot already occupied
		cur = item
		while cur:
			# k existed in current slot, update the value
			if cur.pair[0] == k:
				print 'key[%d] value updated (%d->%d)' % (k, cur.pair[1], v)
				cur.pair = (k, v)
				return

			if cur.next is None:
				# reach the last node in current slot's list
				# means the provided k is the new key to put
				print 'slot[%d] new key [%d] appended after key %d' % (idx, k, cur.pair[0])
				cur.next = LinkedNode(k, v)
				return

			cur = cur.next


	def get(self, k):
		idx = self._hash(k)
		item = self.slots[idx]
		print 'get value for key: %d' % k

		if item is None:
			return -1
		cur = item
		while cur:
			if cur.pair[0] == k:
				return cur.pair[1]
				
			if cur.next is None:
				return -1

			cur = cur.next			

	def remove(self, k):
		idx = self._hash(k)
		item = self.slots[idx]
		if item is None:
			return

		prev, cur = None, item
		while cur:
			if cur.pair[0] == k:
				# find the one to be removed
				# 
				if prev is None:
					print 'slot[%d] remove first item: %s' % (idx, str(cur))
					self.slots[idx] = cur.next
				else:
					print 'slot[%d] remove item: %s' % (idx, str(cur))
					prev.next = cur.next
				# cur = None
				return

			prev = cur
			cur = cur.next

if __name__ == '__main__':
	hmap = HashMap()
	hmap.put(5, 5)
	hmap.put(9, 9)
	hmap.put(99, 99)
	hmap.put(1050, 1050)
	hmap.put(1099, 1099)
	hmap.put(2089, 2089)
	hmap.put(9099, 9099)
	hmap.put(9, 10)

	
	print hmap.get(5)
	print hmap.get(99)
	print hmap.get(6)

	hmap.remove(9)
	print hmap.get(9)
	hmap.remove(99)
	print hmap.get(1099)

	hmap.put(2099, 2099)



