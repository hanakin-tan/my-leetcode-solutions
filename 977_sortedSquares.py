# problem: https://leetcode.com/problems/squares-of-a-sorted-array/
import math


class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        for a in A:
            result.append(int(math.pow(a, 2)))
        result.sort()

        return result


solution = Solution()
input = [-4,-1,0,3,10]

output = solution.sortedSquares(input)

print(output)


