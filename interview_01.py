# problem: f(n) = f(n-1) + f(n-2)


class Solution:
    def fib(self, n):
        if n < 2:
            return n

        n_2 = 0
        n_1 = 1
        for i in range(2, n):
            temp = n_1
            n_1 = n_1 + n_2
            n_2 = temp

        return n_1 + n_2

solution = Solution()

print(solution.fib(1))
print(solution.fib(2))
print(solution.fib(3))
print(solution.fib(4))
print(solution.fib(5))
print(solution.fib(6))
print(solution.fib(300000))
