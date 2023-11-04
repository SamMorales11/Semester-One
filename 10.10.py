while (True):
    try:
        pil = int(input("\nshow menu <7>\nselect calculator = "))
        if pil == 1:
            s = int(input("area of rectangle = Sisi x Sisi\nS = "))
            print(f"= {s} x {s}")
            print("=",s * s)
        elif pil == 2:
            s = int(input("perimeter of rectangle = Sisi * 4\nS = "))
            print(f"= {s} x 4")
            print("=",s * 4)
        elif pil == 3:
             p = int(input("area of rectangular = Panjang x Lebar\nP = "))
             l = int(input("L = "))
             print(f"= {p} x {l}")
             print("=",p * l)
        elif pil == 4:
            p = int(input("perimeter of rectangular = 2(Panjang+Lebar)\nP = "))
            l = int(input("l = "))
            print(f"= 2 * ({p} x {l})")
            print("=",2 * (p + l))
        elif pil == 5:
            a = int(input("area of triangle = 1/2 x alas x tinggi\na = "))
            t = int(input("t = "))
            print(f"= ½ x {a} x {t}")
            print("=",1 / 2 * a * t)
        elif pil == 6:
            a = int(input("perimeter of triangle = sisi A + sisi B + sisi C\na = "))
            b = int(input("b = "))
            c = int(input("c = "))
            print(f"= {a} + {b} + {c}")
            print("=",a + b + c)
        elif pil == 7:
            print(f"""\nMENU
Rectangle
    Area formula <1>
    Perimeter formula <2>
Rectangular
    Area formula <3>
    perimeter formula <4>
Triangle
    Area formula <5>
    perimeter formula <6>

exit            <8>""")
        elif pil == 8:
            print("bye-bye")
            break
        else:
            raise ValueError
    except ValueError:
        print("\ninput salah")    