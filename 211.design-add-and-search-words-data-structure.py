class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = []

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.trie.append(word)

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if '.' not in word:
            return word in self.trie
        for w in self.trie:
            if len(w) != len(word):
                continue
            match = True
            for i in range(len(word)):
                if word[i] != '.' and word[i] != w[i]:
                    match = False
                    break
            if match:
                return True
        return False
        


