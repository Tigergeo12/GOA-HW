def narcissistic( value ):
    base_num = len(str(value))
    print(base_num)
    sum = 0
    for i in str(value):
        sum += int(i)**base_num
    if sum == value:
        return True
    else:
        return False