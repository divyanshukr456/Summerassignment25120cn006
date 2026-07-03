employees = {}
def add_emp():
    emp_id = input("Enter employee ID: ")
    name = input("Enter name: ")
    dept = input("Enter department: ")
    employees[emp_id] = {"Name": name, "Dept": dept}
    print("Added successfully.")

def view_emps():
    for emp_id, details in employees.items():
        print(f"ID: {emp_id}, Name: {details['Name']}, Dept: {details['Dept']}")

if __name__ == '__main__':
    while True:
        print("\n1. Add Employee\n2. View Employees\n3. Exit")
        choice = input("Enter choice: ")
        if choice == '1': add_emp()
        elif choice == '2': view_emps()
        elif choice == '3': break
