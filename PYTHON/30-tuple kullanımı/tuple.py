tuple = (1, 2, 3, [4, 5, 6, "Hikmet"], {7: "Derin", "user3": "Nida"})

print(tuple)
# içinde integer bilgi ile birlikte list ve dictionary var.
# print ile tuple'ın içindeki bilgiyi yazdırıyoruz.
# çıktısı ↓
# (1, 2, 3, [4, 5, 6, 'Hikmet'], {7: 'Derin', 'user3': 'Nida'}) şeklinde olur.
print(" - " * 15)
print(
    tuple[3][3])  #tuple içindeki 3. elemanın içindeki 3. elemanı yazdırıyoruz.
# çıktısı ↓
# "Hikmet" şeklinde olur.
print(" - " * 15)
print(tuple[4].keys()
      )  #tuple içindeki 4. elemanın içindeki anahtarları yazdırıyoruz
print(" - " * 15)
print(tuple[4].values()
      )  #tuple içindeki 4. elemanın içindeki değerleri yazdırıyoruz.
print(" - " * 15)
print(tuple[4].items()
      )  #tuple içindeki 4. elemanın içindeki anahtar-değerleri yazdırıyoruz.
print(" - " * 15)
print(tuple[3][3].upper(
))  #tuple içindeki 3. elemanın içindeki 3. elemanı büyük harfe yazdırıyoruz.
print(" - " * 15)
print(
    tuple[4]["user3"].lower()
)  #tuple içindeki 4. elemanın içindeki user3 anahtarının değerini küçük yazdırıyoruz.
print(" - " * 15)
# tuple.append("Hikmet")
# print(tuple)
#tuple içine veri eklenemez.
tuple[3].append("Seçkin")
print(tuple)
#tuple içindeki listeye veri eklenebilir.
# çıktısı ↓
# (1, 2, 3, [4, 5, 6, 'Hikmet'], {7: 'Derin', 'user3': 'Nida'}) şeklinde olur.
print(" - " * 15)
tuple[4]["admin"] = "Hikmet"  #tuple içindeki dicte admin anahtarını ekliyoruz.
print(tuple)
# çıktısı ↓
# (1, 2, 3, [4, 5, 6, 'Hikmet'], {7: 'Derin', 'user3': 'Nida'}) şeklinde olur.
print(" - " * 15)
print(
    tuple[4]["admin"]
)  #tuple içindeki 4. elemanın içindeki admin anahtarının değerini yazdırıyoruz.
# çıktısı ↓
# Hikmet şeklinde olur.
print(" - " * 15)
tuple[3].pop(3)
print(tuple)
# tuple içindeki 3. elemanın içindeki 3. elemanı siler.
# çıktısı ↓
# (1, 2, 3, [4, 5, 6, 'Hikmet'], {7: 'Derin', 'user3': 'Nida'}) şeklinde olur.
print(" - " * 15)
tuple[3].remove(6)  #tuple içindeki 3. elemanın içindeki 6 elemanını siler.
print(tuple)
# çıktısı ↓
# (1, 2, 3, [4, 5, 6, 'Hikmet'], {7: 'Derin', 'user3': 'Nida'})
print(" - " * 15)
tuple[4].pop(
    "user3")  #tuple içindeki 4. elemanın içindeki user3 anahtarını siler.
print(tuple)
# çıktısı ↓
# (1, 2, 3, [4, 5, 6, 'Hikmet'], {7: 'Derin', 'user3': 'Nida'}) şeklinde olur.
print(" - " * 15)
del (tuple[4]["admin"]
     )  #tuple içindeki 4. elemanın içindeki admin anahtarını siler.
print(tuple)
# çıktısı ↓
# tuple = (1, 2, 3, [4, 5, 6, "Hikmet"], {7: "Derin", "user3": "Nida"}) şeklinde olur.
print(" - " * 15)
tuple[4][
    "admin"] = "Hikmet"  #tuple içindeki 4. elemanın içindeki admin anahtarını ekliyoruz.
print(tuple)
# çıktısı ↓
# tuple = (1, 2, 3, [4, 5, 6, "Hikmet"], {7: "Derin", "user3": "Nida"}) şeklinde olur.
print(" - " * 15)
tuple[3].insert(
    3, "Seçkin"
)  #tuple içindeki 3. elemanın içindeki 3. elemanına Seçkin ekliyoruz.
print(tuple)
# çıktısı ↓
# tuple = (1, 2, 3, [4, 5, 6, "Hikmet"], {7: "Derin", "user3": "Nida"}) şeklinde olur.
print(" - " * 15)
