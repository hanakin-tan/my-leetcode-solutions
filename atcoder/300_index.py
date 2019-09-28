n, m = (int(i) for i in input().split())
ab = [[int(i) for i in input().split()] for i in range(n)]

print(ab)

for i in range(n):
    start = ab[i]
    yes = True
    for j in range(3):
        if start[1] == 0:
            yes = True
            break
        else:
            yes = False
            start = ab[start[1]-1]
    if yes:
        print('YES')
    else:
        print('NO')
