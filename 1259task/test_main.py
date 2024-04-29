import pytest
from main import count_stars

# Проверка на корректный ввод
def test_valid_input():
    assert count_stars(4) == 1
    assert count_stars(5) == 2
    assert count_stars(6) == 1
    assert count_stars(7) == 3

# Проверка на отрицательный ввод
def test_negative_input():
    with pytest.raises(ValueError):
        count_stars(-1)

# Проверка на буквенный ввод
def test_non_integer_input():
    with pytest.raises(ValueError):
        count_stars('abc')

# Проверка на минимальное значение N
def test_min_value_input():
    assert count_stars(3) == 1

# Проверка на максимальное значение N
def test_max_value_input():
    assert count_stars(100000) == 20000
