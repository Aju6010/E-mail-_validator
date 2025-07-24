import streamlit as st
from email_validator import validate_email, EmailNotValidError

st.set_page_config(page_title="Email Validator", page_icon="📧")

st.title("📧 Email Validator Tool")
st.markdown("Check whether an email address is valid according to RFC standards.")

email = st.text_input("Enter your email address:")

if st.button("Validate Email"):
    if not email:
        st.warning("Please enter an email address first.")
    else:
        try:
            valid = validate_email(email, check_deliverability=False)
            st.success(f"✅ Valid Email: {valid.email}")
        except EmailNotValidError as e:
            st.error(f"❌ {str(e)}")
