
# components/query_handler.py  
import streamlit as st  
from knowledge_gpt.utils import document_processor, search  
  
def get_query():  
    return st.text_area("Ask a question about the document 对文件提问题", on_change=document_processor.clear_submit)  
  
def handle_query(document, query):  
    if st.session_state.get("submit"):  
        search.perform_search(document, query)  
 

