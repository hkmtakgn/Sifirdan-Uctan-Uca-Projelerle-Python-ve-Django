products = ["tablet","telefon","laptop",["buzdolabı","çamaşır makinesi","bulaşık makinesi"],["eldiven","matkap","çivi","çekiç"]]

for product in products:
# products içindeki öğeleri product olarak gez
    if type(product) == list:
# eğer product tipi liste ise şunu yap:
        for sub_product in product:
# product liste ise içindeki öğeleri sub_product olarak gez
            print(sub_product)
# print ile sub_product öğesinin çıktısını yazdır
    else:
# if koşulu sağlanmazsa yanii değilse şunu yap:
        print(product)
# print ile product öğesinin çıktısını yazdır

