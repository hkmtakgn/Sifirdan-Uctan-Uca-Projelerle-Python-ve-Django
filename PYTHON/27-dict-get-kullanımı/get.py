users = {
    "admin" : "Hikmet",
    "user1":"Varşin",
    "user2":"Sena",
    "user3":"Tuna",
    "user4":"Derya"
}

# print(users["user5"])
# print("başarılı!")
# # sonuc hata verecektir çünkü "user5" yok

# print(users.get("user5"))
# print("başarılı!")
# # hata vermeyecek sonuç olarak none ve sonrasında başarılı! yazacaktır. Çünkü get ile varsa getir şeklinde komut verdik
# # çıktısı ↓
# # None
# # başarılı!

print(users.get("user5","Maalesef böyle bir bilgi yok!"))
print("başarılı!")
# user5 bilgisi varsa getirir yoksa "Maalesef böyle bir bilgi yok!" dönecektir
# çıktısı ↓
# Maalesef böyle bir bilgi yok!
# başarılı!

