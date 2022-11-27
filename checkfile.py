                                                          # Importing Turtle Library and Math Library
import turtle
import math

                                                          # Inputting Values From User
base_len = int(input("Enter Base length of hexagonal prism: "))
axis_len = int(input("Enter Axis length of hexagonal prism: "))
axis_angle = int(input("Enter Angle of Inclination of Hexagonal Prism: "))

def x_axis(length):                                    #function used to draw x axis of a particular length
    c1 = turtle.Turtle()
    c1.color("black")
    c1.speed(c1s)
    c1.left(45)
    c1.forward(10)
    c1.backward(10)
    c1.right(90)
    c1.forward(10)
    c1.backward(10)
    c1.left(45)
    c1.forward(length)
    c1.left(135)
    c1.forward(10)
    c1.backward(10)
    c1.left(90)
    c1.forward(10)
    c1.hideturtle()

    x = turtle.Turtle()
    x.speed(xs)
    x.penup()
    x.setposition(-15,-5)
    x.pendown()
    style = ('Arial', 10, 'italic')
    x.write('x', font=style, align='center')
    x.hideturtle()

    y = turtle.Turtle()
    y.speed(ys)
    y.penup()
    y.setposition(length+15,-5)
    y.pendown()
    style = ('Arial', 10, 'italic')
    y.write('y', font=style, align='center')
    y.hideturtle()

