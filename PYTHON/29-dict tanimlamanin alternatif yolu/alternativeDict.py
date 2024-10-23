# users = {} boş dictionary

# ilk yöntem ↓
# users = {
#     "admin" : "Hikmet",
#     "user1":"Varşin",
#     "user2":"Sena",
#     "user3":"Tuna",
#     "user4":"Derya"
# }

# ikinci yöntem ↓
admin = "Hikmet"
user1 = "Varşin"
user2 = "Sena"
user3 = "Tuna"
user4 = "Derya"

users = dict(
    admin = admin,
    user1 = user1,
    user2 = user2,
    user3 = user3,
    user4 = user4,
)

print(users)

# şeklinde bir dictionary oluşturulabilir
# çıktısı ↓
# {'admin': 'Hikmet', 'user1': 'Varşin', 'user2': 'Sena', 'user3': 'Tuna', 'user4': 'Derya'} şeklinde olur
