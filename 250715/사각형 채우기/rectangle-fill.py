N = int(input())
dp = [0] * (N + 1)
dp[1], dp[2] = 1, 2
for i in range(3, N + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 10007

print(dp[N])