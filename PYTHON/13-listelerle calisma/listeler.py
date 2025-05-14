# listeler ↓
names1 = ["ahmet","mehmet","veli"]
names2 = ["zerda","aydan","nuran"]

fullNames = list(names1+names2)

print(fullNames)


products1 = "laptop,tablet,phone"
products2 = "buzdolabı,çamaşır makinesi,bulaşık makinesi"
listProducts = products1.split(",") + products2.split(",")
print(listProducts)

list1 = ["item1","item2","item3"]
list2 = ["prod1","prod2","prod3"]

longList = [*list1] + [*list2]

print(longList)

gameList = ["Pubg","Call Of Duty","Valorant"]

games = ",".join(gameList)


print(games)

games = games.replace(","," ")

print(games)

games = games.replace(" ",",")

print(games)

games = [games]

games = [game.replace("Call,", "Call ") for game in games]
games = [game.replace("Of,", "Of ") for game in games]

print(games)

# array olan games değişkenini dışarı çıkardık.↓
games = ",".join(games)

# string veri olan games değişkeninde "," olanları bulup "/" ile değiştik.↓
games = games.replace(",","/")

# string halinde olan games değişkenini split metodu ile "/" olan yerlerden ayırarak tekrar dizi haline getirdik.↓
games = games.split("/")

print(games)

gamesChild = ["Mario","Adventure Island","Bomberman"]

print(gamesChild)

# dizi içine dizi yerleştirmek ↓
games.append(gamesChild)

print(games)

# çıktısı ['Pubg', 'Call Of Duty', 'Valorant', ['Mario', 'Adventure Island', 'Bomberman']] şeklinde olur.

