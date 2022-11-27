# Naming the projection of solid
alpha = turtle.Turtle()
alpha.penup()
alpha.hideturtle()
for i in range(6):  # position
    if (i == 5):
        alpha.setposition(hex.xcor() - 5, hex.ycor() - 3)
        alpha.pendown()
        style = ('Arial', 7, 'italic')
        alpha.write('a', font=style, align='center')
        alpha.penup()
    if (i == 4):
        alpha.setposition(hex.xcor() - 3, hex.ycor() - 12)
        alpha.pendown()
        style = ('Arial', 7, 'italic')
        alpha.write('b', font=style, align='center')
        alpha.penup()
    if (i == 3):
        alpha.setposition(hex.xcor() + 3, hex.ycor() - 12)
        alpha.pendown()
        style = ('Arial', 7, 'italic')
        alpha.write('c', font=style, align='center')
        alpha.penup()
    if (i == 2):
        alpha.setposition(hex.xcor() + 5, hex.ycor() - 3)
        alpha.pendown()
        style = ('Arial', 7, 'italic')
        alpha.write('d', font=style, align='center')
        alpha.penup()
    if (i == 1):
        alpha.setposition(hex.xcor() + 1, hex.ycor() + 1)
        alpha.pendown()
        style = ('Arial', 7, 'italic')
        alpha.write('e', font=style, align='center')
        alpha.penup()
    if (i == 0):
        alpha.setposition(hex.xcor() - 1, hex.ycor() + 1)
        alpha.pendown()
        style = ('Arial', 7, 'italic')
        alpha.write('f', font=style, align='center')
        alpha.penup()

    hex.forward(base_len1)
    hex.right(60)
