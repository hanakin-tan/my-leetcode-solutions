# problem: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_nums = len(nums)
        index_dict = {}
        if len_nums is 2:
            return [0, 1]

        for index, num in enumerate(nums):
            temp = target - num
            if temp in index_dict:
                return [index_dict[temp], index]
            else:
                index_dict[num] = index


# input
nums = [3, 3]
target = 6
print(nums, target)

solution = Solution()
output = solution.twoSum(nums, target)

# output
print(output)
