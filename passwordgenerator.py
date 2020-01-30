import turtle
# screen
wn = turtle.Screen()
wn.title("Calculator")
wn.bgcolor("black")
wn.setup(width=500, height=500)
wn.tracer(0, delay=0.1)  # Turns off the screen updates

# picking operation
pen = turtle.Turtle()
pen.color("white")
pen.goto(-75, 100)

pen.write("Co chcesz obliczyć:\n>Pole powierzchni(p)\n>Stopnie Celsjusza lub Fahrenheita(s)\n>Pitagoras(pitagoras)")
pen.hideturtle()
pen.isvisible()
pen.shapesize()

pen2 = turtle.Turtle()
pen2.color("white")
pen2.hideturtle()
pen2.isvisible()

pen3 = turtle.Turtle()
pen3.color("white")
pen3.goto(-75, 0)
pen3.hideturtle()
pen3.isvisible()

pen4 = turtle.Turtle()
pen4.color("white")
pen4.goto(-75, -100)

pen5 = turtle.Turtle()
pen5.color("white")
pen5.goto(x=0, y=-150)

pen6 = turtle.Turtle()
pen6.color("white")
pen6.goto(-113, -100)

koniec = False
while not koniec:
    l = turtle.textinput("Liczba", "litera")
    if l == "p":
        pen2.goto(-75, 0)
        pen2.write("Pole powierzchni")
        pen2.write(
            "Obliczasz pola powierzchni:\n>Trójkąt(x)\n>Kwadrat(2x)\n>Romb(3x)\n>Równoległobok(5x)\n>Prostokąt(4x)\n")
        x = turtle.textinput("Operacja", "Wpisz x, 2x, 3x, 4x lub 5x")
        if x == "x":
            a = turtle.numinput("Wymiary podstawy", "podaj:")
            h = turtle.numinput("Wysokość: ", "podaj:")
            pp = int(a * h) / 2
        elif x == "2x":
            a = turtle.numinput("Wymiar podstawy: ")
            pp = int(a * a)
        # romb
        elif x == "3x":
            x = turtle.textinput(
                "Chcesz skorzystać z długości przekątnych, czy, z długości podstawy i wysokości rombu\nwpisz p jeśli Chcesz skorzystać z długości przekątnych\nlub\n d jeśli chcesz skorzystać z długości podstawy i wysokości rombu: ")
            if x == "p":
                e = turtle.numinput("Podaj długość jednej przekątnej: ", 'podaj')
                f = turtle.numinput("Podaj długość drugiej przekątnej: ", 'podaj')
                pp = int(e * f) / 2
            elif x == "d":
                a = turtle.numinput("Podaj długość podstawy: ", 'podaj')
                h = turtle.numinput("Podaj wysokość: ", 'podaj')
                pp = a * h
        # równoległobok
        elif x == "5x":
            a = turtle.numinput("Podaj długośc podastawy równoległoboku: ", 'podaj')
            h = turtle.numinput("Podaj wysokość równoległoboku: ", 'podaj')
            pp = a * h
        # prostokąt
        elif x == "4x":
            a = turtle.numinput("Podaj długość dłuższego boku: ", 'podaj')
            b = turtle.numinput("Podaj długość krótszego boku: ", 'podaj')
            pp = a * b
        else:
            pen2.write("Niepoprawny wybór!")
        pen6.write("Wynik=")
        pen4.write(pp)
        pen3.hideturtle()
    elif l == "s":
        pen2.goto(-50, 0)
        pen2.write("Stopnie")
        pen3.write('Wpisz co chcesz zamienic:\nCelsjusze(C) na Fahrenheita(F), czy na odwrót\n>')
        odp = turtle.textinput("C, lub F", '  ')
        if odp == "C":
            x = turtle.numinput("Wpisz stopnie Celsjusza ", ' ')
            y = str(1.800 * x + 32)
            pen3.write("Po zamianie: " + y)
        elif odp == "F":
            x = turtle.numinput("Wpisz stopnie Fahrenheita ", ' ')
            y = str(float(x - 32) / 1.8)
            pen3.write("Po zamianie: " + y)
        if odp == "c":
            x = turtle.numinput("Wpisz stopnie Celsjusza ", ' ')
            y = str(1.800 * x + 32)
            pen3.write("Po zamianie: " + y)
        elif odp == "f":
            x = turtle.numinput("Wpisz stopnie Fahrenheita ", ' ')
            y = str(float(x - 32) / 1.8)
            pen3.write("Po zamianie: " + y)
    elif l == "pitagoras":
        pen4.goto(-75, -50)
        x = pen3.write("obliczasz przeciwprostokątną", '')
        a = turtle.numinput("Jedna przyprostokątna: ", '')
        b = turtle.numinput("Druga przyprostokątna: ", '')
        pp = a * a + b * b
        pen4.write(pp)
    pen2.hideturtle()
    pen4.hideturtle()
    pen5.write("Chcesz wykonac kolejne działanie")
    m = turtle.textinput("Chcesz wykonać kolejne działanie?", "Tak, lub nie")
    if m == "nie":
        koniec = True
        break
    elif koniec != "tak":
        pen5.write("Niepoprawny wybór")

    pen.clear()
    pen3.clear()
    pen4.clear()
    pen5.clear()

while True:
    wn.update()