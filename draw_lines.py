#Функция применяется с целью модуляризации кода рисования отрезка
#прямой. Функция line определена и имеет следующие параметры:
# startx и startY - координаты Х, У начальной точки отрезка;
# endX и endY - координаты Х, У конечной точки отрезка;
# color - название цвета отрезка в виде строкового значения.
import turtle

# именованные констатнты
TOP_X = 0
TOP_Y = 100
BASE_LEFT_X = -100
BASE_LEFT_Y = -100
BASE_RIGHT_X = 100
BASE_RIGH_Y = -100

def main():
    turtle.hideturtle()
    line(TOP_X, TOP_Y, BASE_LEFT_X, BASE_LEFT_Y, 'red')
    line(TOP_X, TOP_Y, BASE_RIGHT_X, BASE_RIGH_Y, 'blue')
    line(BASE_LEFT_X, BASE_LEFT_Y, BASE_RIGHT_X, BASE_RIGH_Y, 'green')

# функция line рисует отрезок от (startX, startY) до (endX, endY)
# параметр color - это цвет отрезка
def line(startX, startY, endX, endY, color):
    turtle.penup()                      # поднять перо
    turtle.goto(startX, startY)         # переместиться в начальную точку
    turtle.pendown()                    # опустить перо
    turtle.pencolor(color)              # задать цвет заливки
    turtle.goto(endX, endY)             # нарисовать треугольник

# dspdfnm главную функцию
main()