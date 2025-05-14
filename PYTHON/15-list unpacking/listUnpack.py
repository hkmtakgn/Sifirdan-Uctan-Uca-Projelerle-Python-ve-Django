# names = [ "Hikmet", "Ahmet", "Mehmet", "Veli" ]

# name1,name2,name3,name4 = names

# print(name1,"\n"+name2,"\n"+name3,"\n"+name4)

# products = ["tablet","telefon","mp3 çalar","buzdolabı","derin dondurucu","fön makinesi"]

# products1 , products2 = products[3:5] , products[:3] + products[-1:]

# print(f"Products1 = {products1} , Products2 = {products2} , All Products = {products}")

# yazilim = ["html","css","bootstrap","javascript","react","python","django"]

# frontEnd,backEnd = yazilim[:-2],yazilim[-2:]

# print(f"FrontEnd => {frontEnd} \nBackEnd => {backEnd}")

isimler = [ "Hikmet", "Ahmet", "Mehmet", "Veli", "Oya", "Jale", "İpek", "Işık" ]

# ilk,ikinci,*geriKalanlar = isimler

# print(f"İlk isim = {ilk} \nİkinci isim = {ikinci} \nGeri Kalanlar = {geriKalanlar}")
# çıktısı ↓
# İlk isim = Hikmet 
# İkinci isim = Ahmet
# Geri Kalanlar = ['Mehmet', 'Veli', 'Oya', 'Jale', 'İpek', 'Işık']

ilkUc,dorduncu,geriKalanlar = isimler[:3],isimler[3],isimler[-4:len(isimler)]

print(f"İlk üç isim = {ilkUc} \nDördüncü isim = {dorduncu} \nGeri kalanlar = {geriKalanlar}")
# çıktısı ↓
# İlk üç isim = ['Hikmet', 'Ahmet', 'Mehmet'] 
# Dördüncü isim = Veli
# Geri kalanlar = ['Oya', 'Jale', 'İpek', 'Işık']

