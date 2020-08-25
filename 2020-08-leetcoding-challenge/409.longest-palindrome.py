#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        for n in collections.Counter(s).values():
            result += n // 2 * 2
            if result % 2 == 0 and n % 2 == 1:
                result += 1
        return result

# @lc code=end
