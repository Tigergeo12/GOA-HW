def square_digits(num):
    sum = ""
    for i in str(num):
        sum = sum + str(int(i)*int(i))
    
    return int(sum)