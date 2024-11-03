num1 = int(input(" Please enter the first number : "))
num2 = int(input(" Please enter the second number : "))
num3 = int(input(" Please enter the third number : "))
num4 = int(input(" Please enter the fourth number : "))
num5 = int(input(" Please enter the fifth number : "))

list = [num1 , num2 , num3 , num4 , num5]
print(list)

for i in list:
    if i % 2 ==0 :
        print( str(i) + "is an even number ")