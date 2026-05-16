# ATM Management System using Streamlit
# python -m streamlit run Atm.py
import streamlit as st
import numpy as np
b=20000
st.title("🏦 Welcome to ATM")
pas = "1234"
en=st.text_input("Enter The Password :",type="password")
if en==pas:
    st.write("Login Successful")
   
    op = st.selectbox(
        "Select Operation",
        ["Withdrawal","Deposit","Check Balance","Exit"]
        )
    if op == "Withdrawal":
        wit = st.number_input("Enter The Amount to Withdraw :", min_value=1)

        if st.button("Submit Withdrawal"):
            if b >= wit:
                st.success("Withdraw Successful 🎉")

                b -= wit
                nt = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
                temp = wit

                for note in nt:
                    count = temp // note
                    temp %= note
                    if count > 0:
                        st.write(f"{note} : {count}")

                st.write(f"Current Balance ₹: {b}")

            else:
                st.error("Insufficient Balance")
    elif op == "Deposit":
            de = st.number_input("Enter amount to deposit:", min_value=1)
            if st.button("Submit Deposit"):
                b+=de  
                st.success(f"Update  Balance ₹:{b}")
    elif op == "Check Balance":
        if st.button("Check"):
            st.write(f"Available balance: ₹{b}")
    elif op=="Exit":
             st.warning("Thank you for using ATM")

elif en != "":
    st.error("Access Denied")
