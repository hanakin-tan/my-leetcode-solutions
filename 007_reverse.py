# Problem: https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        max = 2147483647
        min = -2147483648

        carry = 1 if x >= 0 else -1

        list_x = list(str(x))
        if carry == -1:
            list_x = list_x[1:]

        result = 0
        for index, value in enumerate(list_x):
            result += int(value) * pow(10, index)

        result *= carry
        if result in range(min, max):
            return result
        else:
            return 0

# input
i = -123324

solution = Solution()
output = solution.reverse(i)

print(output)
