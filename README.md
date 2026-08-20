# 🏦 Bank Management System

A **console-based Bank Management System** developed using **Python and MySQL**.
This project is designed to practice Python programming, database connectivity, SQL queries, CRUD operations, exception handling, and menu-driven programming.

---

## 📌 Project Overview

The Bank Management System allows users to create and manage their bank accounts through a simple console interface.

After creating an account, users can log in using their **account number and password** and perform various banking operations such as depositing money, withdrawing money, checking their balance, viewing transaction history, changing their password, updating account information, and deleting their account.

The project uses **MySQL** to permanently store account and transaction information.

---

## ✨ Features

### 👤 Account Management

* Create a new bank account
* Automatically generate an account number
* Store customer details
* Set account password
* Set opening balance
* Update account information
* Change password
* Delete account

### 🔐 Login System

* Login using account number and password
* Prevent unauthorized access to account operations
* Logout from the account

### 💰 Banking Operations

* Deposit money
* Withdraw money
* Check available balance
* Prevent withdrawal when there is insufficient balance

### 📜 Transaction Management

* Store deposit transactions
* Store withdrawal transactions
* View transaction history
* Store transaction date and time

### ⚠️ Validation & Exception Handling

* Handle invalid numeric input
* Prevent negative/invalid transaction amounts
* Check sufficient balance before withdrawal
* Handle database errors
* Roll back database changes when an operation fails
* Handle invalid menu choices

---

## 🛠️ Technologies Used

| Technology                 | Purpose                      |
| -------------------------- | ---------------------------- |
| **Python**                 | Application logic            |
| **MySQL**                  | Database management          |
| **mysql-connector-python** | Connecting Python with MySQL |
| **SQL**                    | Database operations          |

---

## 🗄️ Database Structure

The project uses two main tables:

### 1. `create_account`

Stores customer and account information.

| Column              | Description               |
| ------------------- | ------------------------- |
| `account_no`        | Unique account number     |
| `name`              | Customer name             |
| `phn_no`            | Phone number              |
| `account_type`      | Savings/Current account   |
| `pwd`               | Account password          |
| `opening_balance`   | Initial account balance   |
| `available_balance` | Current available balance |

### 2. `transaction_history`

Stores account transactions.

| Column             | Description                             |
| ------------------ | --------------------------------------- |
| `transaction_id`   | Unique transaction ID                   |
| `account_no`       | Account associated with the transaction |
| `transaction_type` | Deposit/Withdraw                        |
| `amount`           | Transaction amount                      |
| `transaction_date` | Date and time of transaction            |

`account_no` in `transaction_history` is related to `account_no` in `create_account` using a **foreign key**.

---

## 🔄 Application Flow

```text
                    BANK MANAGEMENT SYSTEM
                              |
              +---------------+---------------+
              |               |               |
        Create Account      Login           Exit
                              |
                       Authentication
                              |
                         Home Page
                              |
       +----------+-----------+----------+----------+
       |          |           |          |          |
    Deposit    Withdraw   Balance    History    Account
                                                  |
                                      +-----------+-----------+
                                      |           |           |
                                Change Password Update    Delete
```

---

## 📋 Main Menu

```text
================== BANK MANAGEMENT SYSTEM ==================

1. CREATE NEW ACCOUNT
2. LOGIN
3. EXIT
```

### After Login

```text
========== HOME PAGE ==========

1. DEPOSIT
2. WITHDRAW
3. CHECK BALANCE
4. TRANSACTION HISTORY
5. CHANGE PASSWORD
6. UPDATE ACCOUNT
7. DELETE ACCOUNT
8. LOGOUT
```

---

## 💻 Example

### Creating an Account

```text
========== CREATE ACCOUNT ==========

Enter name: Gaganjot
Enter phone number: 9876543210
Enter account type: Savings
Enter password: ****
Enter opening balance: 5000

Account created successfully!
Your Account Number is: 1001
```

### Deposit

```text
========== DEPOSIT ==========

Enter amount you want to deposit: 2000

Amount deposited successfully!
Deposited Amount: ₹2000
```

The available balance is automatically updated in the database and the transaction is added to the transaction history.

### Withdrawal

```text
========== WITHDRAW ==========

Enter amount you want to withdraw: 1000

Amount withdrawn successfully!
Withdrawn Amount: ₹1000
```

If the withdrawal amount is greater than the available balance:

```text
Insufficient Balance!
Available Balance: ₹6000
```

---

## 🔑 SQL Operations Used

The project demonstrates the major CRUD operations:

* **INSERT** → Create account and store transactions
* **SELECT** → Login, balance checking, and transaction history
* **UPDATE** → Deposit, withdrawal, password and account updates
* **DELETE** → Delete account and associated transactions

---

## ⚙️ Requirements

Before running the project, install:

* Python 3.x
* MySQL Server
* MySQL Workbench (optional)
* `mysql-connector-python`

Install the Python connector using:

```bash
pip install mysql-connector-python
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd bank-management-system
```

### 3. Create the MySQL database

```sql
CREATE DATABASE dbbank;
```

### 4. Select the database

```sql
USE dbbank;
```

### 5. Create the required tables

Create the `create_account` and `transaction_history` tables according to the database structure used by the project.

### 6. Configure MySQL

Update the database connection in the Python file if required:

```python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dbbank"
)
```

Replace the password with your MySQL password.

### 7. Run the project

```bash
python mainMenu.py
```

---

## 📁 Project Structure

```text
Bank-Management-System/
│
├── mainMenu.py
├── README.md
└── database/
    └── dbbank.sql
```

> If you have not created a separate `.sql` file yet, you can remove the `database/` folder from this structure.

---

## 🎯 Learning Objectives

This project was developed to practice:

* Python fundamentals
* Functions
* Conditional statements
* Loops
* Match-case
* Exception handling
* Object/database interaction
* MySQL connectivity
* SQL queries
* CRUD operations
* Foreign keys
* Database transactions
* Input validation
* Menu-driven programming

---

## 🔮 Future Improvements

The project can be extended in the future with:

* Fund transfer between accounts
* Admin dashboard
* Account statement generation
* Interest calculation
* Multiple user roles
* Password hashing
* GUI using Tkinter
* Web version using Flask/Django
* More advanced reporting

---

## 👩‍💻 Author

**Gaganjot Kaur**

Computer Science & Engineering Student

---

## ⭐ Project Purpose

This project was created as a **college and learning project** to gain practical experience with **Python, MySQL, SQL queries, database management, and real-world application logic**.
