names = [
    "Peter", "Bruce", "Steve", "Tony", "Natasha",
    ["Wanda", "Hope", "Danny", "Carol", ["Clint", "Hope", "Wanda", "Jessica"]]
]

def print_data (names,admin,admin_pass,*args,**kwargs):
    for name in names:
        if isinstance(name,list):
            print_data(name,admin,admin_pass,*args,**kwargs)
        else:
            if name.startswith("Jes"):
                print(name,admin,admin_pass,args,kwargs)
            
print_data(names,"Hikmet",1001001,"Derin","Sena","Sinem",nickname="hkmtakgn")

# çıktısı ↓
# Jessica Hikmet 1001001 ('Derin', 'Sena', 'Sinem') {'nickname': 'hkmtakgn'}

