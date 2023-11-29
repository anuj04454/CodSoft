def add(x,y):
   return x + y

def subtract(x, y):
    return x - y

def multiply(x,y):
    return x * y

def divide( x ,y):
    return x / y

def modulus(x,y):
    return x%y

def main():
  while True:
    
    x = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /,%): ")
    y= float(input("Enter the second number: "))
  


    if operator == "+":
      result = add(x, y)
    elif operator == "-":
      result = subtract(x,y)
    elif operator == "*":
      result = multiply(x, y)
    elif operator == "/":
      result = divide(x,y)
    elif operator== "%":
       result = modulus(x,y)
    else:
      print("Invalid operator")
      continue

    print(f"{x} {operator} {y} = {result}")

    choice = input("press 1 to continue or press 0 to end (1/0): ")
    if choice != "1":
      print("Thank You!")
      break
    
if __name__ == "__main__":
  main()