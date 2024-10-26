cars = {"brand": "Ford", "model": "Mustang", "year": 1964}

print(cars["model"])
print(" - " * 15)

# print(cars["km info"])
# böyle bilgi olmadığından hata verir.

print(cars.get("km info"))
# bunda ise get kullanıldığı için hata vermez
# ancak bilgi olmadığından "none" döner.

print(cars.get("km info", "km bilgisi yok!"))
# burada da get kullanıldığı için hata vermez
# ve bilgi olmadığından "km bilgisi yok!" döner.
print(" - " * 15)
