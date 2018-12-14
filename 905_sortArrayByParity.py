# Problem: https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        evens = []
        odds = []
        for a in A:
            if a % 2 == 0:
                evens.append(a)
            else:
                odds.append(a)

        return evens + odds

# Input:  
A = [1, 2, 4, 3]

solution = Solution()
output = solution.sortArrayByParity(A)
print(output)
