#numbers = [1,2,4,5,-5,43,6,4,-52]

#for num in numbers:
    #if num < 0:
        #numbers.pop

numbers = [1,2,4,5,-5,43,6,4,-52]

positive_numbers = []
for num in numbers:
    if num >= 0:
        positive_numbers.append(num) 

print(positive_numbers)