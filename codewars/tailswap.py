def tail_swap(strings):
    first_list = strings[0].split(':')
    second_list = strings[1].split(':')
    
    temp_var = second_list[1]
    second_list[1] = first_list[1]
    first_list[1] = temp_var
    
    return [':'.join(first_list), ':'.join(second_list)]