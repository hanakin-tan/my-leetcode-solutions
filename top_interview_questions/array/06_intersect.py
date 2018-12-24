# problem: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = {}
        result = []

        for n in nums1:
            if n in dict1:
                dict1[n] += 1
            else:
                dict1[n] = 1

        print(dict1)
        for n in nums2:
            if n in dict1:
                if dict1[n]:
                    result.append(n)
                    dict1[n] -= 1

        return result


# input
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

solution = Solution()
output = solution.intersect(nums1, nums2)

# output
print(output)

