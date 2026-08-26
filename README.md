# ATM Management System 🏦

A simple and interactive ATM Management System built using Python and Streamlit. This project simulates basic ATM operations such as withdrawal, deposit, balance inquiry, and secure login authentication through a clean web-based interface.

---

## 📌 Features

* 🔐 Secure password authentication
* 💰 Cash withdrawal functionality
* ➕ Deposit money feature
* 📊 Real-time balance checking
* 🧾 Automatic currency denomination calculation
* ⚡ Interactive and user-friendly interface using Streamlit

---
.

## 🛠️ Technologies Used

* Python
* Streamlit
* NumPy

---

## 📂 Project Structure

```bash
ATM-Management-System/
│
├── Atm.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ATM-Management-System.git
```

### 2️⃣ Navigate to Project Folder

```bash
cd ATM-Management-System
```

### 3️⃣ Install Dependencies

```bash
pip install streamlit numpy
```

### 4️⃣ Run the Application

```bash
python -m streamlit run Atm.py
```

---

## 🔑 Default Login Credentials

```text
Password : 1234
```

---

## 💳 Available Operations

### Withdrawal

* Withdraw available balance
* Displays currency note breakdown automatically

### Deposit

* Add money to account balance

### Check Balance

* View current available balance instantly

### Exit

* Close ATM session safely

---

## 🧠 Currency Denomination Logic

The system automatically calculates the minimum number of notes required for withdrawal using denominations:

```python
[2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
```

Example:

```text
Withdraw Amount : ₹3780

2000 : 1
500  : 3
200  : 1
50   : 1
20   : 1
10   : 1
```

---

## 📸 User Interface Preview

* Login Screen
* Operation Selection Menu
* Withdrawal & Deposit Forms
* Balance Display Section

---

## 🎯 Learning Outcomes

* Streamlit UI development
* Python conditional logic
* Financial transaction simulation
* Currency denomination algorithms
* Interactive web application handling

---

## 🔮 Future Improvements

* Database integration
* Multiple user accounts
* Transaction history
* PIN change functionality
* Receipt generation
* OTP verification system

---

## 👨‍💻 Author

Developed by Boss 🚀
Aspiring AI & ML Developer

---


