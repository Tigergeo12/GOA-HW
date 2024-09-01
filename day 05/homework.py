num1 = int(input("first number: "))
num2 = int(input("second number: "))
operation = int(input('''risi gaketeba gnebavt: 
             1.+
             2.-
             3.*
             4./
             5.< or >'''))

if operation == 1:
     print(num1 + num2)
elif operation == 2:
     print(num1 - num2)
elif operation == 3:
     print(num1 * num2)
elif operation == 4:
     print(num1 / num2)
elif operation == 5:
     if  num1 > num2:
          print("num1 > num2 ")
     elif operation == 5:
          num1 < num2 
          print("num2 > num1 ")
          #else print("wrong operation ") 

