n = int(input())
arr = [int(input()) for _ in range(n)]
cnt = 0
_max = 0
for i in range(len(arr)):
    if i == 0 or arr[i] > arr[i-1]:
        cnt += 1
    else:
        cnt = 1
    _max = max(_max, cnt)
print(_max)