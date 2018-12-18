class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # solution one
        len_nums = len(nums)
        point = len_nums - k
        nums[:] = nums[point:] + nums[:point]

        # solution two
        # while(k):
        #     nums[:] = [nums.pop()] + nums
        #     k -= 1


# input
nums = [1,2,3,4,5,6,7]
k = 3

# output
solution = Solution()
solution.rotate(nums, k)

print(nums)

