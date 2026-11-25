numbers = list(range(1, 11))
print("Initial List:", numbers)

numbers[2] = 99
numbers.append(15)
print("After Updating & Appending:", numbers)

target = 99
if target in numbers:
    print(f"Element {target} found at index {numbers.index(target)}")
else:
    print(f"Element {target} not found")

numbers.sort()
print("Sorted Ascending:", numbers)
numbers.sort(reverse=True)
print("Sorted Descending:", numbers)

squares = [x ** 2 for x in range(1, 6)]
evens = [x for x in numbers if x % 2 == 0]
print("Squares (1-5) via Comprehension:", squares)
print("Even Numbers from List:", evens)