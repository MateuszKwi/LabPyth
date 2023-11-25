#zadanie 4

x = 1
print("Równanie kwadratowe: ax^2+bx+c")
a = float(input("Wypisz a: "))
b = float(input("Wypisz b: "))
c = float(input("Wypisz c: "))

kwad = a * (x**2) + b * x + c == 0
delta = b**2 - 4 * a * c
pierwDelta = delta**(1/2)

x0 = -1 * b / 2 * a
x1 = -1 * b - (pierwDelta)/2 * a
x2 = -1 * b + (pierwDelta)/2 * a

if delta < 0:
    print(f"Delta to {delta} i jest mniejsza od 0.")
    print("Nie ma rozwiązania.")

elif delta == 0:
    print(f"Delta to {delta} i jest równa 0")
    print (f"Rozwiązanie: x={x0}")

elif delta > 0:
    print(f"Delta to {delta} i jest większa od 0")
    print (f"Rozwiązanie: x1={x1} oraz x2={x2}")