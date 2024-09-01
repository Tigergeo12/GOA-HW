def divisors(integer):
    list = []
    for i in range(1,integer+1):
        if integer % i == 0:
            list.append(i)
            
    
    
    return len(list)