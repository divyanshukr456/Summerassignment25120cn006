students = {}
def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    students[roll] = {"Name": name, "Marks": marks}
    print("Added successfully.")

def view_students():
    for roll, details in students.items():
        print(f"Roll: {roll}, Name: {details['Name']}, Marks: {details['Marks']}")

if __name__ == '__main__':
    while True:
        print("\n1. Add Student\n2. View Students\n3. Exit")
        choice = input("Enter choice: ")
        if choice == '1': add_student()
        elif choice == '2': view_students()
        elif choice == '3': break
