def create_list(name, amount = 5):
    names = []

    for i in range(amount):
        names.append(name)
    
    return names


#@result = create_list("nia", 3)
print(create_list("nia", 6))