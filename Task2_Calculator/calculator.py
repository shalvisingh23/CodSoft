# Task 2 - Calculator
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return "Error" if b == 0 else a / b

print("Basic Calculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

if op == "+": print("Result:", add(a, b))
elif op == "-": print("Result:", sub(a, b))
elif op == "*": print("Result:", mul(a, b))
elif op == "/": print("Result:", div(a, b))
else: print("Invalid operation")
