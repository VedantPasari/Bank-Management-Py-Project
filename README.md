🏦 Bank Management System using Streamlit & File Handling  

A simple yet powerful Banking Application built with Python and Streamlit, simulating essential banking operations like creating an account, deposits, withdrawals, and updates — all stored using local JSON file handling (no database required).  

This project is a successor to my File Handling Project, applying object-oriented principles and real-world logic in a user-friendly interface.  

🚀 Features  
🔐 Secure login with Account Number and 4-digit PIN  
🧾 Create Account with validation (age ≥ 18, valid email, secure PIN)  
💰 Deposit money (up to ₹10,000 at a time)  
🏧 Withdraw money with real-time balance check  
📄 View Account Details  
🔄 Update name, email, or PIN  
❌ Delete account (with confirmation)  
📂 Persistent data storage in data.json file  
🧠 Entirely built using Object-Oriented Programming  


Concepts Used :  
1.Object-Oriented Programming (OOP)  
2.File Handling with JSON  
3.Data validation and form control  
4.Exception handling  
5.Streamlit for frontend UI  
6.Secure data access via PIN-based authentication  
7.Modular code structure  

📁 Bank-System-Project  
│
├── data.json             # Stores all user data in JSON format  
├── bank.py               # Core Bank class with all methods  
├── app.py                # Streamlit frontend interface  
├── README.md             # Project documentation (this file)  


At last, the format in which data is stored in .json file is as follows :  
[  
    {  
        "name": "Rahul",  
        "Age": 22,  
        "email": "rahul@ex.com",  
        "pin": 1234,  
        "AccountNo.": "qA9!z6",  
        "Balance": 3000  
    }  
]  
