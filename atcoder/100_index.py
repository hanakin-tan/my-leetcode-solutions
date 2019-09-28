# input
n, k = (int(i) for i in input().split())
a_n = (int(i) for i in input().split())

time = 0
for a in a_n:
    if a > k:
        time += a - k
    else:
        continue

print(time)