def hexagon(base_len1, axis_len1, axis_angle1):                  # Hexagon function to create a hexagon
    hex = turtle.Turtle()
    hex.speed(hexs)
    hex.penup()
    hex.setposition(30, -((base_len1*1.732/2)+30))
    hex.left(60)
    hex.pendown()
    lightl = turtle.Turtle()
    lightl.speed(light1s)
    lightl.hideturtle()
    lightl.penup()
    lightl.setposition(hex.position())
    lightl.pendown()
    for i in range(6):                                                  #drawing hexagon
        hex.forward(base_len1)
        hex.right(60)
    hex.hideturtle()
    lightl.showturtle()
    hex.penup()
    for j in range(6):                                                 #drawing light lines1
        if (j != 1 and j != 2):
            lightl.color("cyan")
            lightl.setposition(hex.position())
            lightl.pendown()
            lightl.setposition(hex.xcor(), 0)
            lightl.penup()
        hex.forward(base_len1)
        hex.right(60)
    lightl.hideturtle()
    light2 = turtle.Turtle()
    light2.speed(light2s)
    light2.penup()
    rec1=hex.xcor()
    light2.setposition(hex.xcor(),0)
    light2.pendown()
    for k in range(6):                                           #Draw base length of axis hexagon
            if (k == 3):
                light2.color("black")
                light2.setposition(hex.xcor(), 0)
            hex.forward(base_len1)
            hex.right(60)

    rec2=light2.xcor()
    rec3 = rec2-rec1
    light2.left(90)
    light2.forward(axis_len1)
    light2.left(90)
    light2.setposition(rec1,axis_len1)
    light2.setposition(rec1,0)
    #light2.hideturtle()
    light2.penup()
    light2.setposition(rec1+(rec3/2),axis_len1+10)
    light2.left(90)
    light2.pendown()

    light2.speed(20)

    rec4 = light2.ycor()
    for i1 in range(math.ceil((base_len1+axis_len1)*0.15)):      # draw the axis of the hexagon
        light2.color("black", "black")
        light2.begin_fill()
        light2.circle(0.5)
        light2.end_fill()
        light2.penup()
        light2.forward(5)
        light2.pendown()
        light2.forward(8)
        light2.penup()
        light2.forward(3)
        light2.pendown()
    rec5 = light2.ycor()
    #print(rec4,rec5)
    #print(hex.position())

    light3 = turtle.Turtle()
    light3.penup()
    light3.speed(light3s)
    for m in range(6):                                         #Draw vertical light lines on axis hexagon
        if (m==1):
            light3.color("grey")
            light3.setposition(hex.xcor(), 0)
            l3=light3.xcor()
            light3.pendown()
            light3.setposition(hex.xcor(), axis_len1)
            light3.penup()
        if (m==2):
            light3.color("grey")
            light3.setposition(hex.xcor(), 0)
            l31=light3.xcor()
            light3.pendown()
            light3.setposition(hex.xcor(), axis_len1)
            light3.penup()

        hex.forward(base_len1)
        hex.right(60)
    light2.penup()
    light2.hideturtle()
    for i2 in range(7):                                         #draw horizontal light lines
        if (i2==2):

            light3.color("grey")
            light3.setposition(hex.position())
            light3.pendown()
            light3.setposition(len2, hex.ycor())
            hexcor1=light3.ycor()
            light3.penup()
        if (i2==4  ):
            light3.color("grey")
            light3.setposition(hex.position())
            light3.pendown()
            light3.setposition(len2, hex.ycor())
            hexcor2 = light3.ycor()
            light3.penup()
        if (i2==6 ):
            light3.color("grey")
            light3.setposition(hex.position())
            light3.pendown()
            light3.setposition(len2, hex.ycor())
            hexcor3=light3.ycor()
            light3.penup()
        if (i2==3):

            light2.setposition(hex.xcor(),0)


        hex.forward(base_len1)
        hex.right(60)

    light3.hideturtle()
    light2.setposition(light2.xcor()+50,light2.ycor())     #moves 50 ahead of the axis rectangle
    l2pos = light2.position()
    l2posx = light2.xcor()
    light2.showturtle()
    light2.left(90+axis_angle1)
    light2.pendown()
    for i3 in range(math.ceil((axis_len1)*0.15)):           #Draws inclined axis
        light2.color("black", "black")
        light2.begin_fill()
        light2.circle(0.5)
        light2.end_fill()
        light2.penup()
        light2.forward(5)
        light2.pendown()
        light2.forward(8)
        light2.penup()
        light2.forward(3)
        light2.pendown()

    rec6=rec3/2
                                                        #drawing an inclined hexagon
    light2.penup()
    light2.setposition(l2pos)
    light2.speed(100)
    light2.forward(1)
    for i4 in range(1000):
        light2.forward(fcheck)
        light2.right(90)
        light2.forward(rec6)

        if (math.floor(light2.ycor())==0):
            x1 = light2.position()
            d1dx = light2.xcor()
            d1dy = light2.ycor()
            light2.speed(light2s)
            light2.pendown()
            light2.backward(rec3)
            x4 = light2.position()
            a1dx = light2.xcor()
            a1dy = light2.ycor()
            light2.left(90)
            light2.forward(axis_len1)
            x5 = light2.position()
            d11x = light2.xcor()
            d11y = light2.ycor()
            light2.right(90)
            light2.forward(rec3)
            x8 = light2.position()
            d41x = light2.xcor()
            d41y = light2.ycor()
            light2.right(90)
            light2.forward(axis_len1)
            light2.penup()

            break

        else:
            light2.backward(rec6)
            light2.left(90)

                                                    #draw inclined light lines
    light2.color("cyan")
    hl = rec1-l3
    hl1 = rec1-l31
    light2.right(90)
    light2.backward(hl)
    x2 = light2.position()
    c1dx = light2.xcor()
    c1dy = light2.ycor()
    e1dx = light2.xcor()
    e1dy = light2.ycor()
    light2.pendown()
    light2.right(90)
    light2.forward(axis_len1)
    x7 = light2.position()
    d31x = light2.xcor()
    d31y = light2.ycor()
    d51x = light2.xcor()
    d51y = light2.ycor()
    light2.penup()
    light2.backward(axis_len1)
    light2.left(90)
    light2.forward(hl)
    light2.backward(hl1)
    x3 = light2.position()
    b1dx = light2.xcor()
    b1dy = light2.ycor()
    f1dx = light2.xcor()
    f1dy = light2.ycor()
    light2.pendown()
    light2.right(90)
    light2.forward(axis_len1)
    x6 = light2.position()
    d21x = light2.xcor()
    d21y = light2.ycor()
    d61x = light2.xcor()
    d61y = light2.ycor()
    light2.penup()

                                                 #draw vertical light lines for inclined rectangle
    light2.setposition(x1)
    x11 = light2.xcor()
    light2.setheading(-90)
    light2.pendown()
    light2.color("grey")
    light2.setposition(light2.xcor(),hexcor2)
    light2.penup()

    light2.setposition(x2)
    x22 = light2.xcor()
    light2.setheading(-90)
    light2.pendown()
    light2.color("grey")
    light2.setposition(light2.xcor(),hexcor2)
    light2.penup()

    light2.setposition(x3)
    x33 = light2.xcor()
    light2.setheading(-90)
    light2.pendown()
    light2.color("grey")
    light2.setposition(light2.xcor(),hexcor2)
    light2.penup()

    light2.setposition(x4)
    x44 = light2.xcor()
    light2.setheading(-90)
    light2.pendown()
    light2.color("grey")
    light2.setposition(light2.xcor(),hexcor2)
    light2.penup()

    light2.setposition(x5)
    x55 = light2.xcor()
    light2.setheading(-90)
    light2.pendown()
    light2.color("grey")
    light2.setposition(light2.xcor(), hexcor2)
    light2.penup()

    light2.setposition(x6)
    x66 = light2.xcor()
    light2.setheading(-90)
    light2.pendown()
    light2.color("grey")
    light2.setposition(light2.xcor(), hexcor2)
    light2.penup()

    light2.setposition(x7)
    x77 = light2.xcor()
    light2.setheading(-90)
    light2.pendown()
    light2.color("grey")
    light2.setposition(light2.xcor(), hexcor2)
    light2.penup()

    light2.setposition(x8)
    x88 = light2.xcor()
    light2.setheading(-90)
    light2.pendown()
    light2.color("grey")
    light2.setposition(light2.xcor(), hexcor2)
    light2.penup()


                                                     #drawing top view hexagon1
    light2.color("black")
    light2.setposition(x22,hexcor2)
    c1x = light2.xcor()+7
    c1y = light2.ycor()-12
    light2.pendown()
    light2.setposition(x33,hexcor2)
    b1x = light2.xcor()+3
    b1y = light2.ycor() - 12
    light2.setposition(x44,hexcor3)
    a1x = light2.xcor() -5
    a1y = light2.ycor()
    light2.setposition(x33, hexcor1)
    f1x = light2.xcor()+3
    f1y = light2.ycor()
    light2.setposition(x22, hexcor1)
    e1x = light2.xcor() + 5
    e1y = light2.ycor()
    light2.color("red")
    light2.setposition(x11,hexcor3)
    d1x = light2.xcor() +8
    d1y = light2.ycor()
    light2.setposition(x22,hexcor2)
    light2.color("black")
    light2.penup()

                                                            #hexagon 2
    light2.setposition(x55, hexcor3)
    light2.pendown()
    light2.setposition(x66, hexcor1)
    light2.setposition(x77, hexcor1)
    light2.setposition(x88, hexcor3)
    light2.setposition(x77, hexcor2)
    light2.setposition(x66, hexcor2)
    light2.setposition(x55, hexcor3)
    light2.hideturtle()

    # Naming the projection of solid

    alpha.penup()
    #alpha.hideturtle()
    for i in range(6):  # position
        if (i == 5):
            ax = hex.xcor() - 4
            ay = hex.ycor() - 3
            adx = hex.xcor() - 5
            ady = 0
            dx1 = hex.xcor() +1
            dy1 = axis_len1
        if (i == 4):
            bx = hex.xcor() - 2
            by = hex.ycor() - 11
            fdx = hex.xcor()
            fdy = 0
            bdx = hex.xcor()
            bdy = -12
            dx2 = hex.xcor() - 2
            dy2 = axis_len1
            dx6 = hex.xcor() - 2
            dy6 = axis_len1-12
        if (i == 3):
            cx = hex.xcor() + 4
            cy = hex.ycor() - 12
            edx = hex.xcor()
            edy = 0
            cdx = hex.xcor()
            cdy = -12
            dx3 = hex.xcor() - 2
            dy3 = axis_len1
            dx5 = hex.xcor() - 2
            dy5 = axis_len1 - 12
        if (i == 2):
            dx = hex.xcor() + 7
            dy = hex.ycor() - 3
            ddx = hex.xcor() +10
            ddy = 0
            dx4 = hex.xcor() + 7
            dy4 = axis_len1
        if (i == 1):
            ex = hex.xcor() + 3
            ey = hex.ycor()
        if (i == 0):
            fx = hex.xcor()+1
            fy = hex.ycor()-2
        hex.forward(base_len1)
        hex.right(60)

    alpha.setposition(l2posx + 30, -1)                 # print theta = given angle
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("θ="+str(axis_angle1), font=style, align='right')
    alpha.penup()
    alpha.hideturtle()
                                                      # Naming the marked points
    alpha.setposition(ax, ay)
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("a", font=style, align='right')       # a
    alpha.penup()
    alpha.setposition(bx, by)
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("b", font=style, align='right')       # b
    alpha.penup()
    alpha.setposition(cx, cy)
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("c", font=style, align='right')       # c
    alpha.penup()
    alpha.setposition(dx, dy)
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("d", font=style, align='right')       # d
    alpha.penup()
    alpha.setposition(ex, ey)
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("e", font=style, align='right')       # e
    alpha.penup()
    alpha.setposition(fx, fy)
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("f", font=style, align='right')       # f
    alpha.penup()

    alpha.setposition(adx, ady)
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("a'", font=style, align='right')  # a'
    alpha.penup()
    alpha.setposition(bdx, bdy)
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("b'", font=style, align='right')  # b'
    alpha.penup()
    alpha.setposition(fdx, fdy)
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("f'", font=style, align='right')  # f'
    alpha.penup()
    alpha.setposition(cdx, cdy)
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("c'", font=style, align='right')  # c'
    alpha.penup()
    alpha.setposition(edx, edy)
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("e'", font=style, align='right')  # e'
    alpha.penup()
    alpha.setposition(ddx, ddy)
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("d'", font=style, align='right')  # d'
    alpha.penup()

    alpha.setposition(dx1, dy1)
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("1'", font=style, align='right')  # 1'
    alpha.penup()
    alpha.setposition(dx2, dy2)
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("2'", font=style, align='right')  # 2'
    alpha.penup()
    alpha.setposition(dx6, dy6)
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("6'", font=style, align='right')  # 6'
    alpha.penup()
    alpha.setposition(dx3, dy3)
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("3'", font=style, align='right')  # 3'
    alpha.penup()
    alpha.setposition(dx5, dy5)
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("5'", font=style, align='right')  # 5'
    alpha.penup()
    alpha.setposition(dx4, dy4)
    alpha.pendown()
    style = ('Arial', 7)
    alpha.write("4'", font=style, align='right')  # 4'
    alpha.penup()

    alpha.setposition(a1dx,a1dy)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("a1'", font=style, align='right')      # a1'
    alpha.penup()
    alpha.setposition(b1dx+22,b1dy-2)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("b1',f1'", font=style, align='right')  # b1', f1'
    alpha.penup()
    alpha.setposition(c1dx+22,c1dy-2)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("c1',e1'", font=style, align='right')   # c1', e1'
    alpha.penup()
    alpha.setposition(d1dx+20,d1dy-2)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("d1'", font=style, align='right')      # d1'
    alpha.penup()

    alpha.setposition(d11x,d11y-5)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("11'", font=style, align='right')      # 11'
    alpha.penup()
    alpha.setposition(d21x+22,d21y-2)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("21',61'", font=style, align='right')  # 21', 61'
    alpha.penup()
    alpha.setposition(d31x+22,d31y-2)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("31',51'", font=style, align='right')   # 31', 51'
    alpha.penup()
    alpha.setposition(d41x+12,d41y-5)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("41'", font=style, align='right')      # 41'
    alpha.penup()

    alpha.setposition(a1x,a1y)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("a1", font=style, align='right')      # a1
    alpha.penup()
    alpha.setposition(b1x, b1y)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("b1", font=style, align='right')      # b1
    alpha.penup()
    alpha.setposition(c1x, c1y)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("c1", font=style, align='right')      # c1
    alpha.penup()
    alpha.setposition(d1x, d1y)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("d1", font=style, align='right')      # d1
    alpha.penup()
    alpha.setposition(e1x, e1y)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("e1", font=style, align='right')      # e1
    alpha.penup()
    alpha.setposition(f1x, f1y)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("f1", font=style, align='right')      # f1
    alpha.penup()

    alpha.setposition(x55,hexcor3-12)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("11", font=style, align='right')      # 11
    alpha.penup()
    alpha.setposition(x66, hexcor2-12)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("21", font=style, align='right')      # 21
    alpha.penup()
    alpha.setposition(x77+6, hexcor2-12)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("31", font=style, align='right')      # 31
    alpha.penup()
    alpha.setposition(x88+10, hexcor3)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("41", font=style, align='right')      # 41
    alpha.penup()
    alpha.setposition(x77+8, hexcor1)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("51", font=style, align='right')      # 51
    alpha.penup()
    alpha.setposition(x66, hexcor1)
    alpha.pendown()
    style = ('Arial', 6)
    alpha.write("61", font=style, align='right')      # 61
    alpha.penup()

    alpha.setposition(200,300)
    alpha.pendown()
    style = ('Arial', 20, 'underline')
    alpha.write("Projection Of Solids (Hexagonal Prism)", font=style, align='right')  # 61
    alpha.penup()

                                                                #Turtle speeds
alpha = turtle.Turtle()
alpha.hideturtle()
alpha.penup()
alphas=10
alpha.speed(alphas)
speeds=10
c1s=speeds
xs=speeds
ys=speeds
hexs=speeds
light1s=speeds
light2s=speeds
light3s=speeds

                                                      #forward check distance
fcheck=1

len2=base_len*10                                      #light lines length in x direction
lenl = base_len*10                                    #x-axis length

x_axis(lenl)                               #function to draw x axis of a particular length

hexagon(base_len,axis_len,axis_angle)      #function to draw hexagon by inputting specific parameters

turtle.done()