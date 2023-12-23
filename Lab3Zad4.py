#a
imie=input("Podaj imię: ")
print(f"Witaj {imie}")

#b
wiek=input("Podaj swój wiek: ")
print(f"Twój wiek to: {wiek}")

#c
imie_nazwisko=input("Podaj imię i nazwisko (oddzielone spacją): ")
inicjaly="".join(word[0].upper() for word in imie_nazwisko.split())
print(f"Inicjały: {inicjaly}")

#d
lanuch_piec_razy=input("Podaj łańcuch do powtórzenia: ")
print(f"{lanuch_piec_razy}\n" * 5)

#e
pierwszy_lancuch=input("Podaj pierwszy łańcuch: ")
drugi_lancuch=input("Podaj drugi łańcuch: ")
polaczony_lancuch=pierwszy_lancuch + drugi_lancuch
print(f"Połączone łańcuchy: {polaczony_lancuch}")

#f
pierwsza_polowa=pierwszy_lancuch[:len(pierwszy_lancuch)//2]
druga_polowa=drugi_lancuch[len(drugi_lancuch)//2:]
nowy_lancuch=pierwsza_polowa + druga_polowa
print(f"Nowy łańcuch: {nowy_lancuch}")