users = {
    "admin" : "Hikmet",
    "user1":"Varşin",
    "user2":"Sena",
    "user3":"Tuna",
    "user4":"Derya"
}

for item in users:
    print(item)
# çıktısı ↓
# admin
# user1
# user2
# user3
# user4  şeklinde sonuç sadece key bilgileri olacaktır.

print(" - " * 15)

# ancak users içindeki keylerin value bilgilerini getirmek için aşağıdaki gibi ;
for item in users:
    print(users[item])
# şeklinde yazılmalı
# çıktısı ↓
# Hikmet
# Varşin
# Sena
# Tuna
# Derya şeklinde gelecektir ekrana
print(" - " * 15)

for item in users:
    print(f"{item} - {users[item]}")
# ile hem key hemde value bilgisi yazdırılır
# çıktısı ↓
# admin - Hikmet
# user1 - Varşin
# user2 - Sena
# user3 - Tuna
# user4 - Derya şeklinde olacaktır
print(" - " * 15)

for key in users.keys():
    print(users[key])
# şeklinde de users dict'inin içindeki keylerini dönerek value bilgisini getirebiliriz
# çıktısı ↓
# Hikmet
# Varşin
# Sena
# Tuna
# Derya
print(" - " * 15)

for value in users.values():
    print(value)
# şeklinde de users içindeki keylerin value bilgisini yazdırabiliriz
# çıktısı ↓
# Hikmet
# Varşin
# Sena
# Tuna
# Derya
print(" - " * 15)

for tupleUsers in users.items():
    print(tupleUsers)
# şeklinde ise users içindeki key ve valueler tuple şeklinde gelecektir
# çıktısı ↓
# ('admin', 'Hikmet')
# ('user1', 'Varşin')
# ('user2', 'Sena')
# ('user3', 'Tuna')
# ('user4', 'Derya')
print(" - " * 15)

for key,value in users.items():
    print(f"Key : {key} → Value : {value}")
# şeklinde ise key ve value bilgileri users içinden alınarak ayrı ayrı kullanılabilir
# çıktısı ↓
# Key : admin → Value : Hikmet
# Key : user1 → Value : Varşin
# Key : user2 → Value : Sena
# Key : user3 → Value : Tuna
# Key : user4 → Value : Derya
print(" - " * 15)
