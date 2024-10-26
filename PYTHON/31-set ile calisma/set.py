list_info = [
    1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9
]  #1'den 9'a kadar olan sayıları bir listeye atıyoruz ve içinde tekrar eden sayılarda var
new_list = []  #Boş bir liste oluşturuyoruz
for item in list_info:  #Listedeki her bir eleman için döngü oluşturuyoruz
  if item not in new_list:  #Eğer eleman listede yoksa

    new_list.append(item)  #

print(new_list)  #Yeni oluşturulan listeyi yazdırıyoruz
# çıktısı: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(" - " * 15)

#2.Yöntem
list_info_two = {
    1, 2, 3, 4, 1, 2, 3, 4, 5, 6
}  #1'den 9'a kadar olan sayıları bir listeye atıyoruz ve içinde tekrar eden sayılarda var

print(list_info_two)  #Yeni oluşturulan listeyi yazdırıyoruz
# çıktısı: {1, 2, 3, 4, 5, 6}
print(" - " * 15)

#3.Yöntem
list_info_three = [
    1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9
]  #1'den 9'a kadar olan sayıları bir listeye atıyoruz ve içinde tekrar eden sayılarda var
new_list_info = set(list_info_three)  #Listeyi set'e çeviriyoruz
print(new_list_info)  #Yeni oluşturulan listeyi yazdırıyoruz

# çıktısı: {1, 2, 3, 4, 5, 6, 7, 8,9}

print(" - " * 15)

users = {
    "Hikmet", "Ahmet", "Mehmet", "Ayşe", "Fatma", "Mehmet", "Ayşe", "Fatma"
}
print(users)
# çıktısı: {'Fatma', 'Hikmet', 'Mehmet', 'Ayşe', 'Ahmet'}
print(" - " * 15)

# users.append("Ali") hata verir çünkü set'lerde append fonksiyonu yoktur

users.add(
    "Ali"
)  # add fonksiyonu append fonksiyonu ile aynı işlevi görür ve "Ali" elemanını set'e ekler"
# çıktısı : {'Fatma', 'Mehmet', 'Ali', 'Ahmet', 'Hikmet', 'Ayşe'}
print(users)
print(" - " * 15)

silinen = users.pop()  #pop fonksiyonu set'lerde eleman silme işlemi yapar
print(silinen)
print(users)
# çıktısı:
# Hikmet
# {'Mehmet', 'Ayşe', 'Ali', 'Fatma', 'Ahmet'}
print(" - " * 15)

new_users = {
    "Hikmet", "Ahmet", "Mehmet", "Ayşe", "Fatma", "Mehmet", "Ayşe", "Fatma"
}
new_users.remove("Ahmet")
print(new_users)
# çıktısı: {'Hikmet', 'Mehmet', 'Fatma', 'Ayşe'}
print(" - " * 15)

new_users.add("Django")
print(new_users)
# çıktısı: {'Hikmet', 'Django', 'Mehmet', 'Fatma', 'Ayşe'}
print(" - " * 15)

#set işleminde listedeki elemanlarınyerleri her zaman değişir

#list işleminde listedeki elemanların yerleri değişmez
new_users_to_list = list(new_users)  #set'i listeye çeviriyoruz
print(new_users_to_list)
# çıktısı: ['Hikmet', 'Ayşe', 'Django', 'Mehmet', 'Fatma']
print(" - " * 15)

new_users_for_discard = {
    "Hikmet", "Ahmet", "Mehmet", "Ayşe", "Fatma", "Mehmet", "Ayşe", "Fatma"
}

new_users_for_discard.discard(
    "Fatma")  #discard fonksiyonu set'lerde eleman silme işlemi yapar
print(new_users_for_discard)
# çıktısı: {'Hikmet', 'Ayşe', 'Ahmet', 'Mehmet'}
print(" - " * 15)

list_one = {
    "Hikmet", "Ahmet", "Mehmet", "Ayşe", "Fatma", "Mehmet", "Ayşe", "Fatma",
    "Derin"
}

list_two = {"Ahmet", "Mehmet", "Ayşe", "Fatma", "Mehmet", "Ayşe", "Fatma"}

print("difference:")
print(list_one.difference(
    list_two))  #difference fonksiyonu set'lerde farklı elemanları alır
print("intersection:")
print(list_one.intersection(
    list_two))  #intersection fonksiyonu set'lerde kesişen elemanları alır
print("union:")
print(list_one.union(list_two))  #union fonksiyonu set'lerde birleştirir

