import pytest

# Импорт функции из оригинального скрипта
from main import days_lived


# Тест: Некорректный формат даты
def test_invalid_date_format():
    with pytest.raises(ValueError):
        days_lived("01.01.2000", "2000-01-02")


# Тест: Отсутствие ввода
def test_missing_input():
    with pytest.raises(ValueError):
        days_lived("01.01.2000", "")


# Тест: Пустые строки
def test_empty_strings():
    with pytest.raises(ValueError):
        days_lived("", "")


# Тест: Одна строка с недостаточным количеством элементов
def test_insufficient_elements():
    try:
        days_lived("01.01.2000", "02.01.2000")
    except ValueError:
        pytest.fail("Function raised unexpected ValueError")


# Тест: Некорректный порядок дат
def test_invalid_date_order():
    with pytest.raises(ValueError):
        days_lived("02.01.2000", "01.01.2000")
