# 💰 Smart Banking System (Python + SQLite)

## 📌 Project Overview

The **Smart Banking System** is a console-based application developed using Python and SQLite.
It simulates basic banking operations such as account creation, deposits, withdrawals, and transaction tracking with persistent database storage.


## 🚀 Features

* 🏦 Create Bank Account (Normal & Savings)
* 💵 Deposit Money
* 💸 Withdraw Money
* 📊 Check Account Balance
* 📜 View Transaction History
* 💹 Interest Calculation (Savings Account)
* 🗑 Delete Account
* 💾 Data stored using SQLite Database


## 🛠 Technologies Used

* Python (Core Programming)
* SQLite (Database)
* VS Code (Development Environment)


## 🧠 System Design

The project uses:

* **OOP Concepts** (Classes, Inheritance, Encapsulation)
* **SQLite Database** for persistent storage
* Separate tables:

  * `accounts`
  * `transactions`


## 📂 Project Structure

banking-project/
│
├── bank.py        # Main application file
├── README.md      # Project documentation
├── .gitignore     # Ignore unnecessary files
└── bank.db        # Auto-generated database (not included in repo)


## ▶️ How to Run the Project

### 1️⃣ Clone Repository

git clone https://github.com/your-username/banking-project.git
cd banking-project

### 2️⃣ Run the Application

python bank.py


## 💾 Database Details

* Database Name: bank.db
* Automatically created when the program runs
* Tables:

  * accounts
  * transactions


## 🔒 Sample Functionalities

* Create account with unique account number
* Perform secure deposit and withdrawal
* Track all transactions with timestamps
* Apply interest for savings accounts


## 📸 Output Example

===== SMART BANKING SYSTEM =====
1 Create Account
2 Deposit
3 Withdraw
4 Check Balance
5 Add Interest (Savings)
6 Transaction History
7 Delete Account
8 Exit

## 🎯 Future Enhancements

* 🔐 User Authentication (Login System)
* 🌐 Web Version using Flask/Django
* 📱 GUI Interface (Tkinter)
* 💳 Fund Transfer between accounts

---

## 👨‍💻 Author

**Tejo Krishna**

---

## ⭐ Conclusion

This project demonstrates a real-world banking system using Python and database integration.
It is suitable for beginners to understand backend logic, database handling, and OOP concepts.

---

⭐ *If you like this project, give it a star on GitHub!*
