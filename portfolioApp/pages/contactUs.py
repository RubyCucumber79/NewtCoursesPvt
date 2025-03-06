import streamlit as st

st.header("contact me")
with st.form(key="email_forms"):
    user_email = st.text_input("your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        print()