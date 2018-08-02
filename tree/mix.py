from tree.bintree import *
import random, array, tempfile, heapq

def build_bintree(sortedlist):
    T = Binarytree()
    Q = [(0, len(sortedlist)-1)]
    while Q:
        l, r = Q.pop(0)
        mid = (l + r) / 2
        print '%d-%d-%d' % (l, mid, r)
        T.insert(sortedlist[mid])
        if l <= mid-1:
            Q.append( (l, mid-1) )
        if r >= mid+1:
            Q.append( (mid+1, r) )
    return T

def find_parent(p, k1, k2):
    def cover(node, key):
        if node is None: return False
        if node.key == key: return True
        return cover(node.left, key) or cover(node.right, key)
    # if both on the left, the first common parent should be one in the left subtree
    if cover(p.left, k1) and cover(p.left, k2):
        return find_parent(p.left, k1, k2)
    if cover(p.right, k1) and cover(p.right, k2):
        return find_parent(p.right, k1, k2)
    # if both are in different subtrees, no need go deeper, return current p
    return p

def tempfile_gen(t):
    t.seek(0)
    ints = array.array('i')
    for data in read_in_chunks(t, 80):
        ints.fromstring(data)
    # create a generator to be used in merge phase
    for each in ints:
        yield each

if __name__ == '__main__':
    #l = [3,6,8,10,15,16,7,9]
    #t1 = Binarytree()
    #t1.insert(6), t1.insert(8), t1.insert(3),t1.insert(1), t1.insert(9)
    #t0 = build_bintree(l)
    #t2 = build_bintree(l2)

    gen_file(1000)
    #sort_in_chunks()
    #ppoutput()
