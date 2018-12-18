# problem: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return False if len(nums) == len(set(nums)) else True


# input
nums = [1,2,3,1]
print('***input***')
print(nums)

solution = Solution()
output = solution.containsDuplicate(nums)
# output
print('***output***')
print(output)
