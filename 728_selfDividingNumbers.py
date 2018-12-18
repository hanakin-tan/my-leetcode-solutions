# Problem: https://leetcode.com/problems/self-dividing-numbers/


class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        if right < 10:
            return [i for i in range(left, right+1)]
        else:
            result = [i for i in range(left, 10)]

        start = 11 if left <= 11 else left
        for i in range(start, right+1):
            is_self_devided = True
            for j in set(str(i)):
                j = int(j)
                if j is 0 or i % j is not 0:
                    is_self_devided = False
                    break

            if is_self_devided:
                result.append(i)

        return result

# input
left = 1
right = 22

solution = Solution()
output = solution.selfDividingNumbers(left, right)

# output
print(output)
