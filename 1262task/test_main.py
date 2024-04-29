import pytest
from main import count_rim_digit

# Тест для случая, когда N = 1
def test_count_rim_digit_1():
    assert count_rim_digit("1") == 1

# Тест для случая, когда N максимально допустимое значение
def test_count_rim_digit_max():
    assert count_rim_digit("102003") == 6

# Тест для случая, когда N состоит из одной цифры
def test_count_rim_digit_N():
    assert count_rim_digit("5") == 1

# Тест для случая, когда N состоит из нескольких цифр, все из которых одинаковы
def test_count_rim_digit_equal():
    assert count_rim_digit("555") == 3

# Тест для случая, когда N меньше 0
def test_count_rim_digit_negative_input():
    with pytest.raises(ValueError):
        count_rim_digit("-10")

# Тест для случая, когда N состоит из букв
def test_count_rim_digit_invalid_input():
    with pytest.raises(ValueError):
        count_rim_digit("ABC")
