import pytest
from main import cyclic_shifts_count_input

# Тест для случая, когда строка состоит только из открывающейся скобки
def test_cyclic_shifts_count_only_opening_bracket():
    assert cyclic_shifts_count_input("(") == 0

# Тест для случая, когда строка состоит только из закрывающейся скобки
def test_cyclic_shifts_count_only_closing_bracket():
    assert cyclic_shifts_count_input(")") == 0

# Тест для случая, когда строка содержит некорректные символы (не '(' и не ')')
def test_cyclic_shifts_count_invalid_input():
    with pytest.raises(ValueError):
        cyclic_shifts_count_input("abc")

# Тест для случая, когда строка имеет неправильное количество открывающих и закрывающих скобок
def test_cyclic_shifts_count_invalid_sequence():
    assert cyclic_shifts_count_input("((())") == 0

# Тест для случая, когда строка требует смещения, чтобы стать правильной скобочной последовательностью
def test_cyclic_shifts_count_shift_required():
    assert cyclic_shifts_count_input(")()()(") == 3
