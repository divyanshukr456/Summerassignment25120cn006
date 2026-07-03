def task_manager():
    tasks = []
    def add_task(t): tasks.append(t)
    def view_tasks():
        for i, t in enumerate(tasks): print(f"{i+1}. {t}")
    def complete_task(i):
        if 0 <= i < len(tasks):
            tasks[i] += " [COMPLETED]"
    while True:
        print("\n1. Add Task\n2. Complete Task\n3. View Tasks\n4. Exit")
        c = input("Choice: ")
        if c == '1': add_task(input("Task: "))
        elif c == '2': complete_task(int(input("Task number: ")) - 1)
        elif c == '3': view_tasks()
        elif c == '4': break
if __name__ == '__main__':
    task_manager()
