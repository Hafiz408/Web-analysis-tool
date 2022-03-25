import streamlit as st
from tool import start
from doc import doc


col1,col2 = st.sidebar.columns([2,5])
col2.image("icon.png",width=100)

col1,col2 = st.sidebar.columns([2,5])
col2.title(""" Log Spy""")      

col1,col2 = st.sidebar.columns([1,8])
col2.title("Menu")

col1,col2 = st.sidebar.columns([2,8])
choice = col2.radio("",['Tool','Brief'])

if choice == 'Tool':
    start()
else:
    doc()