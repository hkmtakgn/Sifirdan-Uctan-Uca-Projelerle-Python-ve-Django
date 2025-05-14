name = "Hikmet"
print("name[0] ile ilk karakter gösterimi('H') : ",name[0])
print("name[3] ile dördüncü karakter gösterimi('m') : ",name[3])

print("Hikmet -> H-0/i-1/k-2/m-3/e-4/t-5 - name[2:4] ile 2 den başla 4'e kadar al('km') yani 3 ve 4.karakterleri alır : ",name[2:4])

print("name[:3] ile bastan basla 3 karakter al : ",name[:3])
print("name[0:3] ile bastan basla 3 karakter al : ",name[0:3])

print("name[-3:] ile sondan basla 3 karakter al : ",name[-3:])
print("name[-3:] ile sondan 2.karakterden basla 4'e kadar al(t = 0,e= -1,m = -2,k = -3,i = -4,H = -5) : ",name[-4:-1])

print("name[::-1] ile bilgiyi ters cevir : ",name[::-1])
print("'Hikmet' -> name[::-2] ile 2 karakter arayla bilgiyi ters cevir : ",name[::-2])

print("name.upper() ile tüm karakterleri büyük yap : ",name.upper())

name = "hikmet"
surname = "akgün"
fullName = name + " " + surname

name2 = "HİkMET"
surname2 = "aKgÜN"
fullName2 = name2 + " " + surname2

print("fullName.capitalize() ile ilk harfi büyük yapar : ",fullName.capitalize())
print("fullName.title() ile ilk harfleri büyük yapar : ",fullName.title())

print("'fullName = hikmet akgün' fullName.swapcase() ile büyükse küçük yap küçükse büyük yap : ",fullName.swapcase())
print("'fullName2 = HİKMET aKgÜN' fullName.swapcase() ile büyükse küçük yap küçükse büyük yap : ",fullName2.swapcase())

print("fullName2.count('k') ile küçük 'k' den kaç tane varsa sayar : ",fullName2.count('k'))
print("fullName2.lower().count('k') ile tüm karakterleri küçük yap ve öyle küçük 'k' karakterlerini say : ",fullName2.lower().count('k'))

print("fullName2.lower() ile tüm karakterleri küçük yap : ",fullName2.lower())

names = ["hikmet","mehmet","seckin"]
print('"-".join(names) ile aralarında "-" olacak sekilde birlestir : ',"-".join(names))

names2 = "-".join(names)
print(names2)

print(names2,"=>>","names2.split('-') ile '-' görülen yerlerden parçalara ayrılır :  ",names2.split("-"))

name = "hikmet"
surname = "Akgün"
fullName = ["Hikmet","Akgün"]

print(name.istitle())
print(surname.istitle())
# print(fullName.istitle()) hatalı kullanım
print("-".join(fullName).istitle())

print("name = hikmet =>> name.isupper() ile name bilgisi karakterleri büyük mü ? sonuc true yada false döner : ",name.isupper())
print("name = hikmet =>> name.islower() ile name bilgisi karakterleri kücük mü ? sonuc true yada false döner : ",name.islower())

print("name = hikmet => name.startswith('i') ile name bilgisi 'i' ile baslıyor mu kontrol edilir ve sonuc true yada false döner : ",name.startswith("i"))
print("name = hikmet => name.startswith('h') ile name bilgisi 'h' ile baslıyor mu kontrol edilir ve sonuc true yada false döner : ",name.startswith("h"))

print("name = hikmet => name.endswith('t') ile name bilgisi 't' ile mi bitiyor kontrol edilir ve sonuc true yada false döner : ",name.endswith("t"))
print("name = hikmet => name.endswith('k') ile name bilgisi 'k' ile mi bitiyor kontrol edilir ve sonuc true yada false döner : ",name.endswith("k"))

print("name = hikmet => ","name.find('k') ile hikmet içinde k arar ve kaçıncı karakterden baslıyor ise onun index numarasını yazar : ",name.find("k"))

print(name.replace("k","z"))
print(name.replace(name[name.find("k")],"t"))

name3 = "HiKmeT"
# print(name3.replace("k","z")) çalışmaz çünkü name3 içindeki HiKmet bilgisindeki K büyük ve bunun için dönüştürme yapılır.Aşağıdaki gibi ;

print("name3.lower().replace('k','z') ile önce name3 bilgisindeki tüm karakterler küçük karakterler yapıldı daha sonra da replace metodu ile küçük k olan karakter z karakterine dönüştürüldü. => ",name3.lower().replace("k","z"))

