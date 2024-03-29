import turtle as t


def koch(size, n):
    t.pendown()
    if n == 0:
        t.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            t.left(angle)
            koch(size / 3, n - 1)


def main():
    t.setup(800, 600)
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    t.pensize(5)
    t.pencolor('purple')
    n = 3
    koch(200, n)
    t.right(120)
    koch(200, n)
    t.right(120)
    koch(200, n)
    t.right(120)
    t.hideturtle()
    t.done()


main()
