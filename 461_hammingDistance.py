# Problem: https://leetcode.com/problems/hamming-distance/


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        result = 0
        
        # To binary.
        x = '{0:b}'.format(x)
        y = '{0:b}'.format(y)
        
        len_x = len(x)
        len_y = len(y)
    
        # To list
        if len_x != len_y:
            if len_x > len_y:
                x = list(x)
                y = list(y.zfill(len_x))
            else:
                y = list(y)
                x = list(x.zfill(len_y))
                
        for i in range(0, len(x)):
            if int(x[i]) + int(y[i]) is 1:
                result += 1
            
        return result

# input
x = 1
y = 4

solution = Solution()
output = solution.hammingDistance(x, y)

print(output)
