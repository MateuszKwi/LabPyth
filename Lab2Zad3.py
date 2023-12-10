while True:
    try:
       liczba=int(input("Podaj liczbę całkowitą. (Jeżeli wprowadzona zostanie liczba ujemna pętla się zakończy): "))
        if liczba<0:
            print("Wpisano liczbę ujemną. To koniec..... ")
            break
        else:
            print(f"Wpisano liczbę: {liczba}")
    except ValueError:
        print("Złe dane. Podaj liczbę całkowitą.")