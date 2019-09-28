# input
n, m = (int(i) for i in input().split())
list_abc = [int(i) for i in input().split()]

result = [0, 0, 0]

if m == 0:
    if 0 in list_abc:
        result[list_abc.index(0)] = n
else:
    for i in range(3):
        if list_abc[i] != 0:
            result[i] = m // list_abc[i]

    found = False
    for i in range(result[0]):
        if found:
            break
        for j in range(result[1]):
            if found:
                break
            for k in range(result[2]):
                if m == i*list_abc[0] + j*list_abc[1] + k*list_abc[2]:
                    result = [i, j ,k]
                    found = True
                    break

    if found is not True:
        result = [-1, -1, -1]
                
print(" ".join(str(r) for r in result))