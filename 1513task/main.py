def calculate_result(n, k):
    if type(n) != int or type(k) != int or n < 1 or k < 0:
        raise ValueError("Both n and k must be integers with n >= 1 and k >= 0")

    dp = [0] * (n + k + 1)
    sum_val = 1
    res = 0

    dp[k] = 1

    for i in range(1, n + 1):
        dp[k + i] = sum_val
        sum_val += dp[k + i] + (-dp[i - 1])

    for i in range(k + 1):
        res += dp[n + i]

    return res

n, k = map(int, input().split())
print(calculate_result(n, k))
