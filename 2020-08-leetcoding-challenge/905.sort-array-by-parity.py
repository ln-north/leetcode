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

        result = []

        for i in range(len(A)):
            if i % 2 == 0:
                result.append(even[int(i / 2)])
            else:
                result.append(odd(int((i - 1) / 2)))
        
        return result
# @lc code=end

