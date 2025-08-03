import streamlit as st
from bank_app import Bank

st.set_page_config(page_title="Bank Management System", layout="centered")
st.markdown("""
    <style>
        .stApp {
            background-color: #e6f2ff;
            color: #000000;
        }

        section[data-testid="stSidebar"] {
            background-color: #003366;
            color: #ffffff;
        }
        section[data-testid="stSidebar"] * {
            color: #ffffff !important;
        }

        input, textarea, .stNumberInput input {
            background-color: #ffffff !important;
            color: #000000 !important;
            caret-color: #000000 !important;  /* Blinking cursor in black */
        }

        section[data-testid="stSidebar"] div[data-baseweb="select"],
        section[data-testid="stSidebar"] div[role="combobox"] {
            background-color: #ffffff !important;
            color: #000000 !important;
        }
        section[data-testid="stSidebar"] div[role="combobox"] * {
            color: #000000 !important;
        }

        label {
            font-weight: bold;
            color: #000000 !important;
        }

        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }

        .stButton>button:hover {
            background-color: #45a049;
        }

            
/* ERROR box styling: Light red background + Dark red text */
div[data-testid="stNotificationContentError"] {
    background-color: #ffe6e6 !important;
    border-left: 6px solid #b22222 !important;
    padding: 1rem !important;
    border-radius: 6px !important;
}

/* Make error text clearly visible */
div[data-testid="stNotificationContentError"] div[role="alert"] {
    color: #8B0000 !important; /* Dark maroon */
    font-weight: bold !important;
    font-size: 1.1rem !important;
}

/* SUCCESS box styling: Light green background + Dark green text */
div[data-testid="stNotificationContentSuccess"] {
    background-color: #e6ffe6 !important;
    border-left: 6px solid #2e8b57 !important;
    padding: 1rem !important;
    border-radius: 6px !important;
}

/* Make success text clearly visible */
div[data-testid="stNotificationContentSuccess"] div[role="alert"] {
    color: #006400 !important; /* Dark green */
    font-weight: bold !important;
    font-size: 1.1rem !important;
}



        div[data-testid="stNotificationContentError"] * {
            color: #8B0000 !important;  /* Deep maroon */
            font-weight: bold !important;
            font-size: 1rem !important;
        }
    </style>
""", unsafe_allow_html=True)





st.title("Bank Management System \U0001F4B0")

bank = Bank()

menu = st.sidebar.selectbox("Choose Action", [
    "Create Account", "Deposit Money", "Withdraw Money",
    "Show Details", "Update Details", "Delete Account"])

if menu == "Create Account":
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, step=1)
    email = st.text_input("Email")
    pin = st.text_input("PIN (4-digit)", type="password")
    if st.button("Create Account"):
        if not (name and email and pin):
            st.warning("All fields are required.")
        else:
            success, result = bank.create_account(name, int(age), email, int(pin))
            if success:
                st.success("Account Created Successfully")
                st.json(result)
            else:
                st.error(result)

if menu == "Deposit Money":
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1, step=1)
    if st.button("Deposit"):
        success, msg = bank.deposit_money(acc, int(pin), int(amount))
        st.success(msg) if success else st.error(msg)

if menu == "Withdraw Money":
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1, step=1)
    if st.button("Withdraw"):
        success, msg = bank.withdraw_money(acc, int(pin), int(amount))
        st.success(msg) if success else st.error(msg)

if menu == "Show Details":
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    if st.button("Show"):
        success, result = bank.show_details(acc, int(pin))
        if success:
            st.json(result)
        else:
            st.error(result)

if menu == "Update Details":
    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")
    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)", type="password")
    if st.button("Update"):
        success, msg = bank.update_details(acc, int(pin), name, email, new_pin)
        st.success(msg) if success else st.error(msg)

if menu == "Delete Account":
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    if st.button("Delete"):
        success, msg = bank.delete_account(acc, int(pin))
        st.success(msg) if success else st.error(msg)
