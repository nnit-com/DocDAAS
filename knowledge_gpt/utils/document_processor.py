# utils/document_processor.py  
import streamlit as st  
from knowledge_gpt.utils import file_parser  
  
def clear_submit():  
    st.session_state["submit"] = False  
  
def parse_file(uploaded_file):  
    if uploaded_file:  
        return file_parser.parse(uploaded_file)  
    return None  
 



