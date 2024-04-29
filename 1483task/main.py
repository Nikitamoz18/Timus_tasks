def calculate_scores(n):
    if type(n) != int or n < 1 or n > 1000:
        raise ValueError("n must be integer with n >= 1 and n <= 1000")
    min_ural_osliki = n - 1
    max_ural_t34 = (n - 1) // 2 * 3 + (n - 1) % 2
    return min_ural_osliki, max_ural_t34

n = int(input())
print(*calculate_scores(n))
