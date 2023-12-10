wysokosc=int(input("Jaka duża ma być twoja choinka? --> "))
for i in range(1,wysokosc+1):
    print(" "* (wysokosc-i)+"* "*i)