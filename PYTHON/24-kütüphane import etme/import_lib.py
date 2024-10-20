from time import sleep

names = ["Hikmet","Ahmet","Mehmet","Oya","Veli"]

def print_names (names) :
    for name in names :
        sleep(3)
        print(name)

print_names (names)
print("Tamamlandı!")
