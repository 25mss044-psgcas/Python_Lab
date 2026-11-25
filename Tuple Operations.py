scores = (85, 92, 78, 92, 88)
print("Scores Tuple:", scores)

print("First score:", scores[0])
print("Last score:", scores[-1])
print("Sliced scores (1:4):", scores[1:4])

print("Length:", len(scores))
print("Maximum:", max(scores))
print("Minimum:", min(scores))
print("Sum:", sum(scores))
print("Count of 92:", scores.count(92))
print("Index of 78:", scores.index(78))

student = ("Arun", 101, ("Python", "DBMS", "OS"))
name, roll_no, subjects = student
print(f"\nStudent Name: {name}, Roll No: {roll_no}")
print("Second Subject in Nested Tuple:", student[2][1])