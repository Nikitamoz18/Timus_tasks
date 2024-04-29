import pytest
from main import solve

# Проверка на отрицательный ввод
def test_negative_input():
    with pytest.raises(ValueError):
        solve(-1)

# Проверка на буквенный ввод
def test_non_integer_input():
    with pytest.raises(ValueError):
        solve('abc')

# Проверка на граничные случаи (нулевой ввод)
def test_zero_input():
    with pytest.raises(ValueError):
        solve(0)

# Проверка на граничные случаи (оба аргумента равны 1)
def test_min_value_input():
    assert solve(1) == False

# Тестирование корректного ввода
def test_valid_input():
    assert solve(4) == False
    assert solve(6) == False
    assert solve(7) == True
    assert solve(30) == True

