import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    # Load existing data
    if Path(database).exists():
        with open(database) as fs:
            data = json.load(fs)
    else:
        with open(database, 'w') as fs:
            json.dump(data, fs)

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __accountgenerate(cls):
        parts = random.choices(string.ascii_letters, k=3) + \
                random.choices(string.digits, k=3) + \
                random.choices("!@#$%^&*", k=1)
        random.shuffle(parts)
        return "".join(parts)

    @classmethod
    def createaccount(cls, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return False, "Age must be 18+ and PIN must be 4 digits."

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "account number": cls.__accountgenerate(),
            "balance": 0
        }

        cls.data.append(info)
        cls.__update()
        return True, info

    @classmethod
    def authenticate(cls, acc_num, pin):
        return next((user for user in cls.data if user["account number"] == acc_num and user["pin"] == pin), None)

    @classmethod
    def depositmoney(cls, acc_num, pin, amount):
        user = cls.authenticate(acc_num, pin)
        if not user:
            return False, "Account not found."

        if amount <= 0 or amount > 10000:
            return False, "Amount must be between 1 and 10000."

        user["balance"] += amount
        cls.__update()
        return True, user["balance"]

    @classmethod
    def withdrawmoney(cls, acc_num, pin, amount):
        user = cls.authenticate(acc_num, pin)
        if not user:
            return False, "Account not found."

        if user["balance"] < amount:
            return False, "Insufficient funds."

        user["balance"] -= amount
        cls.__update()
        return True, user["balance"]

    @classmethod
    def showdetails(cls, acc_num, pin):
        user = cls.authenticate(acc_num, pin)
        if user:
            return True, user
        else:
            return False, "Invalid credentials."

    @classmethod
    def updatedetails(cls, acc_num, pin, name=None, email=None, new_pin=None):
        user = cls.authenticate(acc_num, pin)
        if not user:
            return False, "Account not found."

        if name:
            user["name"] = name
        if email:
            user["email"] = email
        if new_pin:
            user["pin"] = new_pin

        cls.__update()
        return True, user

    @classmethod
    def delete(cls, acc_num, pin):
        user = cls.authenticate(acc_num, pin)
        if not user:
            return False, "Account not found."

        cls.data.remove(user)
        cls.__update()
        return True, "Account deleted successfully."
