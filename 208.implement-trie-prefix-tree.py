class Trie(object):

    def __init__(self):
        self.trie = []

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.trie.append(word)
        return None

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word in self.trie


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        for word in self.trie:
            if word.startswith(prefix):
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)