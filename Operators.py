a = int(input("Enter first integer (a): "))
b = int(input("Enter second integer (b): "))

print("\n--- 1. Arithmetic Operators ---")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b:.2f}")
print(f"Floor Division (a // b): {a // b}")
print(f"Modulus (a % b): {a % b}")
print(f"Exponentiation (a ** b): {a ** b}")

print("\n--- 2. Relational Operators ---")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")

print("\n--- 3. Logical Operators ---")
x, y = True, False
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")

print("\n--- 4. Bitwise Operators ---")
print(f"Bitwise AND (a & b): {a & b}")
print(f"Bitwise OR (a | b): {a | b}")
print(f"Bitwise XOR (a ^ b): {a ^ b}")
print(f"Bitwise NOT (~a): {~a}")
print(f"Left Shift (a << 1): {a << 1}")
print(f"Right Shift (a >> 1): {a >> 1}")

print("\n--- 5. Operator Precedence ---")
expr1 = 10 + 5 * 2 ** 2
expr2 = (10 + 5) * 2 ** 2
print(f"10 + 5 * 2 ** 2 = {expr1}")
print(f"(10 + 5) * 2 ** 2 = {expr2}")