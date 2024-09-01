def str_count(strng, letter):
    sum = 0
    for i in strng:
        if str(i) == letter:
            sum += 1
    return sum
    