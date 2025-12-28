import streamlit as st
from email_validator import validate_email, EmailNotValidError

st.set_page_config(page_title="Email Validator")

st.title("Email Validator")
st.write("Check whether an email address is valid according to RFC standards.")

email = st.text_input("Enter your email address")

if st.button("Validate"):
    if email.strip() == "":
        st.warning("Please enter an email address.")
    else:
        try:
            valid = validate_email(email, check_deliverability=False)
            st.success("Email is valid: " + valid.email)
        except EmailNotValidError as e:
            st.error(str(e))
