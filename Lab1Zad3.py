#zadanie 3
a = float(input("Wpisz pierwszą cyfrę: "))

b = float(input("Wpisz drugą cyfrę: "))

x = input("Jakie działanie chcesz wykonać? + | - | * | / | a**b ? ")


działania = {"+": a+b, "-": a-b, "*": a*b, "/": a/b, "a**b": a**b}
print("Wynik wybranego działania to: " + str(działania[x]))