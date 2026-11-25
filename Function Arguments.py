def calculate_stats(*numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    highest = max(numbers)
    return total, avg, highest


def student_profile(name, course="Computer Science", **details):
    print(f"\nName: {name} | Course: {course}")
    for key, value in details.items():
        print(f" {key.capitalize()}: {value}")


s, a, m = calculate_stats(75, 85, 90, 95)
print(f"Stats -> Sum: {s}, Average: {a:.2f}, Max: {m}")

student_profile("Ananya")
student_profile(course="Data Science", name="Karthik", city="Coimbatore", grade="A+")