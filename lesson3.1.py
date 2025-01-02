a = int(input("number1: "))
b = int(input("number2: "))
c = input("operation: ")

if c == '*':
    print(a*b)
elif c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '/':
    if b == 0:
        print("Error")
    else:
        print(a/b)