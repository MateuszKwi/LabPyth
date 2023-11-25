#zadanie 1
yo = int(input("Podaj swój wiek: ")

if yo < 0:
    print("Niepoprawnie wpisany wiek.")

elif yo < 4:
    print("Twoje wejście jest darmowe.")

elif 4 <= yo <= 18:
    print("Twój bilet kosztuje 10 zł")

else:
    print("Twój bilet kosztuje 20 zł")