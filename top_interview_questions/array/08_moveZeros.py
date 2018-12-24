# problem: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        point = 0
        for i in range(len(nums)):
            if nums[point] == 0:
                nums.pop(point)
                nums.append(0)
            else:
                point += 1


# input
nums = [0, 0, 1]
print('***input***')
print(nums)

solution = Solution()
solution.moveZeroes(nums)

# output
print('***output***')
print(nums)
