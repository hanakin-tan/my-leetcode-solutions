# task-02


class Solution:
    def bi_valued(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_distance = 1

        len_a = len(A)

        if len_a <= 1:
            return len_a

        for i in range(0, len_a):
            values = [A[i]]
            is_break = 1
            for j in range(i+1, len_a):
                if A[j] in values:
                    continue

                if len(values) < 2:
                    values.append(A[j])
                else:
                    is_break = 0
                    break

            dis = j + is_break - i

            if max_distance < dis:
                max_distance = dis

        return max_distance


# input
A = [1, 2, 4, 3, 2, 2, 2]
print('***input***')
print(A)

solution = Solution()
output = solution.bi_valued(A)

print('***output***')
print(output)


