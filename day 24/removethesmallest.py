def remove_smallest(numbers):
    if not numbers: 
        return []
    min_index = numbers.remove(min(numbers))
    return min_index 

#doestn work