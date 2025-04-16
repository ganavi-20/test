def mark_attendance(students):
    attendance = {}
    for student in students:
        while True:
            status = input(f"Is {student} present? (y/n): ").lower()
            if status == 'y':
                attendance[student] = "Present"
                break
            elif status == 'n':
                attendance[student] = "Absent"
                break
            else:
                print("Please enter 'y' for present or 'n' for absent.")
    return attendance
