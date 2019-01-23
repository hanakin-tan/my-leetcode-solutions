# problem: https://leetcode.com/problems/largest-perimeter-triangle/


class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort(reverse=True)
        len_a = len(A)
        for i in range(len_a - 2):
            a = A[i]
            b = A[i+1]
            c = A[i+2]
            if a < (b + c):
                return a + b + c
        return 0

solution = Solution()
input = [3,2,3,4]

output = solution.largestPerimeter(input)
print(output)

