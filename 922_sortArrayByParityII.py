# problem: https://leetcode.com/problems/sort-array-by-parity-ii/


class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        len_A = len(A)
        result = [0] * len_A

        index_odd = 0
        index_even = 1

        for a in A:
            if a % 2:
                result[index_even] = a
                index_even += 2
            else:
                result[index_odd] = a
                index_odd += 2

        return result


# input
A = [4, 2, 5, 7]
print(A)

solution = Solution()
output = solution.sortArrayByParityII(A)

# output
print(output)
