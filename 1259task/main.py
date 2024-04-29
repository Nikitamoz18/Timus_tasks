def count_stars(N):
    if type(N) != int or N < 3 or N > 100000:
        raise ValueError("n must be integer and 3<=n<=100000")
    def nod(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    ans = 0
    for i in range(1, N // 2 + 1):
        if nod(i, N) == 1:
            ans += 1
    return ans


N = int(input())
print(count_stars(N))
