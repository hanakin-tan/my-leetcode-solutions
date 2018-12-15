# Problem: https://leetcode.com/problems/flipping-an-image/


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for line in A:
            line.reverse()
            line[:] = [abs(x-1) for x in line]
            result.append(line)
                
        return result

# input 
A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

solution = Solution()
output = solution.flipAndInvertImage(A)

print(output)
