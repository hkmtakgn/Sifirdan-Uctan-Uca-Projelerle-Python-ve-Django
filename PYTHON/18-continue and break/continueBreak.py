names = ["Sena","Sinem","Varşin","Hikmet","Derin","Asude","Ali","Mehmet"]

for name in names:
    if name == "Derin":
        continue
    elif name == "Hikmet":
        print(f"{name} - Admin")
    else:
        print(f"{name} - Standart kullanıcı")

# çıktısı aşağıdaki gibi olacaktır ve "Derin" ismini atlayacaktır
# Sena - Standart kullanıcı
# Sinem - Standart kullanıcı
# Varşin - Standart kullanıcı
# Hikmet - Admin
# Asude - Standart kullanıcı
# Ali - Standart kullanıcı
# Mehmet - Standart kullanıcı

