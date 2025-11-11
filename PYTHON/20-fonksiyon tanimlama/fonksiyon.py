def isim_yazdir () : #tanımlanan fonksiyon
    name = input ("isim gir! ") #name değişkeninin değerini kullanıcıdan al
    if name == "Hikmet" : #eğer name "Hikmet" ise şunu yap
        print (f"Hoşgeldin {name}") #ekrana "Hoşgeldin " ve name değişkeni yazdır
        return name #return ile fonksiyondan dışarı sonuç ver
    else: #eğer değilse şunu yap
        print(f"Hatalı isim! ") #ekrana "Hatalı isim! " yazdır

isim_yazdir () # "isim_yazdir " fonksiyonunu çalıştır

# çıktısı aşağıdaki gibi olur
# name "Hikmet" ise;
# isim gir! Hikmet
# Hoşgeldin Hikmet
# değilse;
# isim gir! Derin
# Hatalı isim! 
