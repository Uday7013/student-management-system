students = []

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    students.append({"roll": roll, "name": name, "marks": marks})
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")

def update_student():
    roll = input("Enter Roll No to update: ")
    for s in students:
        if s["roll"] == roll:
            s["marks"] = input("Enter new marks: ")
            print("Student updated successfully!")
            return
    print("Student not found.")

def delete_student():
    roll = input("Enter Roll No to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!")
            return
    print("Student not found.")

while True:
    print("\n1.Add Student  2.View Students  3.Update Student  4.Delete Student  5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
