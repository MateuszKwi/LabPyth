#zadanie 4 i 4.1

road = float(input("Wpisz pokonananą przez siebie drogew km: "))
avrConsumption = float(input("Wpisz średnie spalanie swojego samochodu w l/100km: "))
consumption = road * avrConsumption/100
fuelCost = 7.2 * consumption
print(f"Przewidywane zużycie paliwa po pokonaniu {road}km wynosi: {consumption}l, a koszt zużytego paliwa wynosi: {fuelCost}zł")

los = random.randint(1, 100000)
losConsumption = los *avrConsumption/100
losFuel = 7.2 * losConsumption
print(f"Przewidywane zużycie paliwa po pokonaniu losowo wybranych {los}km wynosi: {losConsumption}l, a koszt zużytego paliwa wynosi: {losFuel}zł")