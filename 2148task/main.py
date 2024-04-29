import math


def calculate_hit_point(xc, yc, r, x1, y1, x2, y2):
    # Проверяем, что все входные значения являются числами
    if not all(isinstance(val, int) for val in [xc, yc, r, x1, y1, x2, y2]):
        raise ValueError("All input values must be integers")

    # Проверяем, что все входные значения по модулю не превосходят 3000
    if not all(abs(val) <= 3000 for val in [xc, yc, r, x1, y1, x2, y2]):
        raise ValueError("All input values must be integers not exceeding 3000")

    # Вычисляем расстояние от центра цистерны до точек начала и конца полета пули
    dist1 = math.sqrt(pow(x1 - xc, 2) + pow(y1 - yc, 2))
    dist2 = math.sqrt(pow(x2 - xc, 2) + pow(y2 - yc, 2))

    # Проверяем условия для отражения пули
    if dist1 != dist2 or 4 * (pow(x1 - xc, 2) + pow(y1 - yc, 2) - pow(r, 2)) <= pow(x2 - x1, 2) + pow(y2 - y1, 2):
        return "No way"
    else:
        # Вычисляем новые координаты попадания пули
        xm = (x1 + x2) / 2
        ym = (y1 + y2) / 2
        MO = math.sqrt(pow(xm - xc, 2) + pow(ym - yc, 2))
        MS = MO - r
        Xmo = xc - xm
        Ymo = yc - ym
        Xms = MS * Xmo / MO
        Yms = MS * Ymo / MO
        xs = xm + Xms
        ys = ym + Yms
        return "{:.6f} {:.6f}".format(xs, ys)


xc, yc, r = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
print(calculate_hit_point(xc, yc, r, x1, y1, x2, y2))
