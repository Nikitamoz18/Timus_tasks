import pytest
from main import min_rows_count


def test_min_rows_count_single_type():
    # Тест для случая, когда все дипломы одного типа
    assert min_rows_count(1, ['5']) == 1


def test_min_rows_count_multiple_types():
    # Тест для случая, когда дипломы разных типов, но не требуют дополнительных рядов
    assert min_rows_count(3, ['2', '2', '2']) == 3


def test_min_rows_count_invalid_rows():
    # Тест для случая, когда требуется дополнительные ряды
    with pytest.raises(ValueError):
        min_rows_count(3, ['-1', '2', '1'])


def test_min_rows_count_invalid_input():
    # Тест для случая некорректного ввода
    with pytest.raises(ValueError):
        min_rows_count(2, ['a', '2'])


def test_min_rows_count_symmetric_rows():
    # Тест для случая, когда дипломов разных типов, но все уникальны
    assert min_rows_count(6, ['6', '5', '4', '3', '2', '1']) == 3
