# components/main_app.py  
import streamlit as st  
from knowledge_gpt.components import uploader, document_display, query_handler  
  
def run():  
    uploaded_file = uploader.upload_file()  
    document = uploader.process_file(uploaded_file)  
    query = query_handler.get_query()  
    query_handler.handle_query(document, query)  
 