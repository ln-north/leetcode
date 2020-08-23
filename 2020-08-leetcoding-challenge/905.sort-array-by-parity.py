#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = list(filter(lambda x : x % 2 == 0, A))
        odd = list(filter(lambda x : x % 2 != 0, A))
        
        return even + odd
# @lc code=end

