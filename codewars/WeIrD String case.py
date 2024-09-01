def to_weird_case(words):
    index = 0
    new_words = ""
    for i in words:
        if i == " ":
            index = -1
            new_words = new_words + i
        elif index % 2 == 0:
            new_words = new_words + i.upper()
        else:
            new_words = new_words + i.lower()
        index = index + 1
        
    return new_words
        