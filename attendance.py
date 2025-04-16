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
def display_attendance(attendance):
    print("\n--- Attendance Report ---")
    for student, status in attendance.items():
        print(f"{student}: {status}")
    print("------------------------")


students_list = ["John", "Alice", "Bob", "Eva", "Sam"]

attendance_record = mark_attendance(students_list)

display_attendance(attendance_record)
