import random

a = random.randint(3, 7)
b = random.randint(3, 7)
X = set(random.randint(0, 10) for _ in range(a))
Y = set(random.randint(0, 10) for _ in range(b))

#a
czy_zawiera_5_X=5 in X
print(f"a. Zbiór X zawiera liczbę 5: {czy_zawiera_5_X}")

#b
czy_podzbior_X_Y=X.issubset(Y)
print(f"b. Zbiór X jest podzbiorem zbioru Y: {czy_podzbior_X_Y}")

#c
czy_podzbior_Y_X=Y.issubset(X)
print(f"c. Zbiór Y jest podzbiorem zbioru X: {czy_podzbior_Y_X}")

#d
czy_nadzbior_X_Y=X.issuperset(Y)
print(f"d. Zbiór X jest nadzbiorem zbioru Y: {czy_nadzbior_X_Y}")

#e
czy_nadzbior_Y_X=Y.issuperset(X)
print(f"e. Zbiór Y jest nadzbiorem zbioru X: {czy_nadzbior_Y_X}")

#f
suma_zbiorow=X.union(Y)
print(f"f. Suma zbiorów X i Y: {suma_zbiorow}")

#g
roznica_X_Y=X.difference(Y)
print(f"g. Różnica zbiorów X i Y: {roznica_X_Y}")

#h
roznica_Y_X=Y.difference(X)
print(f"h. Różnica zbiorów Y i X: {roznica_Y_X}")

#i
iloczyn_zbiorow=X.intersection(Y)
print(f"i. Iloczyn zbiorów X i Y: {iloczyn_zbiorow}")

#j
roznica_symetryczna=X.symmetric_difference(Y)
print(f"j. Różnica symetryczna zbiorów X i Y: {roznica_symetryczna}")

#k
najwyzszy_element=max(max(X), max(Y))
print(f"k. Wartość najwyższego elementu w obu zbiorach: {najwyzszy_element}")

#l
element_do_przeniesienia=X.pop()
Y.add(element_do_przeniesienia)
print(f"l. Usunięto pierwszy element ze zbioru X i dodano do zbioru Y:\n   X: {X}\n   Y: {Y}")

#m
Y.update(X)
print(f"m. Przekopiowano wszystkie elementy ze zbioru X do zbioru Y:\n   X: {X}\n   Y: {Y}")

#n
X.clear()
Y.clear()
print(f"n. Oba zbiory zostały wyczyszczone:\n   X: {X}\n   Y: {Y}")