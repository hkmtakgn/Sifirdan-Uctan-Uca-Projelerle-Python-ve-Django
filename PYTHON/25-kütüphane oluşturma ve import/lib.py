def name_generator (word_count=1):
    products = ["tablet","telefon","laptop",["buzdolabı","çamaşır makinesi","bulaşık makinesi"],["eldiven","matkap","çivi","çekiç"]]
    new_list = []
    for product in products :
        if type (product) == list :
            for item in product :
                new_list.append(item)
        else:
            new_list.append(product)
    return new_list[:word_count]

name_generator (7)
