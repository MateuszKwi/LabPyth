rachunki_za_prad={
    'styczeń': 320,
    'luty': 270,
    'marzec': 350,
    'kwiecień': 290,
    'maj': 270
}

#a
wartosci=list(rachunki_za_prad.values())
maksymalna_wartosc=max(wartosci)
minimalna_wartosc=min(wartosci)
suma_wartosci=sum(wartosci)
srednia_wartosc=suma_wartosci/len(wartosci)

print(f"a. Maksymalna wartość: {maksymalna_wartosc} zł")
print(f"   Minimalna wartość: {minimalna_wartosc} zł")
print(f"   Suma wartości: {suma_wartosci} zł")
print(f"   Średnia wartość: {srednia_wartosc} zł")

#b
ostatni_miesiac='maj'
ostatni_rachunek=rachunki_za_prad[ostatni_miesiac]

if ostatni_rachunek>srednia_wartosc:
    print("b. Zacznij oszczędzać")
else:
    print("b. Jesteś bezpieczny")
