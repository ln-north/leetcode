#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        reduced = list(set(nums))    

        for num in reduced:
            nums.remove(num)
        
        return nums
    
# @lc code=end

