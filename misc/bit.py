class Bitset:
    """
    General class represents bit vector using bytearray
    """
    def __init__(self, _range):
        """ 
        Initialize bit vector with all 0 bits

        @param range (int) -- the range of a list of ints
        """
        # how many bytes we need to represent the range
        size = (_range >> 3) + 1 
        self._bv = bytearray([0]* size)
 
    def get(self, num):
        """
        Check if a given number is set in a bit of bit vector 

        @param num (int) -- the number to be checked

        @return 1 if set otherwise 0 
        """
        idx = num >> 3 # divided by 8 to get the index of bytearray where num belongs to
        offset = num & 0b111 # equal to modular since the value of mod 8 is bounded 0-7
        return self._bv[idx] & (1 << offset)
 
    def set(self, num):
        """
        Set a number's corresponding bit to 1
        """
        idx = num >> 3
        offset = num & 0b111
        self._bv[idx] |= (1 << offset)
        
 
if __name__ == '__main__':
    a = [random.randint(0, 100) for i in range(150)]
    print a
    bitset = Bitset(100)
    # use Bitset class to print all duplicates in given array
    # with range from 0 to 100
    for e in a:
        if bitset.get(e):
            print e
        else:
            bitset.set(e)


def diffbits(a, b):
    """
    Check how many bits required to convert integer a to b
    """
    # xor gets different bits between the two
    c = a ^ b; count = 0
    while c > 0: # get the number of '1' bits
        count += c & 1
        c = c >> 1
    return count

def missint():
    """
    Given a large range of integers (billions) find the missing int
    We want to achieve memory efficiency 

    The idea is to use a bit vector, mapping every int to one bit. 
    Example: 1Gb (2^30 8 billion bits) can represent 8 billion ints
    """
    irange = 100
    # simulate a list of ints ranging from 0 to irange
    # in actual case this should come from an external file
    a = [random.randint(0, irange) for i in range(100)]
    #a = [0,1,2,3,4,5,6,9,11,15,10,10,12,7,14,13,7,8]
 
    size = irange / 8 + 1
 
    # allocate a bit vector to represent all ints
    bitset = bytearray([0]*size)
 
    # mapping each int to its corresponding bit
    # each/8 get the index of bytearray (which byte) it belongs to
    # each%8 get the offset of the byte where it should set to 1
    # e.g. the third byte represents ints from 16-23
    # 20 should be mapped to the third byte and the 5th bit (count from the least significant bit)
    for each in a: 
        # keep reading from the file to set bit vector
        bitset[each/8] |= 1 << (each%8)
    for i in xrange(len(bitset)):
        #print bin(bitset[i])
        # visit individual bit of each byte to check a 0 bit
        for j in range(8):
            if (bitset[i] & 1 << j) == 0:
                print i * 8 + j
                return


def swap(a, b):
  """Swap without another temp variable
  According to xor, (a^b) ^ b = a^ (b^b) = a ^ 0 = a
  
  @param a (int)
  @param b (int)
  """
  a = a ^ b
  b = a ^ b
  a = a ^ b # => (a ^ b) ^ a = a ^ a ^ b