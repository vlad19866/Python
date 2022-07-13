# Модуль circle содержит функции, которые выполняют
# вычисления, связанные с кругами.

import math

# функция area принимает радиус круга в качестве
# агрумента и возращает площадь круга
def area(radius):
    return math.pi * radius ** 2

# функция circumference принимает радиус круга
# и возвращает длину окружности

def circumference(radius):
    return 2 * math.pi * radius
