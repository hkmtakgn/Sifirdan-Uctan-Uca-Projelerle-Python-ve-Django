names = [
    "Peter", "Bruce", "Steve", "Tony", "Natasha",
    ["Wanda", "Hope", "Danny", "Carol", ["Clint", "Hope", "Wanda", "Jessica"]]
]


# def isim_yazdir (names):
#     for name in names:
#         if type(name) != list:
#             print(name)
#         else:
#             isim_yazdir(name)
            
# isim_yazdir(names)


def print_names (names):
    for name in names:
        if type(name) == list:
            print_names(name)
        else:
            print(name)
            
print_names(names)