def cyclic_shifts_count_input(sequence):
    k = 0
    min_val = 0
    min_count = 0

    for c in sequence:
        if c not in ['(', ')']:
            raise ValueError("Invalid character in the input sequence")

        if c == '(':
            k += 1
        elif c == ')':
            k -= 1

        if k < min_val:
            min_count = 1
            min_val = k
        elif k == min_val:
            min_count += 1

    result = min_count if k == 0 else 0
    return result

cyclic_shifts_count_input(input().strip())

