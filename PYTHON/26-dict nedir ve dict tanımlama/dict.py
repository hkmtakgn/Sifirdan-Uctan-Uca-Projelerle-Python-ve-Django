# key ve value şeklinde tanımlanan dictionary
users = {
    "admin" : "Hikmet",
    "user1":"Varşin",
    "user2":"Sena",
    "user3":"Tuna",
    "user4":"Derya"
}

# user4 kullanıcısını yazdırma
print(users["user4"]) #users ve köşeli parantez içinde yazılan string ifade ile key bilgisi yazılarak value bilgisini yazdırma
print(" - " * 15)

users["user5"] = "Rihanna" #user5 kullanıcısı olarak "Rihanna" users dict'ine eklendi
print(users["user5"]) #user5'in value'sini yazar çıktısı Rihanna olur
print(" - " * 15)
print(users)
print(" - " * 15)
users["user6"] = "Beyonce" #users içine user6 kullanıcısı "Beyonce" olarak eklendi
print(users)
print(" - " * 15)
users["user6"] = "Shakira" #users içine eklenen user6  "Beyonce" value'si "Shakira" olarak güncellendi
print(users)
print(" - " * 15)
