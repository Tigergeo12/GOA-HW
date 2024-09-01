def no_odds(values):
    new_list = []
    for i in values:
        if i % 2 == 0:
            new_list.append(i)
    return new_list
            