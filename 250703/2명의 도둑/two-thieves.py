def combi(l, idx, arr):
    global value
    if sum(arr) > C:
        return

    _sum = 0
    for e in arr:
        _sum += e ** 2
    
    value = max(value, _sum)

    for i in range(idx, len(l)):
        arr.append(l[i])
        combi(l, i + 1, arr)
        arr.pop()

def get_price(i, j):
    global value
    l = arr[i][j:j+M]
    value = 0
    combi(l, 0, [])

    return value
    
N, M, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
value = 0

for i in range(N):
    for j in range(N - M + 1):
        for k in range(i, N):
            for l in range(N - M + 1):
                if i == k and not (l >= j + M or j >= l + M):
                    continue

                v1 = get_price(i, j)
                v2 = get_price(k, l)

                ans = max(ans, v1 + v2)

print(ans)