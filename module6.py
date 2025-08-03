student_marks = {
    "alice": 85,
    "bob": 90,
    "charlie":78,
    "daisy": 92
}

name = input("enter the student's name:")
if name in student_marks:
    print(f"{name}'s marks:{student_marks[name]}")
else:
    print("student not found.")