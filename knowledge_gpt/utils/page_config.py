# utils/page_config.py  
import streamlit as st  
  
def setup():  
    st.set_page_config(page_title="DocGPT", page_icon="📖", layout="wide")  
  
def hide_default_format():  
    hide_format = """  
       <style>  
       #MainMenu {visibility: hidden; }  
       footer {visibility: hidden;}  
       </style>  
       """  
    st.markdown(hide_format, unsafe_allow_html=True)  
 
