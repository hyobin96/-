N = int(input())
dp = [0] * (N + 1)
dp[1], dp[2] = 1, 3
for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007
print(dp[N])