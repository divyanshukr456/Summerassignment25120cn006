class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def deposit(self, amt):
        self.balance += amt
        print(f"Deposited {amt}. New balance: {self.balance}")
    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print(f"Withdrawn {amt}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

if __name__ == '__main__':
    name = input("Enter account holder name: ")
    acc = BankAccount(name)
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        c = input("Choice: ")
        if c == '1': acc.deposit(float(input("Amount: ")))
        elif c == '2': acc.withdraw(float(input("Amount: ")))
        elif c == '3': print("Balance:", acc.balance)
        elif c == '4': break
