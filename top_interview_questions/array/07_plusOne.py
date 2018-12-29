# problem: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            temp = digits[i] + 1
            carry = temp // 10
            digits[i] = temp % 10
            if not carry:
                return digits

        if carry:
            digits[:] = [carry] + digits

        return digits


# input
digits = [1, 2, 3]

solution = Solution()
output = solution.plusOne(digits)

# output
print(output)
