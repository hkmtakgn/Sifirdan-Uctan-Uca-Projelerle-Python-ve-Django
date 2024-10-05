age = 30
print(type(age),age)

age2 = "33"
print(type(age2),age2)

age2 = int(age2)
print(type(age2),age2)

print("age + age2 = ",age + age2)

tax = 1200 / 0.18
print("tax = ",type(tax),tax)

age = input("Yaş girin! ")
print("Yaş : ",age,type(age))
# print(age + 10) hatalı kullanım çünkü input ile alınan yaş bilgisi string ifadedir.
# string olan yaş ifadesinin integer ifadeye çevirilmesi gerekir.

age = int(age)

print("yaş + 10 : ",age + 10)

print(age == 20)

print(age != 20)

print(age == 30)

print("bool : ",bool(age))

age = -10
print("bool = -10 >> ",bool(age))

age = 0
print("age = 0")
print("bool = 0 >> ",bool(age))

print("bool(age == 0)",bool(age == 0))
print("bool(age != 0)",bool(age != 0))
print("bool(not age == 0)",bool(not age == 0))

age = 15
print("age = 15")
print("10 < age < 20",10 < age < 20)
print("18 < age < 20",18 < age < 20)

age = 18
gender = "f"
print("age = ",age,"gender = ",gender)
print("yaşı 18'den büyük mü veya cinsiyeti kadın mı ? : ",age > 18 or gender == "f" )


age = 18
gender = "m"
print("age = ",age,"gender = ",gender)
print("yaşı 18'den büyük mü veya cinsiyeti kadın mı ? : ",age > 18 or gender == "f" )

age = 18
gender = "m"
print("age = ",age,"gender = ",gender)
print("yaşı 18'den büyük mü ve cinsiyeti kadın mı ? : ",age > 18 and gender == "f" )

age = 19
gender = "f"
print("age = ",age,"gender = ",gender)
print("yaşı 18'den büyük mü ve cinsiyeti kadın mı ? : ",age > 18 and gender == "f" )

