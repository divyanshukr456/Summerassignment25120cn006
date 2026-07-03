def student_records():
    names = []
    rolls = []
    while True:
        print("\n1. Add Student\n2. Display All\n3. Exit")
        c = input("Choice: ")
        if c == '1':
            names.append(input("Name: "))
            rolls.append(input("Roll No: "))
        elif c == '2':
            for i in range(len(names)):
                print(f"Roll: {rolls[i]}, Name: {names[i]}")
        elif c == '3': break
if __name__ == '__main__':
    student_records()
