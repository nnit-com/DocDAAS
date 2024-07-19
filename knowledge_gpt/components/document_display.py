# components/document_display.py  
import streamlit as st  
  
def show_document(doc):  
    if doc:  
        with st.expander("Document"):  
            st.markdown(f"<p>{doc}</p>", unsafe_allow_html=True)  
 