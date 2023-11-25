#zadanie 5

x = input("Podaj pierwszą liczbę: ")
y = input("Podaj drugą liczbę: ")
z = input("Podaj trzecią liczbę: ")

if x < y:
    highNum = x
    x = y
    y = highNum
if x < z:
    highNum = x
    x = z
    z = highNum
if y < z:
    highNum = y
    y = z
    z = highNum

print(x, y, z)
