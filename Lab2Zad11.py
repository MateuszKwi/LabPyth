tekst="Python jest super"
IndeksZerowy=tekst[0]
print("Znak z zerowym indeksem:", IndeksZerowy)

Ostatni=tekst[-1]
print("Ostatni znak:", Ostatni)
CoDrugi=tekst[::2]
print("Co drugi znak, zaczynając od zerowego:", CoDrugi)
CoTrzeci=tekst[1::3]
print("Co trzeci znak, zaczynając od pierwszego:", CoTrzeci)
OdDziewiategoDoKonca=tekst[9:]
print("Od dziesiątego do ostatniego znaku:", OdDziewiategoDoKonca)
OdKoncaDoPoczatku=tekst[::-1]
print("Od końca do początku:", OdKoncaDoPoczatku)