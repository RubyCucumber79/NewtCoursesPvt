import streamlit as st

st.set_page_config(layout="wide")
col1,col2 = st.columns(2)
with col1:
    st.image("./images/photo.jpg")
with col2:
    st.title("Mohd Shahnawaz Khan")
    content = """Hi, Myself Mohd. Shahnawaz Khan, a final-year undergraduate student at Vellore Institute of Technology (VIT) 
Chennai, pursuing a degree in Electronics and Computer Engineering. Highly passionate about data analytics, 
machine learning, and artificial intelligence, with a proven ability to learn rapidly, adapt to new challenges, 
and thrive in fast-paced environments. Seeking opportunities to grow personally, professionally, and as a 
leader."""
    st.info(content)