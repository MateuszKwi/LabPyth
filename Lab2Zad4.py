LiczbaA=int(input("Podaj pierwszą liczbę"))
#print(LiczbaA)
LiczbaB=int(input("Podaj drugą liczbę"))
#print(LiczbaB)
print("\nLiczby parzyste od mniejszej do większej:")
if LiczbaA<=LiczbaB:
    for i in range(LiczbaA, LiczbaB+1):
        if i%2!=0:
            continue
        print(i)
else:
    for i in range(LiczbaA, LiczbaB-1, -1):
        if i%2!=0:
            continue
        print(i)
