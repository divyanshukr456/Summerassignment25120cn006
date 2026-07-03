def mini_emp():
    emps = []
    while True:
        print("\n1. Add Employee\n2. View Employees\n3. Exit")
        c = input("Choice: ")
        if c == '1': emps.append(input("Emp Name: "))
        elif c == '2': print(emps)
        elif c == '3': break
if __name__ == '__main__':
    mini_emp()
