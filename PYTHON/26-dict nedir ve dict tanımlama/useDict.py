names = [
    "Peter", "Bruce", "Steve", "Tony", "Natasha", "Clint", "Wanda", "Hope",
    "Danny", "Carol"
]

print(names)
print(" - " * 15)
print(names[6])
print(" - " * 15)

users = {
    "user1": "Ahmet",
    "user2": "Mehmet",
    "user3": "Ayşe",
}
print(users["user2"])
print(" - " * 15)

users["user4"] = "Leyla"
print(users)
print(" - " * 15)

admin = "Hikmet"
password = 1234567
age = 30

user_info = dict(admin=admin, password=password, age=age)
print(user_info)
print(" - " * 15)

user_info["password"] = 1453
print(user_info)
print(" - " * 15)

user_info["Doğum tarihi"] = 1994
print(user_info)
print(" - " * 15)
