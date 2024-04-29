def solve(N):
    if type(N) != int or N < 1 or N > 2 ** 25 - 1:
        raise ValueError("n must be integer with n >= 1 and n <= 2^25 - 1")
    pow2 = 0
    while N % 2 == 0:
        N //= 2
        pow2 += 1
    if pow2 % 2 == 1:
        if N == 1:
            return True
        else:
            for i in range(2, int(N ** 0.5) + 1):
                if N % i == 0:
                    return True
        return False
    elif pow2 % 2 == 0:
        return N > 1


T = int(input())
for _ in range(T):
    N = int(input())
    print("YES" if solve(N) else "NO")
