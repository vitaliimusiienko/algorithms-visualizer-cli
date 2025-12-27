import turtle


def draw_tree(t: turtle.Turtle, length: float, level: int):
    if level == 0:
        return

    t.forward(length)

    t.left(45)
    draw_tree(t, length * 0.7, level - 1)

    t.right(90)
    draw_tree(t, length * 0.7, level - 1)

    t.left(45)
    t.backward(length)


def pythagoras_tree(level: int, length: int = 100):
    screen = turtle.Screen()
    screen.title("Pythagoras Tree")

    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)
    t.penup()
    t.backward(length)
    t.pendown()

    draw_tree(t, length, level)

    screen.mainloop()