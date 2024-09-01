def length_of_sequence(arr,n):
    if arr.count(n) != 2:
        return 0
    
    first_index = arr.index(n)
    second_index = 0
    
    for index in range(len(arr) - 1, -1, -1):
        if arr[index] == n:
            second_index = index
            break
    
    return len(arr[first_index:second_index + 1])