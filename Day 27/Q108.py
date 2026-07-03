def generate_marksheet():
    name = input("Enter student name: ")
    subs = []
    for i in range(3):
        subs.append(int(input(f"Enter marks for subject {i+1}: ")))
    total = sum(subs)
    avg = total / 3
    grade = "A" if avg >= 80 else "B" if avg >= 60 else "C" if avg >= 40 else "F"
    
    print(f"\n--- Marksheet for {name} ---")
    for i, mark in enumerate(subs):
        print(f"Subject {i+1}: {mark}")
    print(f"Total: {total}\nAverage: {avg:.2f}\nGrade: {grade}")

if __name__ == '__main__':
    generate_marksheet()
