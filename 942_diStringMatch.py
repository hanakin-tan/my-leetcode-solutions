# Problem: https://leetcode.com/problems/di-string-match/


class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        max_v = len(S)
        min_v = 0
        result = []
        for s in S:
            if s is 'I':
                result.append(min_v)
                min_v += 1
            else:
                result.append(max_v)
                max_v -= 1
        result.append(min_v)
        return result


# input
S = 'IDID'

solution = Solution()
output = solution.diStringMatch(S)

print(output)