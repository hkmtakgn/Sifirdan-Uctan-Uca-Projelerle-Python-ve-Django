name = "Hikmet"
surname = "AKGÜN"
age = 30

print(name,"\n",surname,age)

print(age,age+10,age+20)

print(name,surname,age,sep="-")

# sep="-" kullanımı ile "," den sonra boşluk yerine "-" kullanır

year = 2023
print(year)
year = 2024
print(year)

YEAR = 2025
print(year) 
# çıktısı 2024 olur çünkü küçük yazılan değişken olan "year" en son bilgisi 2024'tür.
print(YEAR)
# çıktısı 2025 olur çünkü büyük yazılan değişken olan "YEAR" en son bilgisi 2025'tir.
# ve aynı zamanda büyük yazılan değişkenler değişmemesi gereken değişkenlerdir
# yani değişmesi mümkün olan ancak değişmesi tercih edilmeyen sabit kalınması istenen değişkenlerdir
