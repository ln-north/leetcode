#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
from collections import defaultdict

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = defaultdict(lambda: list())
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.data[len(word)].append(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        words = self.data[len(word)]

        for i, char in enumerate(word):
            words = [c for c in words if char in ('.', c[i])]
            if not words: 
                return False
        return True

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

