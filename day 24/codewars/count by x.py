def count_by(x, n):
    multiples_x = []
    
    for i in range(x, x * n + 1):
        if i % x == 0:
            multiples_x.append(i)
    
    return multiples_x