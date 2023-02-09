def add (a, b):
    answer = a + b
    print(str(a) + " + ", str(b), " = " + str(answer))


def sub (a, b):
    answer = a - b
    print(str(a) + " - ", str(b), " = " + str(answer))


def multiply(a, b):
    answer = a * b
    print(str(a) + " x ", str(b), " = " + str(answer))


def divide(a, b):
    answer = a / b
    print(str(a) + " / ", str(b), " = " + str(answer))

print ("A, addition")
print ("B, subtraction")
print ("C, multiplication")
print ("D, division")
print ("E, exit")

choice = input("Enter your choice: ")
if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    add (a, b)
elif choice == "b" or choice == "B":
    print('Substraction')
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    sub (a,b)
elif choice == "c" or choice == "C":
    print('Multiplication')
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    multiply (a,b)
elif choice == "d" or choice == "D":
    print('Division')
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number:"))
    multiply (a,b)
elif choice == "e" or choice == "E":
    print('Program ended')
    quit()
   
