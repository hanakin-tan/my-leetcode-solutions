# Problem: https://leetcode.com/problems/peak-index-in-a-mountain-array/


class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # for i in range(0, len(A)):
        #     if A[i] > A[i+1]:
        #         return i

        start = 0
        end = len(A)

        while start < end:
            mid = (start + end) // 2
            if A[mid] > A[mid + 1]:
                end = mid
            else:
                start = mid + 1

        return start


# Input
A = [0, 2, 1, 0]

solution = Solution()
output = solution.peakIndexInMountainArray(A)

print(output)