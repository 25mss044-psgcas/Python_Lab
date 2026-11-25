print("1. Factorial\n2. Fibonacci Series\n3. Prime Number Check")
choice = int(input("Enter your choice (1-3): "))
n = int(input("Enter a positive integer: "))

if choice == 1:
    if n < 0:
        print("Factorial does not exist for negative numbers.")
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print(f"Factorial of {n} is {fact}")
elif choice == 2:
    a, b = 0, 1
    print("Fibonacci Series:", end=" ")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
elif choice == 3:
    if n <= 1:
        print(f"{n} is not a prime number.")
    else:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{n} is a prime number.")
        else:
            print(f"{n} is not a prime number.")
else:
    print("Invalid choice!")