def rotate_inplace(M):
    """ Rotate N*N matrix by 90 clockwise in place

    Process in a layer fashion, each layer contain left, top, right, bottom 4 edges 
    All items at left edge go to top edge, bottom go to left, right to bottom..
    
    Time : 
    Space: O(1)
    """
    n = len(M) # the size of matrix
    for layer in range(n/2):
        j = n - 1 - layer
        print "layer bound (%d,%d)" % (layer, j)
        # Inner loop processes all items in the current layer
        # Each iteration rotate one item at 4 edges
        for i in range(layer,j):
            #offset = j - i
            offset = n - 1 - i
            # save the top
            first = M[layer][i]
            # left -> top
            M[layer][i] = M[offset][layer] # M[offset][i] 
            # bottom -> left
            M[offset][layer] = M[j][offset]
            # right -> bottom
            #print 'right %d->bottom %d' % (M[i][j], M[j][offset])
            M[j][offset] = M[i][j]
            # top -> right
            M[i][j] = first

def rotate(M):
    """Rotate N*N matrix by 90 clockwise using another matrix M_

    Process in row by row fashion
    the first row in M becomes the last column in M_ and so on
    
    Time : O(n^2)
    Space: O(n^2)
    """
    n = len(M)
    M_ = [ [0 for j in range(n)] for i in range(n) ]
    for i in range(n):
        for j in range(n):
            M_[j][n-i-1] = M[i][j]
    return M_
