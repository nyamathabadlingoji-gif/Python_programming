# count characters using dictionary 
marks = {
    "Ravi": 85,
    "Anu": 91,
    "John": 76,
    "Rahul": 65,
    "Sneha": 95
}

for name,score in marks.items():
    if score >= 90:
        print(f"{name}: {score}")

# Sum of all marks
total_marks = sum(marks.values())
print(f"Total marks: {total_marks}")


# Highest Marks
highest_marks = max(marks.values())
print(f"Highest marks: {highest_marks}")

# lowest marks
lowest_marks = min(marks.values())
print(f"lowest marks:{lowest_marks}")