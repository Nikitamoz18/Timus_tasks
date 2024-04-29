import pytest
from main import calculate_result

def test_valid_input():
    assert calculate_result(1, 0) == 1

# Проверка на неверный ввод (оба аргумента равны 0)
def test_invalid_input():
    with pytest.raises(ValueError):
        calculate_result(0, 0)

# Проверка на неверный ввод (оба аргумента не являются числами)
def test_invalid_input_2():
    with pytest.raises(ValueError):
        calculate_result('abc', 'def')

# Проверка на граничные случаи (оба аргумента отрицательные)
def test_negative_input():
    with pytest.raises(ValueError):
        calculate_result(-1, -1)

# Проверка на граничные случаи (оба аргумента равны 1)
def test_boundary_cases():
    assert calculate_result(1, 1) == 2
