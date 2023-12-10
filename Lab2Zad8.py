n=int(input("Podaj liczbę naturalną: "))
a=float(input("Podaj pierwszy wyraz ciągu: "))
r=float(input("Podaj różnicę ciągu: "))

print(f"Następujące {n} elementy ciągu arytmetycznego:")
for i in range(n):
    element=a+i*r
    print(element, end=", ")
