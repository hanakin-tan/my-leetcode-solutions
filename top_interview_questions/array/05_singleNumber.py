# problem: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/ 


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num

        return result

# input
nums = [4,1,2,1,2]
print('***input***')
print(nums)

solution = Solution()
output = solution.singleNumber(nums)

print('***output***')
print(output)

