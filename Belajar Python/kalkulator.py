def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def devide(x, y):
  return x / y

print("Select Operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
  choice = input("Enter choice (1/2/3/4): ")
  if choice in ('1', '2', '3', '4'):
    try:
      num1 = int(input("Enter first number: "))
      num2 = int(input("Enter second number: "))
    except ValueError:
      print("Invalid value, please enter a number")
      continue

    if choice == '1':
      print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
      print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
      print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
      print(f"{num1} / {num2} = {devide(num1, num2)}")
  else:
    print("Invalid choice, please select a valid option (1/2/3/4).")
    continue

  next_calculation = input("Let's do next calculation? (yes/no): ")
  if next_calculation.lower() == "no":
    print("Thank you for using the calculator!")
    break