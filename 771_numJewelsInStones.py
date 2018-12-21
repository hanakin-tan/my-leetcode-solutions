# problem: https://leetcode.com/problems/jewels-and-stones/


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        result = 0
        for j in J:
            result += len(S.split(j)) - 1
        return result


# input
J = "aA"
S = "aAAbbbb"
print("***input***")
print(J)
print(S)

solution = Solution()
output = solution.numJewelsInStones(J, S)

# output
print("***output***")
print(output)
