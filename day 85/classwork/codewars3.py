def find_it(seq):
    counts = {}
    for num in seq:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
            
    for num, count in counts.items():
        if count % 2 != 0:
            return num