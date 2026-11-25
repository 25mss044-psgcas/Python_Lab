data = [10, 20, 30]

try:
    idx = int(input("Enter list index (0-2): "))
    divisor = int(input("Enter a divisor: "))
    result = data[idx] / divisor

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input! Please enter integers only.")

except IndexError:
    print("Error: List index out of range!")

else:
    print(f"Calculation Successful! Result = {result:.2f}")

finally:
    print("Execution completed (finally block executed).")