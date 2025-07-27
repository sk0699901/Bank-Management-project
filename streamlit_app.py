import streamlit as st
from bank_app import Bank

st.set_page_config(page_title="Banking App", layout="centered")
st.title("🏦 Python Bank System")

option = st.sidebar.radio("Select Operation", [
    "Create Account", "Deposit Money", "Withdraw Money",
    "Show Account Details", "Update Account Info", "Delete Account"
])

if option == "Create Account":
    st.subheader("🧾 Create Account")
    name = st.text_input("Enter your name")
    age = st.number_input("Enter age", min_value=0)
    email = st.text_input("Enter email")
    pin = st.text_input("Enter 4-digit PIN", type="password")

    if st.button("Create"):
        if not name or not email or not pin:
            st.warning("Fill all fields.")
        else:
            success, result = Bank.createaccount(name, int(age), email, int(pin))
            if success:
                st.success("Account Created!")
                st.json(result)
            else:
                st.error(result)

elif option == "Deposit Money":
    st.subheader("💰 Deposit Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amt = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        success, result = Bank.depositmoney(acc, int(pin), int(amt))
        st.success(f"New Balance: ₹{result}") if success else st.error(result)

elif option == "Withdraw Money":
    st.subheader("💸 Withdraw Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amt = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        success, result = Bank.withdrawmoney(acc, int(pin), int(amt))
        st.success(f"New Balance: ₹{result}") if success else st.error(result)

elif option == "Show Account Details":
    st.subheader("📄 Show Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        success, result = Bank.showdetails(acc, int(pin))
        st.json(result) if success else st.error(result)

elif option == "Update Account Info":
    st.subheader("📝 Update Account Info")
    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")

    new_name = st.text_input("New Name (optional)")
    new_email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)", type="password")

    if st.button("Update"):
        success, result = Bank.updatedetails(
            acc, int(pin),
            name=new_name or None,
            email=new_email or None,
            new_pin=int(new_pin) if new_pin else None
        )
        st.success("Updated") if success else st.error(result)

elif option == "Delete Account":
    st.subheader("🗑 Delete Account")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        success, result = Bank.delete(acc, int(pin))
        st.success(result) if success else st.error(result)
