#შემოგდით ჯერ N - შესატანი რიცხვების რაოდენობა, შემდეგ კი N ცალი რიცხვი. შეინახეთ რიცხვები
#  მასივში და გამობეჭდეთ შებრუნებული თანმიმდევრობით
# . (მაგ: თუ რიცხვებია 5 7 12, გამობეჭდეთ 12, 7, 5)

nums = int(input("please enter amount of numnbers : "))
numbers = []
for i in range(1, nums+1):
    num = int(input("please enter a number : "))
    numbers.append(num)

new_list = []
for i in range(len(numbers) , -1 , -1 ):
    new_list.append(i)
    
print(new_list)