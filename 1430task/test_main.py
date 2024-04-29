import pytest
from main import count_products


# Тест для случая, когда вводится отрицательное число
def test_solution_negative_input():
    with pytest.raises(ValueError):
        count_products(-10, 3, 20)

# Тест для случая, когда один из параметров a или b равен нулю
def test_solution_a_or_b_zero():
    with pytest.raises(ValueError):
        count_products(0, 5, 20)

    with pytest.raises(ValueError):
        count_products(5, 0, 20)

# Тест для случая, когда A и B равны 1, а N положительное число
def test_solution_A_and_B_equal_1():
    assert count_products(1, 1, 10) == (10, 0)

# Тест для случая, когда A равно 1, а B и N положительные числа
def test_solution_A_equal_1():
    assert count_products(1, 5, 20) == (20, 0)

# Тест для случая, когда B равно 1, а A и N положительные числа
def test_solution_B_equal_1():
    assert count_products(5, 1, 20) == (0, 20)
