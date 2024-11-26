#) შემოგდით N, შემდეგ N ცალი რიცხვი. შეინახეთ მასივში, ადგილი გაუცვალეთ
#  პირველ და ბოლო ელემენტს, და მასივი გამობეჭდეთ ეკრანზე.

nums = int(input("please enter amount of numnbers : "))
numbers = []
for i in range(1, nums+1):
    num = int(input("please enter a number : "))
    numbers.append(num)

num0 = numbers[0]
numbers[0] = numbers[-1]
numbers[-1] = num0
print(numbers)