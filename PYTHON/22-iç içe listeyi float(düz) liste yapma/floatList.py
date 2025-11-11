names = [
    "Peter", "Bruce", "Steve", "Tony", "Natasha",
    ["Wanda", "Hope", "Danny", "Carol", ["Clint", "Hope", "Wanda", "Jessica"]]
]

def print_names (names , new_list = list()) :
    for name in names:
        if not type(name) == list:
            new_list.append(name)
        else:
            print_names (name)
    return new_list
    
    
print(print_names(names))

