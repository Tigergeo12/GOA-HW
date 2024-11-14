def bubble_sort(list):
    length = len(list)

    for i in range(length-1):
        for j in range(length-1):
            if list[j] > list[j+1]: 
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp

    return list