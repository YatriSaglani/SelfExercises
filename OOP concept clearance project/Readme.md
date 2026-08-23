# 🏦 Bank Management System

A **console-based Bank Management System** developed in Python using **Object-Oriented Programming (OOP)** concepts.

The project allows users to create bank accounts, deposit and withdraw money, transfer funds, check balances, and view account statements through a simple menu-driven interface.

---

## 📌 Features

* 👤 Create new customer accounts
* 🏦 Create different types of bank accounts
* 💰 Deposit money
* 💸 Withdraw money
* 🔄 Transfer money between accounts
* 💳 Check account balance
* 📄 View account statements
* 📊 View total number of accounts
* 🕒 Store transaction date and time
* ✅ Validate 10-digit account numbers
* 🚫 Prevent duplicate account numbers
* ⚠️ Handle invalid amounts and insufficient balances

---

## 🏦 Account Types

### 1. Savings Account

* Interest rate: **4%**
* Supports deposits and withdrawals
* Provides an interest calculation feature

### 2. Current Account

* Overdraft facility available
* Default overdraft limit: **₹10,000**
* Allows withdrawals using the overdraft limit

### 3. Premium Savings Account

* Inherits from `SavingsAccount`
* Interest rate: **6%**
* Provides its own withdrawal implementation

---

## 🧩 OOP Concepts Used

This project demonstrates several important Python OOP concepts:

| OOP Concept                 | Implementation                                     |
| --------------------------- | -------------------------------------------------- |
| **Class & Object**          | `Person`, `Customer`, `Account`, `Bank`            |
| **Inheritance**             | `Customer → Person`                                |
| **Multilevel Inheritance**  | `PremiumSavingsAccount → SavingsAccount → Account` |
| **Abstraction**             | `Account` uses `ABC` and `@abstractmethod`         |
| **Encapsulation**           | Account balance is managed through a property      |
| **Polymorphism**            | Different account classes implement `withdraw()`   |
| **Class Method**            | `get_total_accounts()`                             |
| **Static Method**           | `validate_account_number()`                        |
| **Composition/Aggregation** | `Bank` manages customers and accounts              |

The `Account` class maintains the account balance through a property and setter, while its `withdraw()` method is abstract.

---

## 🗂️ Project Structure

```text
Bank Management System/
│
├── Bank management system.py
└── README.md
```

---

## 🔄 System Flow

```text
Start
  │
  ▼
Bank Management System
  │
  ├── Create New Account
  │       ├── Customer Details
  │       ├── Account Number
  │       └── Account Type
  │
  ├── Deposit Money
  │
  ├── Withdraw Money
  │
  ├── Transfer Money
  │
  ├── Check Balance
  │
  ├── Print Statement
  │
  ├── View Total Accounts
  │
  └── Exit
```

---

## ⚙️ Requirements

* **Python 3.x**
* No external libraries are required.

The project uses Python's built-in `abc` module for abstraction and `datetime` for recording transaction timestamps.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd Bank-Management-System
```

### 3. Run the Python file

```bash
python "Bank management system.py"
```

---

## 🖥️ Main Menu

When the program starts, the following menu is displayed:

```text
=======================================================
             BANK MANAGEMENT SYSTEM
=======================================================
1. Create New Account
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. Check Balance
6. Print Statement
7. View Total Accounts (classmethod)
8. Exit
=======================================================
```

---

## 💳 Transaction Management

Every deposit, withdrawal, interest addition, and transfer is recorded in the account's transaction history along with the date and time.

Example:

```text
23-08-2026 08:30 PM | Deposit | Rs. 5000
23-08-2026 08:45 PM | Withdraw | Rs. 1000
23-08-2026 09:00 PM | Transfer to 1234567890 | Rs. 2000
```

The transaction history is displayed through the **Account Statement** option.

---

## 🔐 Account Validation

The system validates account numbers to ensure that they:

* Contain exactly **10 digits**
* Are numeric
* Are not already registered

This validation is implemented using a static method.

---

## 📚 Classes

### `Person`

Stores basic personal information:

* Name
* Age
* Address

### `Customer`

Inherits from `Person` and additionally stores a customer ID.

### `Account`

Abstract base class responsible for:

* Account number
* Account holder
* Balance
* Deposits
* Transaction history

### `SavingsAccount`

Provides savings account functionality and interest calculation.

### `CurrentAccount`

Provides an overdraft facility.

### `PremiumSavingsAccount`

Extends `SavingsAccount` with a premium savings account implementation.

### `Bank`

Manages:

* Customers
* Accounts
* Account creation
* Deposits
* Withdrawals
* Transfers
* Balance checking
* Account statements

---

## 📝 Example Operations

### Deposit

```text
Enter account number : 1234567890
Enter amount to deposit : Rs. 5000

Amount deposited successfully.
Current Balance : Rs. 15000
```

### Withdraw

```text
Enter account number : 1234567890
Enter amount to withdraw : Rs. 2000

Amount withdrawn successfully.
Current Balance : Rs. 13000
```

### Transfer

```text
Enter sender account number   : 1234567890
Enter receiver account number : 9876543210
Enter amount to transfer     : Rs. 3000

Money transferred successfully.
```

---

## 🎯 Purpose of the Project

This project was created to demonstrate the practical implementation of **Object-Oriented Programming in Python** through a real-world banking application.

It is suitable for learning and demonstrating:

* Python classes and objects
* Inheritance
* Abstraction
* Encapsulation
* Polymorphism
* Class methods
* Static methods
* Object relationships
* Basic transaction management

---

## 🚀 Future Improvements

Possible improvements include:

* 🔐 User authentication and login
* 💾 Database integration using MySQL/SQLite
* 🔒 PIN/password protection
* 🧾 Export statements to PDF
* 📧 Email notifications
* 🖥️ Graphical User Interface (GUI)
* 📱 Mobile/web interface
* 🗃️ Persistent transaction storage
* 🧑‍💼 Admin dashboard

---

## 👩‍💻 Author

**Yatri Saglani**

Computer Engineering Student

---

## 📄 License

This project is created for **educational and academic purposes**.
