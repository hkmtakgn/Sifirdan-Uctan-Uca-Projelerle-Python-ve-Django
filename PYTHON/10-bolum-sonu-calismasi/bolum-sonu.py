# name = "Hikmet"
# surname = "akgün"
# fullname = name + " " + surname


# print(name[2])
# # 2.İndex numarası yani 3.karakter olan k harfini yazar

# print(name[3:6])
# # Hikmet ismindeki index numarası 3'ten basla 3 dahil olacak ve 6.indexe kadar olanı yaz 6.index dahil değil yani 3.4.5.index numaralı karakterleri yazar.
# # çıktısı "met" olur.

# print(name[:3])
# # 0.indexten başla 3.indexe kadar olanı yazar
# # yani 0.1.2.indexleri yazar
# # çıktısı "Hik" olur.

# print(name[-3:])
# # sondan 3 karakteri yazar.
# # çıktısı "met" olur.

# print(name[:-3])
# # son üç karakteri yazmaz.

# print(name[::-1])
# # ters cevirir yazar.
# # çıktısı temkiH olur.

# print(name[::-2])
# # ters çevirip baştan başlayarak 0.index yazar 1.index atlar 2.index yazar 3.index atlar ve devam eder ekrana çıktısını print yazar.
# # çıktısı "tmi" olur. (temkiH)

# print(name.upper())
# # tüm karakterleri büyük yapar
# # çıktısı "HIKMET" olur.

# print(name.capitalize())
# # ilk karakteri büyük yapar.
# # çıktısı Hikmet olur.

# print(fullname.title())
# # çıktısı "Hikmet Akgün" olur.
# print(name.title())
# # çıktısı "Hikmet" olur.
# print(surname.title())
# # çıktısı "Akgün" olur.
# # ilk karakterleri büyük yapar.

# print(fullname.swapcase())
# # karakterler büyükse küçük yapar küçükse büyük yapar.
# # çıktısı "hIKMET AKGÜN" olur.

# print(fullname.lower())
# # hepsini küçük yapar.

# print(fullname.upper())
# # tüm karakterleri büyük yapar.

# print(fullname.count("k"))
# # belirtilen karakterden kaç tane var sayar.

# array = ["item1","item2","item3"]
# print("-".join(array))
# # "-" ile ayırarak array içindeki itemleri join metodu birleştirir.
# # çıktısı item1-item2-item3 olur.

# forSplit = "Hikmet AKGÜN 1994"
# print(forSplit.split(" "))
# # split ve parantezde belirtilen " " ile boşluk gördüğü yerden ayırarak tek dizi haline getirir.
# # çıktısı ['Hikmet', 'AKGÜN', '1994'] olur.

# print(name.istitle())
# # ile name değişkenindeki değer başlık mı yani ilk karakteri büyük mü sorulur ve cevabı true yada false olur.

# print(name.islower())
# # islower metodu ile name değişkenindeki değerin tüm karakterleri küçük mü sorulur ve cevabı true yada false döner.

# print(name.startswith("k"))
# # ile name içindeki değerin ilk karakteri "k" ile mi başlıyor sorulur ve cevap "true" yada "false" döner.
# # çıktısı "false" olur. Çünkü name içindeki bilgi Hikmet yani "H" ile başlıyor,"k" ile değil.

# print(name.endswith("t"))
# # ile name "t" ile mi bitiyor kontrol edilir ve sonuç "true" olur.

# print("Hikmet akgün = 'g' => ",fullname.find("g"))
# # fullname içinde "g" karakterini arar ve index numarasını yazar.
# # NOT : boşluk 'ta bir karakter sayılır.

# print(fullname.replace("akgün","AKGÜN"))
# # fullname içindeki "akgün" bilgisini "AKGÜN" olarak değiştirir.

name = input("Adınızı girin! ")
surname = input("Soyadınızı girin! ")
age = int(input("Yaşınızı girin! "))

information = f"Ad : {name} \nSoyad : {surname} \nYaş : {age}"

print(information)

print(f"Seneye yaşınız : {age + 1}")

print(f"(2024 yılında hesaplandı)Doğum tarihiniz : {2024 - age}")

# çıktısı ↓
# Adınızı girin! Hikmet
# Soyadınızı girin! AKGÜN
# Yaşınızı girin! 30
# Ad : Hikmet 
# Soyad : AKGÜN
# Yaş : 30 
# Seneye yaşınız : 31
# (2024 yılında hesaplandı)Doğum tarihiniz : 1994
# şeklinde olur.

username = input("Kullanıcı adınızı girin! :")
password = int(input("Şifre girin! : "))

if username == "hkmtakgn" and password == 1234:
    print(f"Hoşgeldin {name}")
else:
    print("Kullanıcı adı veya şifre hatalı!")
