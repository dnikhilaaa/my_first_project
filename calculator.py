def add(x,y):
    return x + y

def subtract(x,y):
    return x - y
print("1. Add")
print("2. Subtract")
choice = input("Choose (1/2): ")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == '1':
    print("Result:", add(a, b))
elif choice == '2':
    print("Result:", subtract(a, b))
else:
    print("Invalid choice")
