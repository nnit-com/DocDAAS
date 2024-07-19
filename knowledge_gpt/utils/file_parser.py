# utils/file_parser.py  
from knowledge_gpt.utils import text_converter  
  
def parse(uploaded_file):  
    if uploaded_file.name.endswith(".pdf"):  
        return text_converter.parse_pdf(uploaded_file)  
    elif uploaded_file.name.endswith(".docx"):  
        return text_converter.parse_docx(uploaded_file)  
    elif uploaded_file.name.endswith(".txt"):  
        return text_converter.parse_txt(uploaded_file)  
    else:  
        raise ValueError("File type not supported!")  
 

