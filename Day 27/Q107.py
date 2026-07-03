def calculate_salary():
    basic = float(input("Enter basic salary: "))
    hra = 0.2 * basic
    da = 0.5 * basic
    pf = 0.1 * basic
    net_salary = basic + hra + da - pf
    print(f"\n--- Salary Slip ---")
    print(f"Basic: {basic}\nHRA: {hra}\nDA: {da}\nPF: -{pf}")
    print(f"Net Salary: {net_salary}")

if __name__ == '__main__':
    calculate_salary()
