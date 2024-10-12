SYS_USER_NAME = "hkmtakgn"
SYS_PASSWORD = 1234

username = input("kullanici adi girin! : ")
password = input("sifre girin! : ")

# SHORT IF ↓↓↓
print("Password bilgisi integer!") if password == int(password) else print("Password bilgisi string!")

# çıktısı // Password bilgisi string!

# Şimdi ise password bilgisini integer yapalım.

password = int(password)

print("Password bilgisi integer!") if password == int(password) else print("Password bilgisi string!")

# çıktısı // Password bilgisi integer!

# IC ICE IF VE ELIF ↓↓↓
# input ile kullanıcıdan alınan bilgi string olduğundan yaş yani age bilgisi string olacaktır.↓

age = input("Yaşınızı girin! : ")

if type(age) == int:
    if age > 18:
        print("işe alındınız!")
    else:
        print("18 yaşından küçüksünüz!")
else:
    print("yaş bilgisi integer olmalı!")

# şimdi yaş bilgisini integer yapalım ↓

age = int(age)

if type(age) == int:
    if age > 18:
        print("işe alındınız!")
    else:
        print("18 yaşından küçüksünüz!")
else:
    print("yaş bilgisi integer olmalı!")

    