Liczba=int(input("Podaj liczbę naturalną: "))
PierwszyWyraz=float(input("Podaj pierwszy wyraz ciągu: "))
Roznica=float(input("Podaj różnicę ciągu: "))

print(f"Następujące {Liczba} elementy ciągu arytmetycznego:")
for i in range(Liczba):
    element=PierwszyWyraz+i*Roznica
    print(element, end=", ")