def divisors(integer):
    list = []
    for i in range(1,integer):
        if integer % i == 0:
            list.append(i)
            
    list.remove(list[0])
    
    if len(list) == 0:
        return str(integer) +  " is prime"
    else:
        return list