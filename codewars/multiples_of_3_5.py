def solution(number):
    sum = 0
    if number < 0:
        return 0
    else:
        for i in range(number):
            if i % 3 == 0 or i % 5 == 0:
                sum = sum + i
                
    return sum
            
print(solution(4))