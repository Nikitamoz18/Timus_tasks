import pytest
from main import calculate_scores

def test_negative_input():
    with pytest.raises(ValueError):
        calculate_scores(-1)

def test_non_integer_input():
    with pytest.raises(ValueError):
        calculate_scores('abc')

# Проверка на граничные случаи (оба аргумента отрицательные)
def test_negative_input():
    with pytest.raises(ValueError):
        calculate_scores(0)

# Проверка на граничные случаи (оба аргумента равны 1)
def test_max_value_input():
    assert calculate_scores(1000) == (999, 1498)

# Проверка на минимальное значение N
def test_min_value_input():
    assert calculate_scores(1) == (0, 0)
