#!/usr/bin/python3

if __name__ == "__main__":
from calculator_1 import add, subtract, multiply, divide
a = 10
b = 5
result_add = add(a, b)
result_subtract = subtract(a, b)
result_multiply = multiply(a, b)
result_divide = divide(a, b)
print(f"Adding {a} and {b} equals {result_add}")
print(f"Subtracting {b} from {a} equals {result_subtract}")
print(f"Multiplying {a} and {b} equals {result_multiply}")
print(f"Dividing {a} by {b} equals {result_divide}")`
