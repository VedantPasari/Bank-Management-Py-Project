import json
import random
import string
from pathlib import Path
import streamlit as st

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            with open(database, 'w') as fs:
                fs.write(json.dumps([]))
    except Exception as err:
        st.error(f"An exception occurred: {err}")

    @staticmethod
    def __update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data, indent=4))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    @staticmethod
    def find_user(accnumber, pin):
        return [i for i in Bank.data if i['AccountNo.'] == accnumber and i['pin'] == pin]

    def create_account(self, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return False, "Account creation failed: Age must be 18+ and PIN must be 4 digits."
        info = {
            "name": name,
            "Age": age,
            "email": email,
            "pin": pin,
            "AccountNo.": Bank.__accountgenerate(),
            "Balance": 0
        }
        Bank.data.append(info)
        Bank.__update()
        return True, info

    def deposit_money(self, accnumber, pin, amount):
        user = self.find_user(accnumber, pin)
        if not user:
            return False, "No matching account found."
        if amount <= 0 or amount > 10000:
            return False, "Invalid deposit amount. Must be between 1 and 10,000."
        user[0]['Balance'] += amount
        Bank.__update()
        return True, "Deposit successful."

    def withdraw_money(self, accnumber, pin, amount):
        user = self.find_user(accnumber, pin)
        if not user:
            return False, "No matching account found."
        if amount > user[0]['Balance']:
            return False, "Insufficient balance."
        user[0]['Balance'] -= amount
        Bank.__update()
        return True, "Withdrawal successful."

    def show_details(self, accnumber, pin):
        user = self.find_user(accnumber, pin)
        if not user:
            return False, "No matching account found."
        return True, user[0]

    def update_details(self, accnumber, pin, name=None, email=None, new_pin=None):
        user = self.find_user(accnumber, pin)
        if not user:
            return False, "No matching account found."
        if new_pin and (not new_pin.isdigit() or len(new_pin) != 4):
            return False, "PIN must be a 4-digit number."
        
        if name:
            user[0]['name'] = name.strip()
        if email:
            user[0]['email'] = email.strip()
        if new_pin:
            user[0]['pin'] = int(new_pin)

        Bank.__update()
        return True, "Details updated successfully."

    def delete_account(self, accnumber, pin):
        user = self.find_user(accnumber, pin)
        if not user:
            return False, "No matching account found."
        Bank.data.remove(user[0])
        Bank.__update()
        return True, "Account deleted successfully."