import turtle
import math
# screen
wn = turtle.Screen()
wn.title("Calculator")
wn.bgcolor("light green")
wn.setup(width=500, height=500)
wn.tracer(0, delay=0.1)  # Turns off the screen updates

# pen's
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.color("black")
pen.goto(x=-75, y=50)

# asking
pen.write("Co chcesz obliczyć:\n> Pole powierzchni (pp)\n> Stopnie Celsjusza lub Fahrenheita (s)\n> Pitagoras (pitagoras)\n> Pierwiastek (p)\n> Przekątna kwadratu (pk)\n> Trójkąt równoboczny (tr)\n> Zamiana jednostek (zj)", move=False, align="left", font=("Aleo", 13, "normal"))
pen.isvisible()
# pen's 2
pen2 = turtle.Turtle()
pen2.penup()
pen2.color("black")
pen2.hideturtle()

pen3 = turtle.Turtle()
pen3.penup()
pen3.color("black")
pen3.goto(-75, 0)
pen3.hideturtle()
pen3.isvisible()

pen4 = turtle.Turtle()
pen4.penup()
pen4.hideturtle()
pen4.color("black")
pen4.goto(-75, -100)

pen5 = turtle.Turtle()
pen5.hideturtle()
pen5.penup()
pen5.color("black")
pen5.goto(x=-95, y=-150)

pen6 = turtle.Turtle()
pen6.hideturtle()
pen6.penup()
pen6.color("black")
pen6.goto(-113, -100)

pen7 = turtle.Turtle()
pen7.hideturtle()
pen7.penup()
pen7.color("black")
pen7.goto(y=-150, x=-20)

pen8 = turtle.Turtle()
pen8.penup()
pen8.hideturtle()
pen8.color("black")
pen8.goto(-55, 200)
pen8.write('Kalkulator', move=False, align="left", font=("Arial", 15, "normal"))

pen9 = turtle.Turtle()
pen9.hideturtle()
pen9.penup()
pen9.color("black")
pen9.goto(-75, 86)

pen10 = turtle.Turtle()
pen10.penup()
pen10.hideturtle()
pen10.goto(-75, 0)
pen10.color('black')

pen11 = turtle.Turtle()
pen11.penup()
pen11.hideturtle()
pen11.goto(-75, -20)
pen11.color('black')

pen12 = turtle.Turtle()
pen12.penup()
pen12.hideturtle()
pen12.color('black')
pen12.goto(x=-75, y=-20)

pen13 = turtle.Turtle()
pen13.penup()
pen13.hideturtle()
pen13.color('black')
pen13.goto(x=0, y=0)

# picking operation
koniec = False
while not koniec:
    l = turtle.textinput("Liczba", "litera")
    # pole powierzchni
    if l == "pp":
        pen2.goto(y=-70, x=-75)
        pen2.write("Pole powierzchni")
        pen2.write("Obliczasz pola powierzchni:\n>Trójkąt(x)\n>Kwadrat(2x)\n>Romb(3x)\n>Równoległobok(5x)\n>Prostokąt(4x)\n", move=False, align="left", font=("Arial", 10, "normal"))
        x = turtle.textinput("Operacja", "Wpisz x, 2x, 3x, 4x lub 5x")
        if x == "x":
            a = turtle.numinput("Wymiary podstawy", "podaj:")
            h = turtle.numinput("Wysokość: ", "podaj:")
            pp = int(a * h) / 2
        elif x == "2x":
            a = turtle.numinput("Wymiar podstawy: ", '')
            pp = int(a * a)
        # romb
        elif x == "3x":
            x = turtle.textinput("Chcesz skorzystać z długości przekątnych, czy, z długości podstawy i wysokości rombu\nwpisz p jeśli Chcesz skorzystać z długości przekątnych\nlub\n d jeśli chcesz skorzystać z długości podstawy i wysokości rombu: ", '')
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
        pen6.write("Wynik = ")
        pen4.write(pp)
        pen3.hideturtle()
        # stopnie
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
            # pitagoras
    elif l == "pitagoras":
        pen4.goto(-75, -50)
        x = pen3.write("obliczasz przeciwprostokątną", '')
        a = turtle.numinput("Jedna przyprostokątna: ", '')
        b = turtle.numinput("Druga przyprostokątna: ", '')
        pp = a * a + b * b
        pen4.write(pp)
        # pierwiastek
    elif l == "p":
        pen9.goto(-75, -50)
        a = float(turtle.numinput("Pierwiastek", ''))
        pierwiastek = math.sqrt(a)
        pen9.write(('pierwiastek z ') + str(a) + (" to ") + repr(pierwiastek))
        # przekątna kwadratu
    elif l == "pk":
        pen9.goto(-75, -50)
        a = turtle.numinput('Podaj długość boku kwadratu','')
        przekatna = a * 1.41
        pen9.write(str('Przekątna wynosi: ') + (str(przekatna)))
    elif l == "tr":
        pen9.goto(-75, -50)
        pen9.write('Wysokość(w), czy pole trójkąta równobocznego(pt)?', '')
        o = turtle.textinput('w lub pt', '')
        if o == "w":
            a = turtle.numinput('Podstawa trójkąta', '')
            d = (a * 1.73)/2
            pen10.write(str('Wysokość: ')+ str(d))
        elif o == "pt":
            a = turtle.numinput('Podstawa trójkąta', '')
            d = ((a * a)*1.73)/2
            pen10.write(str('Pole: ')+ str(d))
    elif l == "zj":
        pen10.write("Cale na cm(1),\n cm na cale(2), \ngalony na litry(3)", move=False, align="left", font=("Arial", 10, "normal"))
        wybor = turtle.textinput('1, 2 lub 3', '')
        if wybor == "1":
            liczba = turtle.numinput('Podaj liczbę w calach', '')
            wynik = float(liczba)*2.54
            pen9.write('Podana liczba: '+ liczba)
            pen12.write("wynik: " + str(wynik))
        elif wybor == "2":
            liczba = turtle.numinput('Podaj liczbę w cm', '')
            wynik = float(liczba)/2.54
            pen11.write("wynik: " + str(wynik))
        elif wybor == "3":
            liczba = turtle.numinput('Podaj liczbę w galonach', '')
            wynik = float(liczba)*3.79
            pen12.write('podana liczba: '+ liczba)
            pen11.write("wynik: " + str(wynik))
    pen5.write("Czy chcesz wykonac kolejne działanie?\n w tym celu wpisz tak lub nie")
    m = turtle.textinput("Czy chcesz wykonać kolejne działanie?", "tak, lub nie")
    if m == "nie":
        koniec = True
        break
    elif koniec != "tak":
         pen5.write("Niepoprawny wybór")
        
    pen2.clear()
    pen3.clear()
    pen4.clear()
    pen5.clear()
    pen6.clear()
    pen9.clear()
    pen10.clear()
    pen11.clear()

wn.mainloop()