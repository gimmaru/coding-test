import collections
from typing import List

class TrieNode:
    def __init__(self):
        self.indices = []
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, j):
        node = self.root
        for char in word:
            node = node.children[char]
            node.indices.append(j)

    def _startswith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False, None
            node = node.children[char]
        return True, node

    def is_palindrome(self, word, words, i):
        result = []
        if not word:
            for j, word in enumerate(words):
                if i == j:
                    continue
                left, right = 0, len(word)-1
                is_pal = True
                while left < right:
                    if word[left] != word[right]:
                        is_pal = False
                        break
                    left += 1
                    right -= 1

                if is_pal:
                    result.append([i, j])
                    result.append([j, i])
        else:
            start, node = self._startswith(word)
            if start:
                for j in node.indices:
                    if i == j or not words[j]:
                        continue

                    string = word + words[j]
                    left, right = 0, len(string)-1
                    is_pal = True
                    while left < right:
                        if string[left] != string[right]:
                            is_pal = False
                            break
                        left += 1
                        right -= 1

                    if is_pal:
                        result.append([i, j])
        return result
        

class Solution:
    trie = Trie()

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        for j, word in enumerate(words):
            self.trie.insert(word[::-1], j)
        
        result = []
        for i, word in enumerate(words):
            result.extend(self.trie.is_palindrome(word, words, i))
        return list(set(result))


'''
* 책에 나온 풀이
'''
class TrieNode:
    def __init__(self):
        self.word_id = -1
        self.children = collections.defaultdict(TrieNode)
        self.palindrome_word_ids = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    
    def insert(self, index, word):
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word)-i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index
    
    def search(self, index, word):
        result = []
        node = self.root

        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])
        
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])
            
        return result
    
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)
        
        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))
        return results
