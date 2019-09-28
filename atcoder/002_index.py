# input
# 3

# 1 2 5
# 4 1 4

# output
# 3
n = int(input())

array_a = list(int(i) for i in input().split())
array_b = list(int(i) for i in input().split())

# print(array_a)
# print(array_b)

array_a.sort()
array_b.sort()

result = 0
for i in range(n):
    result += abs(array_a[i] - array_b[i])

print(result)
