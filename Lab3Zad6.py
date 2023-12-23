zakupki={
    'Chleb': 2.5,
    'Mleko': 3.0,
    'Szynka': 4.0,
    'Ser': 5.5,
    'Artykuł wysokoprocentowy': 10.0
}

print("Lista zakupów:")
for artykul, kwota in zakupki.items():
    print(f"{artykul}: {kwota} zł")

suma_wydatkow=sum(zakupki.values())
print(f"\nPodsumowanie wydatków: {suma_wydatkow} zł")