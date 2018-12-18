# Problem: https://leetcode.com/problems/array-partition-i/


class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
        return result


# input
nums = [1, 4, 3, 2, 3, 8]

solution = Solution()
output = solution.arrayPairSum(nums)

print(output)
