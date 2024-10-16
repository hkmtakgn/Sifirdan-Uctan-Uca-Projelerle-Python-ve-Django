age = input("Lütfen yaşınızı girin! : ")

age = int(age) #Eğer bu satır pasif hale gelirse yaş bilgisi string olacağından while döngüsünden çıkmayacaktır.


while type(age) == str:
    age = input("Lütfen yaşınızı giriniz! : ")
    break
print(f"Merhaba, yaşınız : {age} \nDoğum tarihiniz : {2024 - age}")

# While döngüsünden çıktığında yani yaş bilgisi integer olduğunda çıktısı ↓
# Merhaba, yaşınız : 30 
# Doğum tarihiniz : 1994

# While döngüsünden çıkmazsa çıktısı her zaman aşağıdaki gibi olacaktır ↓
# Lütfen yaşınızı girin! : 

