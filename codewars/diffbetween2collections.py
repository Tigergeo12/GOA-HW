def diff(a, b):
    new_list = []
    for i in a:
        if i not in b and i not in new_list:
            new_list.append(i)
    for i in b:
        if i not in a and i not in new_list:
            new_list.append(i)
    new_list.sort()
    return new_list