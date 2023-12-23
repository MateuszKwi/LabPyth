#Napisy (string)

ListaImion=["Ania", "Zdzichu", "Wiesław", "Grażyna"]
for name in ListaImion:
    print(name)

#a

posortowanaLista=sorted(ListaImion)

#b

posortowanaLista.append("Ludwika")
posortowanaLista.append("Daniel")

imie = posortowanaLista.pop()

print(imie)

#c

posortowanaLista.insert(3, "Ola")

#d
posortowanaLista.reverse()
ListaZdublowana=posortowanaLista*2

for name in posortowanaLista:
    print(name)