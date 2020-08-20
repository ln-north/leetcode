#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
import math

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num >= 4:
            if num % 4 == 0:
                num = num / 4
            else:
                return False
        
        if num == 1:
            return True
        else:
            return False
        
# @lc code=end

