def reverse_words(text):
    """
    Print text containing several words in reversed order
    Use list slice for one-line function
    """
    print ' '.join( text.split(' ')[::-1] )

"""
reverse a string of words
" the sky   is blue  " => "blue is sky the"
"""
def reverse_words_rec(text):
    words = text.split(' ')
    length = len(words)
    if length == 0:
        print ''

    def recurse(i):
        """ 
        Internal recursive function to put each word in reversed order
        Use the recursive call stack to control the order
        
        Time : O(n) n is the number of words 
        Space: O(n) allocated for call stack
        """
        # reach to the last word, return as the first one to upper recursive call
        if i == length-1:
            return [ words[i] ] 
        res = recurse(i+1)
        print 'reach word at %d' % (i+1)
        res.append( words[i] )
        print 'append previous word: %s' % (words[i])
        return res

    # print ' '.join( recurse(0) )
    print recurse(0)
    
def reverse_in_place(text):
    words = text.split(' ')
    _len = len(words) - 1
    i, j = 0, _len
    # while i < j:
    #   words[i], words[j] = words[j], words[i]
    #   i += 1
    #   j -= 1
    for i in range( (_len/2 + 1) ):
        j = _len - i
        words[i], words[j] = words[j], words[i]

    print ' '.join(words)
  
if __name__ == '__main__':
    original = "the sky is blue"
    o = ' the sky   is blue  '
    reverse_words_rec(o)
