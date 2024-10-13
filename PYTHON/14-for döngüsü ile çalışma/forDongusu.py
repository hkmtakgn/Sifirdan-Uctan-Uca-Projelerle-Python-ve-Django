names = ["Ahmet","Mehmet","Veli","Hikmet"]

# for name in names:
#     print(name)
# çıktısı ↓
# Ahmet
# Mehmet
# Veli
# Hikmet

# for num in range(1,4):
#     print(num)
# çıktısı ↓
# 1
# 2
# 3

# for num in range(4):
#     print(num)
# çıktısı ↓
# 0
# 1
# 2
# 3

# for index,name in enumerate(names,start=1):
#     print(f"{index} - {name}")
#  çıktısı ↓
# 1 - Ahmet
# 2 - Mehmet
# 3 - Veli
# 4 - Hikmet

# for num in range((len(names)-len(names))+1,len(names)):
#     print(f"{num} - {names[num]}")
# çıktısı ↓
# 1 - Mehmet
# 2 - Veli
# 3 - Hikmet

# for num in range(1,101):
#     print(f"Sayı - {num}")
# çıktısı ↓
# Sayı - 1
# Sayı - 2
# Sayı - 3
# ...
# Sayı - 100

# for name in names:
#     newName = name.replace("e","i")
#     print(newName)
# çıktısı ↓
# Ahmit
# Mihmit
# Vili
# Hikmit

# for index,name in enumerate(names,start=1):
#     print(f"{index} - {name}")
#     newName = name.replace("e","i")
#     print(newName)
# çıktısı ↓
# 1 - Ahmet
# Ahmit
# 2 - Mehmet
# Mihmit
# 3 - Veli
# Vili
# 4 - Hikmet
# Hikmit

# for num in range(21):
#     if num % 2 == 0:
#         print(num)
#     else:
#         print(num," → 2 ile tam bölünmüyor")
# çıktısı ↓
# 0
# 1  → 2 ile tam bölünmüyor
# 2
# 3  → 2 ile tam bölünmüyor
# ...
# 19  → 2 ile tam bölünmüyor
# 20

userNum = input("2 ile bölünebilirliğini kontrol etmek için sayı girin! : ")

if userNum.isdigit():
    userNum = int(userNum)
    reaminder = userNum % 2
    result = userNum / 2
    result = int(result)
    if reaminder == 0:
        print("2'ye tam bölünür → kalan : ",reaminder)
        print(f"Sonuç : {result}")
    else:
        print("2'ye tam bölünmez → kalan : ",reaminder)
        print(f"Sonuç : {result}")

else:
    print("Lütfen pozitif bir sayı girin! ")
