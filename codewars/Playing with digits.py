def dig_pow(n, p):

    x = [int(d) for d in str(n)]
    print(n)
    print(p)
    print(x)

    sum = 0

    for i in x:
        sum = sum + i**p
        p = p+1
        print(sum)
        print(sum/n)


    if sum % n == 0:
        return sum/n
    else:
        return -1