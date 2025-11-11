#Toplama-Cikarma
print(2+2) #ciktisi 4
print(2 + 2) #ciktisi 4
print("2+2 sonucu kactir?",":",2+2)
#ekran ciktisi ↓↓↓
# 4
# 4
# 2+2 sonucu kactir? : 4
# ↑↑↑

#Carpma-Bolme
print(2*5) #ekran ciktisi 10
print("2*5 isleminin sonucu kactir?",2*5) #ekran ciktisi → 2*5 isleminin sonucu kactir? 10 olur.
print(2*8*10) #ekran ciktisi 160 olur.

#Islem Onceligi Ve Parantez Kullanimi
print(2+8*5) #ekran ciktisi 50 olmaz.Sonuc 42 olur.
print((8+2)*5) #ekran ciktisinda sonuc 50 olur.Çünkü islem onceligine gore once parantez icini yapar.

#Kalansiz Bolme
print(2*(50//2),type(2*(50//2)))#ekran ciktisi → 50 <class 'int'> olur.Çünkü "//" sonucu integer yani virgülsüz yapar.
print(2*(50/2),type(2*(50/2)))#ekran ciktisi → 50.0 <class 'float'> olur.Çünkü "/" sonucu float yani virgüllü yapar.
print("3/2 isleminin sonucu = ?",3/2,type(3/2))
print("3//2 isleminin sonucu = ?",3//2,type(3//2))
print("/","sonucu float",",","// ise sonucu integer yapar.")

#Mod Alma (Kalani Bulma) / divmod
print("9%3 isldeminin sonucu nedir?",9%3) #ekran ciktisi → 9%3 isldeminin sonucu nedir? 0 olur.
print("10%8 isleminin sonucu nedir?",10%8) #ekran ciktisi → 10%8 isleminin sonucu nedir? 2 olur.
print(divmod(9,3)) #ekran ciktisi → (3, 0) olur.
print(divmod(10,8)) #ekran ciktisi → (1, 2) olur.
print("divmod(10,8) isleminden : ","10 sayisi 8'e bolunur ve ","bolum : 1","kalan : 2 olur. Ve sonuc : ",divmod(10,8),"olur.")
