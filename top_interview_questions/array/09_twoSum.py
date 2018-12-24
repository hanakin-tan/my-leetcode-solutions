# problem: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_nums = len(nums)

        if len_nums is 2:
            return [0, 1]

        for i in range(len_nums):
            temp = target - nums[i]
            sub_nums = nums[i + 1:]
            if temp in sub_nums:
                j = sub_nums.index(temp)
                return [i, i + j + 1]


# input
nums = [3, 3]
target = 6
print(nums, target)

solution = Solution()
output = solution.twoSum(nums, target)

# output
print(output)
