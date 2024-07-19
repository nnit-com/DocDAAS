# utils/search.py  
import streamlit as st  
from knowledge_gpt.utils import document_indexing, answer_retrieval  
  
def perform_search(document, query):  
    if document and query:  
        index = document_indexing.embed(document)  
        sources = document_indexing.search(index, query)  
        answer_retrieval.display_answer(sources, query)  