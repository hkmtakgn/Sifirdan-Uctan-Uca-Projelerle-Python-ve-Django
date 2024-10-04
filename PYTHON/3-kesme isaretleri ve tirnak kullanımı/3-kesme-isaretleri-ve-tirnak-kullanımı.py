print("Merhaba")
print('merhaba')

print(
    """
    Merhaba
    Hikmet
    Nasılsın?
    """
)

print(
    '''
        iyiyim
        teşekkür ederim
        sen nasılsın?
    '''
)

# print('
# merhaba
# nasılsın
# ')
# hatalı kullanım
# çünkü tek tırnak kullanırken birden falza 
# satıra bilgi giremeyiz

# print("
# merhaba
# python
# ")
# hatalı kullanım 
# çünkü çift tırnak içindeki bilgi de 
# yine aynı satırda olmalı
# birden fazla satıra
# bilgi girilemez

# print("Merhaba Hikmet "Togg" nasıldı?") hatalı kullanım
# çift tırnak içinde çift tırnak kullanılamaz.
# bunun için doğru kullanım aşağıdaki gibi olmalı
print("Merhaba Hikmet \"Fringe\" nasıldı?") 
# yani "\" kullanımı ile hemen sonrasındakini etkisiz eleman moduna alırız
# print('Hikmet sen 'Fringe' dizisini izledin mi?') yanlış kullanım
print('Hikmet sen \'Fringe\' dizisini izledin mi?')
print("Hikmet \nAKGÜN")
# "\n" kullanımı ile bir satır aşağı kaydırdık soonrasındaki bilgiyi
print("Hikmet\tAKGÜN")
print("Hikmet\t\tAKGÜN")
print("Hikmet\t\t\tAKGÜN")
# print("Hikmet\tAKGÜN") "\t" ile tab tuşuna basarmış gibi bir tab boşluk bırakırız
print(
    """
    Merhaba
    Hikmet
    Fringe dizisini
    beğendin mi?
    """
)
print("evet beğendim.\"Fringe\" güzel diziydi!")