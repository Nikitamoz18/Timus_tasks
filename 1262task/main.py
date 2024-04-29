def count_rim_digit(input_str):
    v = [0, 1, 2, 3, 2, 1, 2, 3, 4, 2]
    ans = 0

    for char in input_str:
        ans += v[int(char)]
    return ans

valid_input = 0
while not valid_input:
    try:
        input_str = input()
        n = int(input_str)
        if n <= 0:
            print("The number must be greater than 0")
        else:
            valid_input = 1
    except ValueError:
        print("Invalid input. Please enter an integer.")

ans = count_rim_digit(input_str)
print(ans)
