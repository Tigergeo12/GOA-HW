def spin_words(sentence):
    list = sentence.split()
    new_list = []
    for i in list:
        if len(i) >= 5:
            new_list.append(i[::-1])
        else:
            new_list.append(i)
    for x in new_list:
        listToStr = ' '.join(new_list)
    return listToStr
    
        