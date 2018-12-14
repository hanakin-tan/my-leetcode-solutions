# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_str = list(s)
        result = 0;
        if len(s) <= 1:
            return len(s)

        sub_str = [];
        for c in list_str:
            if c not in sub_str:
                sub_str.append(c)
            else:
                result = max(len(sub_str), result)
                sub_str = sub_str[sub_str.index(c)+1:]
                sub_str.append(c)

        return max(len(sub_str), result)

# input 
input_str = "abcabcbb"

solution = Solution()
output_str = solution.lengthOfLongestSubstring(input_str)

# output
print(output_str)
