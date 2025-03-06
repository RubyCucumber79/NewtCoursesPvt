import streamlit as st
import pandas as pd

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
content2 = """
Below you can find some of the apps I have built in python, feel free to contact me"""
st.write(content2)

col3,empty_col,col4 = st.columns([1.5,0.5,1.5])
df = pd.read_csv("./portfolioApp/data.csv",sep=";")
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
