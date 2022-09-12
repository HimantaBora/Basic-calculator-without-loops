print ("\t WELCOME TO HIMANTA'S CALCULATOR")
a1 = "+"
b1 = "-"
c1 = "*"
d1 = "/"
a = int(input("Enter the first number\n"))
b = int(input("Enter the second number\n"))
print("Signs =\t ' +', '-', '*', '/' ")
c = input("Enter the sign from above line\n")
if c==a1:
    print("The sum of two numbers is\n", a + b )
elif c==b1:
    print("The substraction of two numbers is\n", a - b)
elif c == c1:
    print("The multiplication of two numbers is \n", a * b)
elif c == d1:
    print("The division of two numbers is\n", a / b)
else:
    print("None you not entered the sign")
                  