n=int(input("Podaj wartość n: "))
x=int(input("Podaj wartość x: "))

lista_ciagow=[input(f"Podaj ciąg znakowy {i + 1}: ")[:x] for i in range(n)]

#a
ilosc_znakow=sum(len(ciag) for ciag in lista_ciagow)
print(f"a. Ilość znaków w liście: {ilosc_znakow}")

#b
ilosc_liter_k=sum(ciag.count('k') for ciag in lista_ciagow)
print(f"b. Ilość liter 'k' w liście: {ilosc_liter_k}")

#c
ilosc_ciagow_kt=sum(ciag.count('kt') for ciag in lista_ciagow)
print(f"c. Ilość ciągów 'kt' w liście: {ilosc_ciagow_kt}")

#d
s=int(input("Podaj wartość s: "))
ilosc_ciagow_dluzszych_niz_s=sum(1 for ciag in lista_ciagow if len(ciag) > s)
print(f"d. Ilość ciągów dłuższych niż {s}: {ilosc_ciagow_dluzszych_niz_s}")