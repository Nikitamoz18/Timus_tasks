import pytest
from main import calculate_hit_point

# Тест для случая, когда вводятся некорректные координаты центра цистерны
def test_calculate_hit_point_invalid_tank_coordinates():
    with pytest.raises(ValueError):
        calculate_hit_point('a', 0, 5, 5, 0, 5, 5)

# Тест для случая, когда вводятся некорректные координаты пули
def test_calculate_hit_point_invalid_bullet_coordinates():
    with pytest.raises(ValueError):
        calculate_hit_point(0, 0, 5, 0, 0, 3001, 5)


# Тест для случая, когда вводятся некорректные координаты пули
def test_calculate_hit_point_invalid_bullet_coordinates_5():
    with pytest.raises(ValueError):
        calculate_hit_point(0, 0, 5, 'a', 0, 5, 5)

# Тест для случая, когда пуля находится внутри цистерны
def test_calculate_hit_point_bullet_inside_tank():
    assert calculate_hit_point(0, 0, 5, 0, 0, 0, 10) == "No way"

# Тест для случая, когда пуля движется параллельно касательной к цистерне
def test_calculate_hit_point_bullet_moves_along_tangent():
    assert calculate_hit_point(0, 0, 5, 0, 5, 10, 5) == "No way"
