n = int(input())
def recur(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
    return 1 + recur(n)

print(recur(n))