# components/uploader.py  
import streamlit as st  
from knowledge_gpt.utils import document_processor  
  
def upload_file():  
    return st.file_uploader(  
        "Upload a pdf, docx, or txt file 上传文件",  
        type=["pdf", "docx", "txt"],  
        help="Scanned documents are not supported yet! 扫描的文件不支持",  
        on_change=document_processor.clear_submit,  
    )  
  
def process_file(uploaded_file):  
    return document_processor.parse_file(uploaded_file)  
 