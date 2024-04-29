def min_rows_count(N, diplomas):
    if N < 1 or N > 18:
        raise ValueError("Invalid number of diploma types")

    if len(diplomas) != N:
        raise ValueError("Number of diploma types does not match N")

    for num in diplomas:
        try:
            int(num)
        except ValueError:
            raise ValueError("Invalid number of diplomas")

        if int(num) < 1 or int(num) > 30:
            raise ValueError("Invalid number of diplomas")

    c = [0] * 31

    for num in diplomas:
        x = int(num)
        c[x] += 1

        if c[x] > 30:
            raise ValueError("Number of diplomas exceeds 30")

    ans = 0

    for i in range(2, 31):
        mn = min(c[i], c[i-1])
        c[i] -= mn
        c[i-1] -= mn
        ans += mn

    for i in range(1, 31):
        ans += c[i]

    return ans

N = int(input())
diplomas = input().split()
print(min_rows_count(N, diplomas))
