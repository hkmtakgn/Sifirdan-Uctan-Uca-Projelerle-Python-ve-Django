# short karar yapısı
age = input("Yaş girin! : ")
print("↓short type↓")
age = int(age)

print("Yaş bilgisi integer bir ifadedir!") if type(age) == int else print("Yaş bilgisi integer değil , string ifadedir!")

# long karar yapısı
print("↓long type↓")
if type(age) == int:
    print("Yaş bilgisi integer")
else:
    print("Yaş bilgisi string")

