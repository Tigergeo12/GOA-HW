def number_of_occurrences(element, sample):
    occurence = 0
    for i in sample:
        if i == element:
            occurence = occurence + 1
    return occurence
            