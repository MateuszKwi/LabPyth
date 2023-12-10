LiczbaA=int(input("Podaj pierwszą liczbę"))
#print(LiczbaA)
LiczbaB=int(input("Podaj drugą liczbę"))
#print(LiczbaB)
if LiczbaB > LiczbaA:
   highNum = LiczbaB
   lowNum = LiczbaA
elif LiczbaA > LiczbaB:
   highNum = LiczbaA
   lowNum = LiczbaB
while lowNum < highNum:
   lowNum = lowNum + 1
   print(f"{lowNum} {highNum}")
else:
   print("Udało się :) ")
print(f"Teraz obie liczby są równe --> {lowNum} {highNum}")
