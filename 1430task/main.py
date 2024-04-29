def count_products(a, b, n):
    if a < 0 or b < 0 or n < 0:
        raise ValueError("All inputs must be positive integers")
    if a == 0 or b == 0:
        raise ValueError("a and b mustn't be zero")
    if a == 1:
        return n, 0
    elif b == 1:
        return 0, n
    elif a == b:
        return n // a, 0
    else:
        flag = False
        if a < b:
            a, b = b, a
            flag = True
        x = 0
        min_ost = float('inf')
        t = min(n // a, b)
        for i in range(t + 1):
            tmp = (n - a * i) % b
            if min_ost > tmp:
                min_ost = tmp
                x = i
        if flag:
            return (n - a * x) // b, x
        else:
            return x, (n - a * x) // b

a, b, n = map(int, input().split())
quality, affordable = count_products(a, b, n)
print(f"{quality} {affordable}")
