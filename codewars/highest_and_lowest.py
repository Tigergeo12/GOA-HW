def high_and_low(numbers):
    new_numbers = list(map(int, numbers.split()))
    max_num = new_numbers[0]
    min_num = new_numbers[0]
    for i in new_numbers:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    return str(max_num) + " " + str(min_num)