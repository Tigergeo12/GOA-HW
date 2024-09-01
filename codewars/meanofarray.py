def get_average(marks):
    sum = 0
    for i in marks:
        sum += i
    
    return sum // len(marks)