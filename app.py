#Addition
def add(a,b):
    return a+b

#Subtraction
def subtract(a,b):
    return a-b

#Multiplication
def multiply(a,b):
    return a*b

#Division
def divide(a,b):
    return a/b

#Take numbers from the user
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

print("Pick one operation")
print("1.Add", "2.Subtract", "3.Multiply", "4.Divide")
#Pick an operation
option=input("Pick: 1,2,3,4: ")
if option == "1":
    print("a", "+", "b", "=", add(a,b))
elif option == "2":
    print("a", "-", "b", "=", subtract(a,b))
elif option == "3":
    print("a", "*", "b", "=", multiply(a,b))
elif option == "4":   
    print("a", "/", "b", "=", divide(a,b))
else: print("Invalid option")
    


