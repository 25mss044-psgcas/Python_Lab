students = {
    101: {"name": "Kavya", "marks": 88},
    102: {"name": "Rohan", "marks": 95},
    103: {"name": "Meera", "marks": 79}
}

students[104] = {"name": "Vikram", "marks": 91}
students[103].update({"marks": 84})

print("Search Roll 102:", students.get(102, "Record Not Found"))

removed = students.pop(101)
print("Removed Record (101):", removed)

sorted_students = sorted(
    students.items(),
    key=lambda item: item[1]["marks"],
    reverse=True
)

print("\n--- Sorted Student Leaderboard ---")
for roll, info in sorted_students:
    print(f"Roll No: {roll} | Name: {info['name']} | Marks: {info['marks']}")