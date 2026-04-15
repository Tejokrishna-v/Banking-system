import sqlite3
from datetime import datetime

# ---------------- DATABASE SETUP ----------------
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    account_number TEXT PRIMARY KEY,
    name TEXT,
    balance REAL,
    type TEXT,
    interest_rate REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_number TEXT,
    action TEXT,
    amount REAL,
    time TEXT
)
""")

conn.commit()


# ---------------- CLASSES ----------------

class BankAccount:
    bank_name = "Tejo Krishna International Bank"

    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def update_balance(self, amount):
        self.__balance = amount
        cursor.execute("UPDATE accounts SET balance=? WHERE account_number=?",
                       (self.__balance, self.account_number))
        conn.commit()

    def add_transaction(self, action, amount):
        cursor.execute("""
        INSERT INTO transactions (account_number, action, amount, time)
        VALUES (?, ?, ?, ?)
        """, (self.account_number, action, amount, str(datetime.now())))
        conn.commit()

    def deposit(self, amount):
        if amount > 0:
            new_balance = self.__balance + amount
            self.update_balance(new_balance)
            self.add_transaction("Deposit", amount)
            print(f" Deposited: {amount}")
        else:
            print(" Invalid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            new_balance = self.__balance - amount
            self.update_balance(new_balance)
            self.add_transaction("Withdraw", amount)
            print(f" Withdrawn: {amount}")
        else:
            print(" Insufficient balance")

    def show_transactions(self):
        print("\n---- Transaction History ----")
        cursor.execute("SELECT action, amount, time FROM transactions WHERE account_number=?",
                       (self.account_number,))
        rows = cursor.fetchall()

        if not rows:
            print("No transactions found")
        else:
            for r in rows:
                print(f"{r[2]} | {r[0]} | {r[1]}")

    def display(self):
        print("\n------ Account Details ------")
        print(f"Bank: {BankAccount.bank_name}")
        print(f"Account No: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.__balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, name, balance=0, interest_rate=0.05):
        super().__init__(account_number, name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f" Interest Added: {interest}")


# ---------------- BANK SYSTEM ----------------

class BankSystem:

    def create_account(self, account, acc_type="normal", interest_rate=0.05):
        cursor.execute("SELECT * FROM accounts WHERE account_number=?",
                       (account.account_number,))
        if cursor.fetchone():
            print(" Account already exists")
            return

        cursor.execute("""
        INSERT INTO accounts VALUES (?, ?, ?, ?, ?)
        """, (account.account_number, account.name,
              account.get_balance(), acc_type, interest_rate))
        conn.commit()

        print(" Account Created Successfully")

    def delete_account(self, acc_no):
        cursor.execute("DELETE FROM accounts WHERE account_number=?", (acc_no,))
        cursor.execute("DELETE FROM transactions WHERE account_number=?", (acc_no,))
        conn.commit()
        print(" Account Deleted")

    def get_account(self, acc_no):
        cursor.execute("SELECT * FROM accounts WHERE account_number=?", (acc_no,))
        data = cursor.fetchone()

        if not data:
            return None

        acc_no, name, balance, acc_type, interest_rate = data

        if acc_type == "savings":
            return SavingsAccount(acc_no, name, balance, interest_rate)
        else:
            return BankAccount(acc_no, name, balance)


# ---------------- MAIN ----------------

def main():
    bank = BankSystem()

    while True:
        print("\n===== SMART BANKING SYSTEM =====")
        print("1 Create Account")
        print("2 Deposit")
        print("3 Withdraw")
        print("4 Check Balance")
        print("5 Add Interest (Savings)")
        print("6 Transaction History")
        print("7 Delete Account")
        print("8 Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                acc_no = input("Account Number: ")
                name = input("Customer Name: ")
                acc_type = input("Account Type (normal/savings): ")

                if acc_type.lower() == "savings":
                    account = SavingsAccount(acc_no, name)
                    bank.create_account(account, "savings", account.interest_rate)
                else:
                    account = BankAccount(acc_no, name)
                    bank.create_account(account, "normal")

            elif choice == "2":
                acc_no = input("Account Number: ")
                amount = float(input("Amount: "))
                account = bank.get_account(acc_no)

                if account:
                    account.deposit(amount)
                else:
                    print(" Account not found")

            elif choice == "3":
                acc_no = input("Account Number: ")
                amount = float(input("Amount: "))
                account = bank.get_account(acc_no)

                if account:
                    account.withdraw(amount)
                else:
                    print(" Account not found")

            elif choice == "4":
                acc_no = input("Account Number: ")
                account = bank.get_account(acc_no)

                if account:
                    account.display()
                else:
                    print(" Account not found")

            elif choice == "5":
                acc_no = input("Account Number: ")
                account = bank.get_account(acc_no)

                if isinstance(account, SavingsAccount):
                    account.calculate_interest()
                else:
                    print(" Not a savings account")

            elif choice == "6":
                acc_no = input("Account Number: ")
                account = bank.get_account(acc_no)

                if account:
                    account.show_transactions()
                else:
                    print(" Account not found")

            elif choice == "7":
                acc_no = input("Account Number: ")
                bank.delete_account(acc_no)

            elif choice == "8":
                print(" Thank you for using Tejo Krishna International Bank ")
                break

            else:
                print(" Invalid choice")

        except Exception as e:
            print(" Error:", e)


if __name__ == "__main__":
    main()