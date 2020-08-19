#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = re.sub('[^a-z0-9]', "", s.lower())
        if lower == lower[::-1]:
            return True
        else:
            return False
        
# @lc code=end

