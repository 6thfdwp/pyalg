class TrieNode(object):
  def __init__(self, val=None):
    self.val = val
    self.children = {}
    # if only has 26 lower case letters, can use array to store nodes
    # the position can be decided with ord(c) - ord('a')
    # self.children = [None] * 26
    self.ended = False

class Trie(object):
    """
    input range: a-z
    
    If W is the length of word to insert or search
    Time:  O(W)
    Extra space needed for this efficiency, the children storage
    worst is O(number of words inserted * input range)
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = TrieNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None

        """
        curNode = self._root
        for c in word:
          if c not in curNode.children:
            # branch out a new node as curNode children
            # measn some new word inserted
            curNode.children[c] = TrieNode(c)

          # if the c is found in existing path, use the existing node
          # else use the new node just created
          curNode = curNode.children[c]

        # mark the last node corresponding to last char as ended
        # NOTE: not just leaf node will be marked as ended, some previously inserted
        # which is prefix of other words added later
        # does not hurt to mark again if Trie already contains exactly same word
        curNode.ended = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool

        check each char in word
        True if a path containing ended node found when word finished
        """
        curNode = self._root
        for c in word:
          if c not in curNode.children:
            return False
          curNode = curNode.children[c]

        return curNode.ended

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curNode = self._root
        for c in prefix:
          if c not in curNode.children:
            return False
          curNode = curNode.children[c]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
