nums = int(input("please enter amount of numnbers : "))
numbers = []
for i in range(1, nums+1):
    num = int(input("please enter a number : "))
    numbers.append(num)

for i in range(len(numbers)):
    if i % 2 != 0:  
        print(numbers[i])