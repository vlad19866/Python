#По мере написания все большего количества функций черепашьей графики,
# следует рассмотреть возможность их хранения в модуле.
# Потом этот модуль можно импортировать в любую программу,
# в которой потребуется их применить.
# Например, в программе имеется модуль my_graphics.py,
# который содержит представленные ранее функции square, circle и line.
# Демонстрирует импортирование данного модуля и вызовы функций,
# которые он содержит.
import turtle

# функция square рисует квадрат
# параметры x и y - это координаты левого нижнего угла
# параметр widht - это ширина стороны квадрата
# параметр color - это цвет заливки в иде строки
def square(x, y, widht, color):
    turtle.penup()              # поднять перо
    turtle.goto(x, y)           # переместиться в заданное место
    turtle.fillcolor(color)     # задать цвет
    turtle.pendown()            # опустить перо
    turtle.begin_fill()         # начать заливку

    for count in range(4):
        turtle.forward(widht)
        turtle.left(90)
    turtle.end_fill()            # завершить заливку

# функция circle рисует круг
# параметры х и у - это координаты центральной точки
# параметр radius - это радиус ruheuf
# параметр color - это цвет заливки в виде строки

def circle(x, y, radius, color):
    turtle.penup()                  # поднять перо
    turtle.goto(x, y - radius)     # спозиционировать черепаху
    turtle.fillcolor(color)         # задать цвет заливки
    turtle.pendown()                # опустить перо
    turtle.begin_fill()             # начать заливку
    turtle.circle(radius)           # нарисовать круг
    turtle.end_fill()               # завершить заливку

# функция line рисует линии от (startX, startY) до (endX, endY)
# параметр color - это цвет линии
def line(startX, startY, endX, endY, color):
    turtle.penup()                  # поднять перо
    turtle.goto(startX, startY)     # переместить в начальную точку
    turtle.pendown()                # опустить перо
    turtle.pencolor(color)          # задать цвет заливки
    turtle.goto(endX, endY)         # нарисовать треугольник


