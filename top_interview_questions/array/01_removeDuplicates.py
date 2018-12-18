# Problem: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums <= 1:
            return len_nums

        new_array = [nums[0]]
        for i in range(1, len_nums):
            if nums[i] != nums[i-1]:
                new_array.append(nums[i])

        nums[:] = new_array
        return len(new_array)


# input
nums = [1, 2, 2, 4, 3]
print('***input***')
print(nums)

solution = Solution()
output = solution.removeDuplicates(nums)

print('***output***')
print(nums)
print(output)
