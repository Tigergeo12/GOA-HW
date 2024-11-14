def count_odd_digits(num):
    count = 0
    for i in str(num):
        if int(i) % 2 != 0:
            count += 1
    print(count)