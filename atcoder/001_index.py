# input
n = int(input())
array = list(int(i) for i in input().split())
array_set = set(array)

if n != len(array):
    print("NO")
elif n == len(array_set):
    print("YES")
else:
    print("NO")
