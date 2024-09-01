def triple_trouble(one, two, three):
    res_str = "" 
    for i in range(len(one)):
        res_str += one[i]
        res_str += two[i]
        res_str += three[i]

    return res_str