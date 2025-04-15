student_marks = {'Alice': 85, 'Arihant': 99}

input_name = input("Enter the student's name: ")

if input_name in student_marks:
    print(f"{input_name}'s marks: {student_marks[input_name]}")
else:
    print('Student not found.')
