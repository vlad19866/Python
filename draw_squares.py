#Использование черепахи для рисования фигуры обычно требует
# нескольких шагов. Предположим, что вы хотите нарисовать
# квадрат со стороной 100 пикселов, заполненный синим цветом.
import turtle

def main():
    turtle.hideturtle()
    circle(0, 0, 100, 'red')
    circle(-150, -75, 50, 'blue')
    circle(-200, 150, 75, 'green')

# функция circule рисует круг
# параметр x и y - это координаты центральной точки
# параметры radius - это радиус круга.
# параметры color - это цвет заливки в виде строки

def circle(x, y, radius, color):
    turtle.penup()                  # поднять перо
    turtle.goto(x, y - radius)      # спозиционировать церепаху
    turtle.fillcolor(color)         # задать цвет заливки
    turtle.pendown()                # опустить перо
    turtle.begin_fill()             # начать заливку
    turtle.circle(radius)           # нарисовать круг
    turtle.end_fill()               # завершить заливку

# вызвать главную функцию
main()

turtle.exitonclick()  # выход по нажатию кнопки
