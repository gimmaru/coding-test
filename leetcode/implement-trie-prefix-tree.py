class Trie:

    def __init__(self):
        self.trie = dict()

    def insert(self, word: str) -> None:
        trie = self.trie
        for char in word:
            if char not in trie:
                trie[char] = dict()
            trie = trie[char]
        trie['Done'] = None

    def search(self, word: str) -> bool:
        trie = self.trie
        for char in word:
            if char not in trie:
                return False
            trie = trie[char]
        return True if 'Done' in trie else False
    
    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for char in prefix:
            if char not in trie:
                return False
            trie = trie[char]
        return True


'''
* 책에 나온 풀이
'''
import collections


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True
    
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True